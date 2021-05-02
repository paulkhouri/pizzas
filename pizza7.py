from validation_functions import get_integer, get_string, get_single_entry, get_single_entry_two_option, get_phone_string
from test_files import test_one, repeated_zero_list


def print_pizza_menu(P):
    """Print row column list of pizzas

    :param P: list (row column)
    :return: None
    """
    for i in range(0, len(P)):
        row_string = "{:<5}{:20}${:<10.2f}".format(i,P[i][0], P[i][1])
        print(row_string)
    print("-"*30)


def get_the_customer_details():
    """Get customer details.

    :return: dict
    """
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
        customer_details["Name"] = name_string
        customer_details["Phone"] = phone
    else:
        print("Error in getting P or D")
    return customer_details

def clean_up_order_list(O):
    """

    :param O: list (row column)
    :return: None
    deprecated function design to remove double orders
    """
    remove_zero_orders(O)
    i = 0
    while i < len(O):
        temp = O[i][0]
        j= i+1
        while j < len(O):
            if O[j][0] == temp:
                O[i][2] += O[j][2]
                del O[j]
                j -= 1
            j+=1
        i += 1


def remove_zero_orders(O):
    """Remove any entries with 0 pizzas

    :param O: list (row column)
    :return: None
    """
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
        # x **** at $****  sub total = $*****
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


# ------------------------------------------------------------------------
def check_name_present(o, n):
    """Check if a name is already in a 

    :param o: order list
    :param n: choice name
    :return: int
    """
    for i in range(0,len(o)):
        if o[i][0]==n:
            message = "{} is already present at index {} 0".format(n,i)
            print(message)
            return i
    return -1

def add_pizza(p, order_list, s,max_):
    """Request option number of pizza and quantity and add it to order list.

    :param P: tuple list (row column)
    :param order_list: list (row coumn)
    :param s: boolean
    :param s: int
    :return: None
    """
    # print menu if s is true
    if s:
        print_pizza_menu(p)
    # get option and quantity
    message = "Please choose a option number from the menu: ->   "
    choice = get_integer(message, 0, len(p))
    choice_name = p[choice][0]
    price = p[choice][1]
    # gets the index number of the choice if it is already in the list
    result = check_name_present(order_list,choice_name)
    if result != -1:
        message = "You already have {} of {} in the order".format(order_list[result][2], p[choice][0])
        print(message)
        message = "You can order at most {} more".format(max_ - order_list[result][2])
        print(message)

    message = "How many {} would you like?  "
    amount_string = message.format(p[choice][0])
    if result != -1:
        amount = get_integer(amount_string, 0, max_ - order_list[result][2])
    else:
        amount = get_integer(amount_string, 0, max_)

    # add to order list
    if result != -1:
        # update existing entry
        order_list[result][2] += amount
    else:
        # add new entry
        order = [choice_name, price, amount]
        order_list.append(order)
    message = "{} {} have been added to the order "
    confirmation_message = message.format(amount, p[choice][0])
    print(confirmation_message)
    return None

# ------------------------------------------------------------------------


def run_options_menu(PIZZA_LIST, order_list, show_pizza_menu, max_):
    options=[
        ["P", "Print Menu"],
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
    if choice == "P":
        print_pizza_menu(PIZZA_LIST)
    elif choice == "A":
        add_pizza(PIZZA_LIST, order_list, show_pizza_menu, max_)
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

def main():
    regular_price = 18.5
    gourmet_price = regular_price + 7
    maximum_individual_pizza = 5
    PIZZA_LIST = [("Vegetarian", regular_price),
                  ("Pepperoni", regular_price),
                  ("Hawaiian", regular_price),
                  ("Artichoke Special", gourmet_price),
                  ("Supreme", gourmet_price)]
    # each element of the list is also a list with 3 items.
    # pizza name, pizza price, quantity of pizza
    order_list_map = ["name", "price", "quantity"]
    order_list = []
    #order_list = test_one()
    #order_list = repeated_zero_list()
    #clean_up_order_list(order_list)
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
        x = run_options_menu(PIZZA_LIST, order_list ,show_pizza_menu, maximum_individual_pizza)
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
