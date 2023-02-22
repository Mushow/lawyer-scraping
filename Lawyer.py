class Lawyer:
    def __init__(self, lawyer_name, lawyer_number, lawyer_email, cases, sworn_date, address, city):
        self.set_name(lawyer_name)
        self.set_number(lawyer_number)
        self.set_email(lawyer_email)
        self.set_cases(cases)
        self.set_sworn_date(sworn_date)
        self.set_address(address)
        self.set_city(city)

    def set_name(self, name):
        self.lawyer_name = name

    def set_number(self, number):
        self.lawyer_number = number

    def set_email(self, email):
        self.lawyer_email = email

    def set_cases(self, cases):
        self.cases = cases

    def set_sworn_date(self, sworn_date):
        self.sworn_date = sworn_date

    def set_address(self, address):
        self.address = address

    def set_city(self, city):
        self.city = city

    def get_name(self):
        return self.lawyer_name

    def get_number(self):
        return self.lawyer_number

    def get_email(self):
        return self.lawyer_email

    def get_cases(self):
        return self.cases

    def get_sworn_date(self):
        return self.sworn_date

    def get_address(self):
        return self.address

    def get_city(self):
        return self.city
