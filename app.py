from RatioObtainer import RatioObtainer
import pip._vendor.requests 

class App:
    base_currency = None
    target_currency = None
    amount = None

    def __init__(self, command_arguments):
        self.amount = command_arguments[1]
        print(self.amount)
        self.base_currency = command_arguments[2]
        print(self.base_currency)
        self.target_currency = command_arguments[3]
        print(self.target_currency)

    def get_result_equation(self):
        base_currency_amount = str(self.amount) + " " + str(self.base_currency)
        target_currency_amount = str((self.get_ratio()) * float(self.amount)) + " " + self.target_currency
        return base_currency_amount + " = " + target_currency_amount

    def get_ratio(self):
        obtainer = RatioObtainer(base=self.base_currency, target=self.target_currency)
        print(self.base_currency)
        
        if not obtainer.was_ratio_saved_today():
            obtainer.fetch_ratio()
        return obtainer.get_matched_ratio_value()
