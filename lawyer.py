class Lawyer:
    def __init__(self, lawyer_name, lawyer_number, lawyer_email, cases, sworn_date, address, city):
        self.lawyer_name = lawyer_name
        self.lawyer_number = lawyer_number
        self.lawyer_email = lawyer_email
        self.cases = cases
        self.sworn_date = sworn_date
        self.address = address
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
