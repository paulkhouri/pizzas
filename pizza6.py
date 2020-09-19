from validation_functions import get_integer, get_string, get_single_entry, get_single_entry_two_option, get_phone_string
from test_files import test_one, repeated_zero_list


def print_pizza_menu(P):
    for i in range(0, len(P)):
        row_string = "{:<5}{:20}${:<10.2f}".format(i,P[i][0], P[i][1])
        print(row_string)
    print("-"*30)


def get_the_customer_details():
    """ no parameters
    gets customer details
    returns a dictionary"""
    print("Getting customer details")
    customer_details={}
    delivery = get_single_entry_two_option("(P)ickup or (D)elivery?   ", "P", "D")
    if delivery == "P":
        print("Get full information")
        name_string = get_string("Please enter customer name :  ", 20)
        address_one_string = get_string("Please enter address line 1: ",30)
        address_two_string = get_string("Please enter address line 1: ", 30)
        phone = get_phone_string("Please enter phone number: ")
        customer_details["Name"]=name_string
        customer_details["Address1"] = address_one_string
        customer_details["Address2"] = address_two_string
        customer_details["Phone"] = phone
    elif delivery == "D":
        print("Get name and phone")
        name_string = get_string("Please enter customer name :  ", 20)
        phone = get_phone_string("Please enter phone number: ")
        customer_details["Name"]=name_string
        customer_details["Phone"] = phone
    else:
        print("Error in getting P or D")
    return customer_details


def run_options_menu(PIZZA_LIST, order_list, show_pizza_menu):
    options=[
        ["A", "Add pizza"],
        ["R", "Review order"],
        ["M", "Show/hide when adding pizzas "],
        ["D", "Delete order and start new order"],
        ["E", "Edit Order"],
        ["C", "Confirm and action order"],
        ["Q", "Quit"]
    ]
    for i in range(0, len(options)):
        row_string = "{:5}{:15}".format(options[i][0], options[i][1])
        print(row_string)
    print("-" * 30)
    choice = get_single_entry("Please choose a option:   ")
    print("-" * 30)
    if choice == "A":
        add_pizza(PIZZA_LIST, order_list, show_pizza_menu)
        print("-" * 30)
        return None
    elif choice == "R":
        print_order(order_list)
        print("-" * 30)
        return None
    elif choice == "M":
        return "M"
    elif choice == "D":
        return "D"
    elif choice == "E":
        edit_order(order_list)
        return None
    elif choice == "C":
        return confirm_and_close_order(order_list)
    elif choice == "Q":
        return "Q"
    else:
        print("You have not chosen a valid option")
        return None


def add_pizza(P,order_list, s):
    if s:
        print_pizza_menu(P)
    choice = get_integer("Please choose a option:   ", 0, len(P))
    amount_string = "How many {} would you like?  ".format(P[choice][0])
    amount = get_integer(amount_string,0,10)
    order = [P[choice][0], P[choice][1], amount]
    order_list.append(order)
    confirmation_message = "{} {} have been added to the order ".format(amount, P[choice][0])
    print(confirmation_message)
    return None



def clean_up_order_list(O):
    remove_zero_orders(O)
    i = 0
    while i < len(O):
        temp = O[i][0]
        j= i+1
        while j < len(O):
            #print(O)
            #print("{},{}".format(i,j))
            if O[j][0] == temp:
                #print("{}={}".format(temp,O[j][0]))
                O[i][2] += O[j][2]
                del O[j]
                j -= 1
            j+=1
        i += 1


def remove_zero_orders(O):
    i = 0
    while i < len(O):
        if O[i][2] == 0:
            del O[i]
            i -= 1
        i += 1

def edit_order(O):
    header = "{:^20}{:^20}{:^20}".format("Option Number","Item", "Quantity")
    print(header)
    for i in range(0, len(O)):
        row = "{:^20}{:^20}{:^20}".format(i,O[i][0], O[i][2])
        print(row)
    print("-"*30)
    choice = get_integer("Please select option to edit:  ", 0, len(O)-1)
    my_string = "Please update number of {} pizza:  ".format(O[choice][0])
    new_number = get_integer(my_string, 0, 10)
    O[choice][2]=new_number
    print("Current order status")
    print_order(O)
    return None


def print_order(O):
    print("*"*50)
    total = 0
    for i in range(0, len(O)):
        # 3 Hawaiian at price sub total
        sub_total = O[i][1]*O[i][2]
        total += sub_total
        my_string = "{:^5}{:<20}@ ${:<8.2f}${:<8.2f}".format(O[i][2], O[i][0], O[i][1], sub_total)
        print(my_string)
    my_string = "{:36}${:<8.2f}".format("", total)
    print(my_string)
    print("*" * 50)

def confirm_and_close_order(O):
    print_order(O)
    x=get_single_entry("Press C to confirm order or any other key to continue  ")
    if x == "C":
        print("Thankyou order has now been finalised")
        return "C"
    else:
        return None



def main():
    PIZZA_LIST = [("Vegetarian", 8.5), ("Pepperoni", 8.5), ("Hawaiian", 8.5),
                  ("Artichoke Special", 13.5), ("Supreme", 13.5)]
    # each element of the list is also a list with 3 items.
    # pizza name, pizza price, quantity of pizza
    order_list_map = ["name", "price", "qunatity"]
    order_list = []
    order_list = test_one()
    order_list = repeated_zero_list()
    clean_up_order_list(order_list)
    customer_details_dict = {}
    show_pizza_menu = True
    get_customer_details = False
    previous_orders=[]
    while True:
        if get_customer_details:
            customer_details_dict= get_the_customer_details()
            print(customer_details_dict)
            for x,y in customer_details_dict.items():
                print(x,y)
            get_customer_details = False
        x = run_options_menu(PIZZA_LIST, order_list ,show_pizza_menu)
        if x == "Q":
            break
        elif x == "M":
            if show_pizza_menu == True:
                show_pizza_menu = False
            else:
                show_pizza_menu = True
        elif x == "D":
            customer_details_dict= {}
            order_list = []
            get_customer_details = True
        elif x == "C":
            new_dictionary= {}
            new_dictionary["Customer"] = customer_details_dict
            new_dictionary["Order"] = order_list
            previous_orders.append(new_dictionary)
            customer_details_dict = {}
            order_list = []
            get_customer_details = True
            #print(get_customer_details)



if __name__ == "__main__":
    main()
