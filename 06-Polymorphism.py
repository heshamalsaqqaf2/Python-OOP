"""
  ? System Mangment Payment In E-commerc:
    1- Class Abstract => Payemnt
       1.1 - Abstract Method -> Process_payment
    
    2- Type CreaditCard-Payment  
    3- Type Paypal-Payment  
    4- Type CashPayment

    5- Create Function Accepted Payments
"""

from abc import ABC, abstractmethod


# Create Abstract Class
class Payemnt(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass


class CreaditCardPayment(Payemnt):
    def process_payment(self, amount):
        return f"Process BY CreditCard Paymant Of ${amount}"


class PayPalPayment(Payemnt):
    def process_payment(self, amount):
        return f"Process BY PayPal Paymant Of ${amount}"


class CashPayment(Payemnt):
    def process_payment(self, amount):
        return f"Process BY Cash Paymant Of ${amount}"


class MesterCardPayment(Payemnt):
    def process_payment(self, amount):
        return f"Process BY Mester Paymant Of ${amount}"

class MesterCardPayment2(Payemnt):
    def process_payment(self, amount):
        return f"Process BY Mester2 Paymant Of ${amount}"


# Functions Acccept Payment
def accept_payment(paymrnt_method, amount):
    return paymrnt_method.process_payment(amount)


# Polymorphism
credit_card = CreaditCardPayment()
payPal = PayPalPayment()
cash = CashPayment()
mestar = MesterCardPayment()
mestar2 = MesterCardPayment2()


print(accept_payment(credit_card, 100))
print(accept_payment(payPal, 500))
print(accept_payment(cash, 800))
print(accept_payment(mestar, 200))
print(accept_payment(mestar2, 20000))
