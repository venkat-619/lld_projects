from .payment_base import Payment

class UPIPayment(Payment):

    def pay(self, amount: float) -> bool:
        print(f"UPI Paid : {amount}")
        return True