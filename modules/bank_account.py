class BankAccount:

    # constructor method - if you needs to pass data to the class.
    # self needs to be the first parameter in ALL methods in a class!
    # self needs to be the first parameter in ALL methods in a class!
    # self needs to be the first parameter in ALL methods in a class!
    def __init__(self, input_holder_name, input_balance, input_type):

        #instance variables - all needs to be prefixed by "self."
        self.holder_name = input_holder_name
        self.balance = input_balance
        self.type = input_type

        # The underscore ( '_' in "_rates") *indicates* that this variable should 
        # NOT be accessed from outside of the class. It not enforceable.
        self._rates = {
            "personal" : 10,
            "business" : 50
        }


    # methods: functions in classes
    def pay_in(self, amount):
        self.balance += amount


    def pay_monthly_fee(self):
        self.balance -= self._rates[self.type]

        # The line above replaces all of the code below
        #
        # if self.type == "business":
        #     self.balance -= 50
        # elif self.type == "personal":
        #     self.balance -= 10        
        #