from .payment_base import Payment

class CashPayment(Payment):

    def pay(self, amount: float) -> bool:
        print(f"Cash Paid : {amount}")
        return True