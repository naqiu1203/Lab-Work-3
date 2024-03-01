"""
    Program Purpose: To ask user to input data and select room type, number of rooms and numbers og nights staying at
    the hotel with services that can be choose from as additional add-on.
    Programmer: MUHAMMAD AFIF NAQIUDDIN BIN OTHMAN
    Date: 1 March 2024
"""
from datetime import datetime

# Define room types and their nightly rates
room_types = ["Single", "Double", "Suite"]
nightly_rates = [100, 150, 250]

# Define additional services and their prices
services = ["Breakfast", "WiFi", "Gym Access"]
service_prices = [10, 5, 20]


# Function to calculate total cost booking confirmation
def get_total_cost(room_type, num_rooms, check_in, check_out, selected_services):
    try:
        # Convert check-in and check-out dates to datetime objects
        check_in_date = datetime.strptime(check_in, "%Y-%m-%d")
        check_out_date = datetime.strptime(check_out, "%Y-%m-%d")

        # Validate check-out date is after check-in date
        if check_in_date >= check_out_date:
            print("Check-out date must be after check-in date.")
            return None

        # Calculate number of nights
        num_nights = (check_out_date - check_in_date).days
        if num_nights <= 0:
            print("Invalid number of nights.")
            return None

        # Calculate room cost
        rate = nightly_rates[room_types.index(room_type)]
        room_cost = rate * num_rooms * num_nights

        # Calculate service cost
        service_cost = sum(service_prices[i] for i in selected_services)

        # Calculate total cost
        total_cost = room_cost + service_cost

        # Display reservation details
        print("\nReservation Details:")
        print("Hotel: Mayang Sari Hotel")
        print("Room Type:", room_type)
        print("Number of Rooms:", num_rooms)
        print("Check-in Date:", check_in)
        print("Check-out Date:", check_out)
        print("Selected Services:")
        for service_index in selected_services:
            print("-", services[service_index])
        print("Total Cost: $", total_cost)

        # Prompt for booking confirmation
        confirm_booking = input("Confirm booking (yes/no): ")
        if confirm_booking.lower() == "yes":
            print("Booking confirmed. Thank you! For choosing to stays the nights at Mayang Sari Hotel.")
            return total_cost
        else:
            print("Booking canceled. Thank you for using our system.")
            return None

    except ValueError:
        print("Invalid room type or date format.")
        return None
    except Exception as e:
        print("An error occurred:", str(e))
        return None


def main():
    # Display welcome message and available room types with rates
    print("Welcome to the Mayang Sari Hotel Reservation System!")
    print("Room Types and Nightly Rates:")
    for i, room_type in enumerate(room_types):
        print(f"{i + 1}. {room_type} - ${nightly_rates[i]} per night")

    # Prompt user for reservation details
    room_type = input("Enter the room type (1, 2, or 3): ")
    if not room_type.isdigit() or int(room_type) not in range(1, len(room_types) + 1):
        print("Invalid room type.")
        return

    num_rooms = input("Enter the number of rooms: ")
    if not num_rooms.isdigit() or int(num_rooms) <= 0:
        print("Invalid number of rooms.")
        return

    check_in = input("Enter the check-in date (YYYY-MM-DD): ")
    check_out = input("Enter the check-out date (YYYY-MM-DD): ")

    # Display available services with prices
    print("\nAdditional Services and Prices:")
    for i, service in enumerate(services):
        print(f"{i + 1}. {service} - ${service_prices[i]}")

    selected_services = []
    while True:
        service_choice = input("Select additional services (enter the service number or 'done' to finish): ")
        if service_choice == "done":
            break
        elif service_choice.isdigit() and int(service_choice) in range(1, len(services) + 1):
            selected_services.append(int(service_choice) - 1)
        else:
            print("Invalid service choice.")

    # Calculate total cost and handle booking confirmation
    total_cost = get_total_cost(room_types[int(room_type) - 1], int(num_rooms), check_in, check_out, selected_services)

    if total_cost is not None:
        print("Total Cost: $", total_cost)


main()
