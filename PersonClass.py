
class Person:

    def __init__(self, name, address, phone):
        self.name = name
        self.address = address
        self.phone = phone

    def get_name(self):
        return self.name

    def get_address(self):
        return self.address

    def get_phone(self):
        return self.phone

    def print_person(self):
        print(f'{self.name}, {self.address}, {self.phone}')


class Customer(Person):

    def __init__(self, name, address, phone, cust_num, mailing_list):

        Person.__init__(self, name, address, phone)

        self.cust_num = cust_num
        self.mailing_list = mailing_list

    def print_customer(self):

        Person.print_person(self)

        print(f'Customer Number: {self.cust_num}')

        if self.mailing_list() == True:
            print('On mailing list: Yes')
        else:
            print('Not on mailing list.')
