class Calculator():
    def __init__(self, principal, down_payment, interest, insurance, hoa, taxes, mortgage_type):
        self.principal = principal
        self.down_payment = down_payment
        self.interest = interest / 100
        self.insurance = insurance
        self.hoa = hoa
        self.taxes = taxes / 100
        self.mortgage_type = mortgage_type
    def calculate(self):
        mortgage = ((self.principal - self.down_payment) + (self.hoa * 12 * self.mortgage_type) + (self.principal * self.taxes) + (self.insurance * 12 * self.mortgage_type) + (((self.principal - self.down_payment) * self.interest) * self.mortgage_type)) / (self.mortgage_type * 12)

        return int(mortgage)


