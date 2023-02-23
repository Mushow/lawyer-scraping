class Lawyer:
    def __init__(self, lawyer_name, lawyer_number, lawyer_email, address):
        self.set_name(lawyer_name)
        self.set_number(lawyer_number)
        self.set_email(lawyer_email)
        self.set_address(address)

    def set_name(self, name):
        self.lawyer_name = name

    def set_number(self, lawyer_number):
        self.lawyer_number = lawyer_number

    def set_email(self, lawyer_email):
        self.lawyer_email = lawyer_email

    def set_address(self, lawyer_address):
        self.address = lawyer_address

    def get_name(self):
        return self.lawyer_name

    def get_number(self):
        return self.lawyer_number

    def get_email(self):
        return self.lawyer_email

    def get_address(self):
        return self.address
