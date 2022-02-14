class Person:
    def __init__(self, name, address, phone_number):
        self.__name = name
        self.__address = address
        self.__phone_number = phone_number

    
    def get_name(self):
        return self.__name
        
    def get_address(self):
        return self.__address
    
    def get_phone_number(self):
        return self.__phone_number
    
##    def set_name(self,name):
##        self.__name = name

    def print_person(self):
        print('Name:',self.__name)
        print('Addr:',self.__address)
        print('Phone:',self.__phone_number)
        
        
class Customer(Person):
    def __init__(self, name, address, phone_number, cust_number, on_list):
        # Call superclass __init__ method
        Person.__init__(self, name, address, phone_number)

        # Initialize the cust_number and on_list attributes
        self.__cust_number = cust_number
        self.__on_list = on_list

##    def set_person_name(self,name):
##        Person.set_name(self,name)
        

    def print_person(self):
        print(Person.print_person(self))
##        print('Name:',Person.get_name(self))
##        print('Addr:',Person.get_address(self))
##        print('Phone:',Person.get_phone_number(self))
        print('Customer Number:',self.__cust_number)
        if self.__on_list:
            print('On Mailing List: Yes')
        else:
            print('On Mailing List: No')



