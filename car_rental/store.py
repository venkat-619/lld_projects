
from typing import List
from datetime import date

from car_rental.location import Location
from car_rental.user import User
from car_rental.vehicle_product import VehcileType, Vehicle, VehicleInventoryManager
from car_rental.payment import Payment, PaymentManager, PaymentStrategy, UPIPaymentStrategy
from car_rental.bill import Bill, BillManager, BillingStrategy, DailyBillingStrategy
from car_rental.reservation import Reservation, ReservationType, ReservationManager

class Store:

    def __init__(self, store_id: int, location: Location):
        self.store_id = store_id
        self.store_location = location

        self.inventory: VehicleInventoryManager = VehicleInventoryManager()
        self.reservation_manager: ReservationManager = ReservationManager(self.inventory)
        self.bill_manager: BillManager = BillManager(DailyBillingStrategy(self.inventory))
        self.payment_manager: PaymentManager = PaymentManager(UPIPaymentStrategy())

    def get_vehicles(self, vehcile_type: VehcileType, from_date: date, to_date: date) -> List[Vehicle]:
        return self.inventory.get_available_vehicles(vehcile_type, from_date, to_date)

    def create_reservation(
        self, vehicle_id: int, user: User, from_date: date, to_date: date, reservation_type: ReservationType
    ) -> Reservation:
        return self.reservation_manager.create_reservation(
            vehicle_id, user, from_date, to_date, reservation_type
        )

    def cancel_reservation(self, reservation_id: int) -> None:
        self.reservation_manager.cancel_reservation(reservation_id)

    def start_trip(self, reservation_id: int) -> None:
        self.reservation_manager.start_trip(reservation_id)

    def submit_vehicle(self, reservation_id: int) -> None:
        self.reservation_manager.submit_vehicle(reservation_id)

    def generate_bill(self, reservation_id: int, billing_strategy: BillingStrategy) -> Bill:

        reservation = self.reservation_manager.find_by_id(reservation_id)

        if reservation is None:
            raise Exception("Reservation not found...")

        self.bill_manager.set_billing_strategy(billing_strategy)
        return self.bill_manager.generate_bill(reservation)

    def make_payment(self, bill: Bill, payment_strategy: PaymentStrategy, payment_amount: float) -> Payment:

        self.payment_manager.set_payment_strategy(payment_strategy)
        payment = self.payment_manager.make_payment(bill, payment_amount)

        if not bill.bill_paid:
            raise Exception("Payment Failed...")

        self.reservation_manager.remove(bill.reservation_id)
        return payment

    