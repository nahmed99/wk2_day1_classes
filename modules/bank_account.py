class BankAccount:

    # constructor method - if you needs to pass data to the class.
    # self needs to be the first parameter in ALL methods in a class!
    # self needs to be the first parameter in ALL methods in a class!
    # self needs to be the first parameter in ALL methods in a class!
    def __init__(self, input_holder_name, input_balance, input_type):

        #instance variables
        self.holder_name = input_holder_name
        self.balance = input_balance
        self.type = input_type


    # methods: functions in classes
    def pay_in(self, amount):
        self.balance += amount


    def pay_monthly_fee(self):
        self.balance -= 50