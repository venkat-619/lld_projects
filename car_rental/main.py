
from datetime import date

from car_rental.location import Location
from car_rental.user import User
from car_rental.store import Store
from car_rental.vehical_rental_system import VehicleRentalSystem
from car_rental.vehicle_product import Vehicle, VehcileType
from car_rental.reservation import ReservationType
from car_rental.bill import DailyBillingStrategy
from car_rental.payment import UPIPaymentStrategy


def main():
    print("\n===== LLD: Car Rental System Demo =====")

    rental_system = VehicleRentalSystem()

    store_1_location = Location(
        building_no = 82079,
        area = "Electronic city Phase I",
        city = "Bengaluru",
        state = "Karnataka",
        country = "India",
        pincode = 560100
    )

    store_1 = Store(store_id=1001, location=store_1_location)
    rental_system.add_store(store_1)

    user_1 = User(user_id = 501, user_name = "Venkat", driving_license_no = "DL12345")
    user_2 = User(user_id = 502, user_name = "Adithya", driving_license_no = "DL31245")

    rental_system.add_user(user_1)
    rental_system.add_user(user_2)

    v1 = Vehicle(vehicle_id = 1, vehicle_number = "KA1300", vehicle_type = VehcileType.TWO_WHEELER)
    v1.set_daily_rental_cost(600)
    v2 = Vehicle(vehicle_id = 2, vehicle_number = "KA2500", vehicle_type = VehcileType.FOUR_WHEELER)
    v1.set_daily_rental_cost(2000)
    v3 = Vehicle(vehicle_id = 3, vehicle_number = "KA1560", vehicle_type = VehcileType.FOUR_WHEELER)
    v1.set_daily_rental_cost(1500)

    store_1.inventory.add_vechile(v1)
    store_1.inventory.add_vechile(v2)
    store_1.inventory.add_vechile(v3)

    selected_store = rental_system.get_store(1001)

    from_date = date(2026, 9, 25)
    to_date = date(2026, 9, 28)

    print(f"\nAvailable vehicles from {from_date} to {to_date}:")

    for v in selected_store.get_vehicles(VehcileType.FOUR_WHEELER, from_date, to_date):
        print(f" - {v.vehicle_id}: {v.vehicle_type.name}")


    print("\nCreating reservation...")

    reservation = selected_store.create_reservation(
        vehicle_id=1,
        user=user_1,
        from_date=from_date,
        to_date=to_date,
        reservation_type=ReservationType.DAILY
    )

    print(f"Reservation created with ID: {reservation.reservation_id}")

    print("\nStarting trip...")
    selected_store.start_trip(reservation.reservation_id)

    print("Submitting vehicle...")
    selected_store.submit_vehicle(reservation.reservation_id)

    print("\nGenerating bill...")
    bill = selected_store.generate_bill(
        reservation_id=reservation.reservation_id,
        billing_strategy=DailyBillingStrategy(selected_store.inventory)
    )

    print(f"Bill ID: {bill.bill_id}")
    print(f"Bill Amount: {bill.total_bill_amount}")

    print("\nProcessing Payment...")

    payment = selected_store.make_payment(
        bill=bill, 
        payment_strategy=UPIPaymentStrategy(), 
        payment_amount=bill.total_bill_amount
    )

    print("\n===== PAYMENT RECEIPT =====")
    print(f"Payment ID: {payment.payment_id}")
    print(f"Paid Amount: {payment.amount_paid}")
    print(f"Payment Mode: {payment.payment_mode.value}")
    print(f"Payment Date: {payment.payment_date}")
    print("============================")

if __name__ == "__main__":
    main()