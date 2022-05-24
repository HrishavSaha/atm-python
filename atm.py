class atm:
    def __init__(self, card_number, pin, balance):
        self.card_number = card_number
        self.pin = pin
        self.balance = balance

    def CashWithdrawal(self):
        return "200$ withdrawn"

    def BalanceEnquiry(self):
        return "Card Number: " + self.card_number, "Balance: " + self.balance

card_number = input("Please type your card number: ")
pin = input("Please type your PIN: ")

atm_user_1 = atm(card_number, pin, "500$")

print(atm_user_1.CashWithdrawal())
print("")
print(atm_user_1.BalanceEnquiry())