class BankAccount:

    # constructor method - if you needs to pass data to the class.
    # self needs to be the first parameter!
    def __init__(self, input_holder_name, input_amount, input_type):

        #instance variable
        self.holder_name = input_holder_name
        self.amount = input_amount
        self.type = input_type

