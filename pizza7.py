from validations_pizza import get_integer, get_string, get_single_entry, \
    get_phone_string, get_entry_option_list, confirmation
from test_files import test_one

# ---------------------------------------------------


def print_line():
    """Print dashed line of set length

    :return: None
    """
    print("-" * 30)


def print_pizza_menu(p):
    """Print row column list of pizzas

    :param p: list (row column)
    :return: None
    """
    for i in range(0, len(p)):
        row_string = "{:<5}{:20}${:<10.2f}".format(i, p[i][0], p[i][1])
        print(row_string)
    print_line()


def print_details(c):
    """Print formatted information from the customer order dictionary

    :param c: list (row column)
    :return: None
    """
    print("The current customer details loaded are: ")
    for x, y in c.items():
        print("{:<13} : {:20}".format(x, y))
    print_line()


def print_order(o, e):
    """Print out the current pizza order

    :param o: list (row column) of the the current customer order
    :param e: integer greater than 0
    :return: None
    """
    print("*"*50)
    total = 0
    for i in range(0, len(o)):
        # x **** at $****  sub total = $*****
        sub_total = o[i][1]*o[i][2]
        total += sub_total
        # Quantity , Pizza , Cost , subtotal
        my_string = "{:^5}{:<20}@ ${:<8.2f}${:<8.2f}".format(o[i][2], o[i][0], o[i][1], sub_total)
        print(my_string)
    if e != 0:
        my_string = "{:^5}{:<20}@ ${:<8.2f}${:<8.2f}".format(1, "Extras", e, e)
        total += e
        print(my_string)

    my_string = "{:36}${:<8.2f}".format("", total)
    print(my_string)
    print("*" * 50)

# -----------------------main menu functions----------------------------


def get_the_customer_details(c):
    """Get customer details.

    :param c: dictionary
    :return: dictionary
    """
    print("Getting customer details")
    if c:
        print_details(c)
        message = "Would you like to overwrite these details? Y/N: "
        choice = get_entry_option_list(message, ["Y", "N"])

        if choice == "N":
            print("Returning to main menu")
            return None
        else:
            # clear dictionary before adding new details
            # avoids problem is customer changes from delivery to pick-up
            c.clear()
    while True:
        delivery = get_entry_option_list("(P)ickup or (D)elivery?   ", ["P", "D"])
        if delivery == "D":
            print("Get full information")
            name_string = get_string("Please enter customer name :  ", 20).title()
            address_one_string = get_string("Please enter address line 1: ", 30).title()
            address_two_string = get_string("Please enter address line 1: ", 30).title()
            phone = get_phone_string()
            c["Name"] = name_string
            c["Address_1"] = address_one_string
            c["Address_2"] = address_two_string
            c["Phone"] = phone
        elif delivery == "P":
            print("Get name and phone")
            name_string = get_string("Please enter customer name :  ", 20).title()
            phone = get_phone_string()
            c["Name"] = name_string
            c["Phone"] = phone
        else:
            print("Error in getting P or D")

        print_details(c)
        message = "Would you like to confirm these details? Y/N: "
        choice = get_entry_option_list(message, ["Y", "N"])
        print_line()
        if choice == "Y":
            print("Order details updated")
            print_line()
            if delivery == "D":
                return 3
            else:
                return 0
        else:
            # clear dictionary if we need to start again
            c.clear()


def confirm_and_close_order(o, c, p, e):
    """Confirm that order is to be finalised. Store the data and clear the list/dictionary

    :param o: list (row column) of the the current customer order
    :param c: dictionary containing information about the customer
    :param p: list containing information about previous orders
    :param e: integer greater than 0
    :return: None
    """
    print("-" * 30)
    # check for incomplete data
    if c is False and o is False:
        print("There is no order data")
        print("-" * 30)
        return None
    elif not c:
        print("Order details incomplete (no customer information) ")
        print("Returning to main menu")
        print("-" * 30)
    elif not o:
        print("Order details incomplete (no pizzas have been ordered")
        print("Returning to main menu")
        print("-" * 30)
    # all data present
    else:
        print_order(o, e)
        print_details(c)
        if confirmation("Do you want to finalise the order: Y/N  -> "):
            # save the current order
            new_dictionary = {"Customer": c, "Order": o}
            p.append(new_dictionary)
            # reset customer details and order list to empty
            c.clear()
            o.clear()
            return True
        else:
            print("Order is still current")
            return False


def edit_order(o, e):
    """Remove any entries with 0 pizzas

    :param o: list (row column) of the the current customer order
    :param e: integer greater than 0
    :return: None
    """
    # used for last option given allows user to exit function quickly
    exit_num = 0
    for i in range(0, len(o) + 1):
        if i < len(o):
            row = "{:<5}{:20}#{:<10}".format(i, o[i][0], o[i][2])
            print(row)
        else:
            exit_num = i
            exit_option = "{:<5}{:20}".format(len(o), "Return to main menu -- Not Required -- ")
            print("-" * 30)
            print(exit_option)
    print("-"*30)
    choice = get_integer("Please choose an option:  ", 0, len(o)-1+1)
    if choice == exit_num:
        print("Returning to main menu")
        return None
    my_string = "Please update number of {} pizza: (Enter 0 to delete pizza)  ".format(o[choice][0])
    new_number = get_integer(my_string, 0, 5)
    if new_number == 0:
        temp = o.pop(choice)
        output = "All {} have been removed ".format(temp[0])
        print(output)
    else:
        o[choice][2] = new_number
    print("Current order status")
    print_order(o, e)
    return None


