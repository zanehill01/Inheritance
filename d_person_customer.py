import d_person_customer_class as p

def main():
    # Local variables
    name = 'John'
    address = '1234 Main St'
    phone_number = '123-456-7890'
    cust_number = 1234
    on_list_flag = False
    

    # Create an instance of the Person class
    person1 = p.Person(name, address, phone_number)
 

    # Create an instance of the Customer class.
    customer1 = p.Customer(name, address, phone_number, cust_number, on_list_flag)


    # Display information for the Person.
    person1.print_person()


    print()
    print()
    print()
    
    # Display information for the Customer.
    customer1.print_person()


##    name = 'Jack'
##
##    customer1.set_person_name(name)
##
##    customer1.print_person()
    

# Call the main function.
main()

