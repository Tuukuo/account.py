class Account:
    def __init__(self, account_owner, current_balance=0):
        self.account_owner = account_owner
        self.balance = current_balance
        self.transactions = []  

    def view_account_details(self):
        print(f"Account Owner is {self.account_owner}")
        print(f"Current Balance is {self.balance}")

    def change_account_owner(self, new_owner):
        self.account_owner = new_owner
        print(f"Account owner changed to  {self.account_owner}")

    def account_statement(self,recent_transactions):
        self.recent_transactions=recent_transactions
        print(f"recent transactions is {self.recent_transactions}")

    def set_overdraft_limit(self, overdraft_limit):
        self.overdraft_limit = overdraft_limit
        print(f"Overdraft limit set to {self.overdraft_limit}")

    def calculate_interest(self, annual_interest_rate):
        monthly_interest_rate = annual_interest_rate / 12 / 100
        interest_amount = self.balance * monthly_interest_rate
        self.balance += interest_amount
        print(f"Interest applied is ${interest_amount}")

    def freeze_account(self):
        self.is_frozen = True
        print("Account frozen.")

    def unfreeze_account(self):
        self.is_frozen = False
        print("Account unfrozen.")

    def transfer_funds(self, target_account, amount):
        if self.balance >= amount:
            self.balance -= amount
            target_account.balance += amount
            self.add_transaction("Transfer Out", -amount)
            target_account.add_transaction("Transfer In", amount)
            print(f"${amount:.2f} transferred to {target_account.account_owner}.")
        else:
            print("Insufficient balance for transfer.")

    def close_account(self):
        self.balance = 0
        self.transactions = []
        print("Account closed.")


if __name__ == "__main__":
    my_account = Account(account_owner="Dorcas Tuukuo", current_balance=20000)
    my_account.view_account_details()
    my_account.change_account_owner("Mary Jane")
    my_account.calculate_interest(4.5)
    my_account.transfer_funds(target_account=my_other_account, amount=2500)
    my_account.add_transaction("Deposit", 3000)
    my_account.account_statement()
    my_account.close_account()
    