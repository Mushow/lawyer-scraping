class Lawyer:
    def __init__(self, name, number, email, address, website):
        self.set_name(name)
        self.set_number(number)
        self.set_email(email)
        self.set_address(address)
        self.set_website(website)

    def set_name(self, name):
        self.lawyer_name = name
        return self

    def set_number(self, number):
        self.lawyer_number = number
        return self

    def set_email(self, email):
        self.lawyer_email = email
        return self

    def set_address(self, address):
        self.address = address
        return self

    def set_website(self, website):
        self.website = website

    def get_name(self):
        return self.lawyer_name

    def get_number(self):
        return self.lawyer_number

    def get_email(self):
        return self.lawyer_email

    def get_address(self):
        return self.address

    def get_website(self):
        return self.website
