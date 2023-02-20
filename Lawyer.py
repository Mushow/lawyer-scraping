class Lawyer:
    def __init__(self, lawyerName, lawyerNumber, lawyerEmail, cases, swornDate, address, city):
        self.name = lawyerName
        self.number = lawyerNumber
        self.email = lawyerEmail
        self.cases = cases
        self.swornDate = swornDate
        self.address = address
        self.city = city

    def get_name(self):
        return self.name

    def get_number(self):
        return self.number

    def get_email(self):
        return self.email

    def get_cases(self):
        return self.cases

    def get_sworn_date(self):
        return self.swornDate

    def get_address(self):
        return self.address

    def get_city(self):
        return self.city