def check_name_present(o, n):
    """Check if a name is already in the pizza list

    :param o: order list
    :param n: choice name
    :return: int
    """
    for i in range(0, len(o)):
        if o[i][0] == n:
            message = "Test Message: {} is already present at index {}".format(n, i)
            print(message)
            return i
    return -1


def add_pizza(p, order_list, s, max_):
    """Add a pizza to the customer order

    :param p: 2D list of pizzas and prices
    :param order_list: 2D list to hold customer pizza order
    :param s: boolean to display pizza menu or not
    :param max_: integer for maximum number of a particular pizza
    :return: None
    """
    if s:
        print_pizza_menu(p)
    exit_option = "{:<5}{:20}".format(len(p), "Return to main menu -- Not Required -- ")
    print(exit_option)
    print("-" * 30)

    # get option and quantity
    message = "Please choose an option: ->   "
    choice = get_integer(message, 0, len(p))
    # quick escape option
    if choice == len(p):
        print("Returning to main menu")
        return None
    #
    pizza_name = p[choice][0]
    price = p[choice][1]
    # gets the index number of the choice if it is already in the list
    result = check_name_present(order_list, pizza_name)
    # feedback to user if they already have an entry for this pizza
    if result != -1:
        message = "You already have {} of {} in the order".format(order_list[result][2], pizza_name)
        print(message)
        message = "You can order at most {} more".format(max_ - order_list[result][2])
        print(message)

    message = "How many {} would you like, in total?  "
    amount_string = message.format(pizza_name)
    if result != -1:
        amount = get_integer(amount_string, 0, max_ - order_list[result][2])
        # update existing entry
        order_list[result][2] += amount
        confirmation_message = "{} {} have been added to the order => " \
                               "There are now {} {} " \
                               "pizzas".format(amount, pizza_name, order_list[result][2], order_list[result][0])
    else:
        # create and append new list entry
        amount = get_integer(amount_string, 0, max_)
        if amount != 0:
            order = [pizza_name, price, amount]
            order_list.append(order)
            confirmation_message = "{} {} have been added to the order".format(amount, p[choice][0])
        else:
            confirmation_message = "You have entered 0 so no pizzas have been added"

    print(confirmation_message)
    return None

# ------------------------------------------------------------------------


def main():
    """Start program.
    :return: None
    """
    options = [
        ["P", "Print Menu"],
        ["A", "Add pizza"],
        ["R", "Review order"],
        ["M", "Show/hide when adding pizzas "],
        ["D", "Delete order and start new order"],
        ["E", "Edit Order"],
        ["G", "Customer Order Details (Pick-up/Delivery)"],
        ["C", "Confirm and action order"],
        ["Q", "Quit"]
    ]

    # main program variables
    regular_price = 18.5
    gourmet_price = regular_price + 7
    maximum_individual_pizza = 5
    extra_costs = 0
    pizza_list = [("Vegetarian", regular_price),
                  ("Pepperoni", regular_price),
                  ("Hawaiian", regular_price),
                  ("Artichoke Special", gourmet_price),
                  ("Supreme", gourmet_price)]
    # each element of the list is also a list with 3 items.
    # pizza name, pizza price, quantity of pizza
    order_list = test_one()

    customer_details_dict = {}
    show_pizza_menu = True
    starting_new_order = True
    previous_orders = []

    # -- start main program loop
    while True:
        if starting_new_order:
            print("-"*20)
            print("Starting new order")
            extra_costs = 0
            starting_new_order = False

        for i in range(0, len(options)):
            row_string = "{:5}{:15}".format(options[i][0], options[i][1])
            print(row_string)
        # run main options menu

        print("-" * 30)
        choice = get_single_entry("Please choose an option:   ")
        print("-" * 30)
        if choice == "P":
            print_pizza_menu(pizza_list)
        elif choice == "A":
            add_pizza(pizza_list, order_list, show_pizza_menu, maximum_individual_pizza)
            print("-" * 30)
        elif choice == "R":
            print_order(order_list, extra_costs)
            print("-" * 30)
        elif choice == "M":
            if show_pizza_menu is True:
                print("Pizza Menu will not appear")
                show_pizza_menu = False
            else:
                print("Pizza Menu will appear")
                show_pizza_menu = True
        elif choice == "D":
            if customer_details_dict is False and order_list is False:
                print("The is no order data")
            elif confirmation():
                customer_details_dict = {}
                order_list = []
                starting_new_order = True
            else:
                print("The order has not been deleted")
        elif choice == "E":
            edit_order(order_list, extra_costs)
        elif choice == "G":
            extra_costs = get_the_customer_details(customer_details_dict)
        elif choice == "C":
            if confirm_and_close_order(order_list, customer_details_dict, previous_orders, extra_costs):
                starting_new_order = True
        elif choice == "Q":
            print("Quitting")
            break

        else:
            print("You have not chosen a valid option")


if __name__ == "__main__":
    main()
