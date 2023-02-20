
class Person:

    def __init__(self, name, address, phone):
        self.name = name
        self.address = address
        self.phone = phone

    def print_person(self, name, address, phone):
        print(f'{name}, {address}, {phone}')


class Customer(Person):

    def __init__(self, name, address, phone, cust_num, mailing_list):

        Person.__init__(self, name, address, phone)

        self.cust_num = cust_num
        self.mailing_list = mailing_list

        def print_customer(self):
            return self.person
