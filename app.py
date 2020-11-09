from modules.bank_account import BankAccount

account = BankAccount("John", 500, "business")
account_2 = BankAccount("Osian", 1000, "personal")

print(account.holder_name)
print(account_2.holder_name)

account_2.holder_name = "Sarah"
print(account_2.holder_name)

print("balance before pay_in: ", account_2.balance)
account_2.pay_in(250)
print(f"balance after pay_in: {account_2.balance}")


print("balance before pay_monthly_fee: ", account_2.balance)
account_2.pay_monthly_fee()
print(f"balance after pay_monthly_fee: {account_2.balance}")
