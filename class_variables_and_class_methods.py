class Bank:
      bank_name = "Meezan bank"
      def __init__(self, customer_name):
        self.customer_name = customer_name

      @classmethod
      def change_bank(cls,newBank):
        cls.bank_name = newBank

      def show_details(self):
        print(f"Customer: {self.customer_name}, Bank: {self.bank_name}")

bank = Bank("Talha")
bank.show_details()

bank1 = Bank("Talha")
bank1.change_bank("Allied")
bank1.show_details()
# print(math_utils.bank_name)