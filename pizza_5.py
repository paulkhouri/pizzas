pizza_list = [("Vegetarian", 8.5), ("Pepperoni", 8.5), ("Hawaiian", 8.5),
             ("Artichoke Special", 13.5), ("Supreme", 13.5)]
order_quantities = []
order_total = 0
customer_information = []
delivery = False
delivery_charge = 3


def init_method():
    global order_quantities
    global order_total
    global delivery
    delivery = False
    order_total = 0
    for i in range(0, len(pizza_list)):
        order_quantities.append(0)


def get_string_input(m,a,b):
    cont = "y"
    while cont == "y":
        txt = input(m)
        if len(txt) < a:
            print("You have not entered sufficient characters")
        elif len(txt)>b:
            print("You entered too many characters")
        else:
            return txt


def get_single_input(m):
    txt = input(m)
    return txt[0]


def get_integer_input(m):
    txt = input(m)
    try:
        my_int = int(txt)
    except ValueError:
        print("not an integer")
    return my_int


def my_print(m):
    print("---------------------------")
    print(m)
    print("---------------------------")


def print_menu(l):
    for i in range(0, len(l)):
        print("{}.{:17} \t @ ${:.2f}".format(i+1, l[i][0], l[i][1]).expandtabs(1))


def manage_order():
    global order_quantities
    cont = "y"
    while cont == "y" or cont == "r":
        print("--------------------")
        print_menu(pizza_list)
        print("--------------------")
        my_pizza = get_integer_input("Enter the pizza number: ")
        print("--------------------")
        my_pizza = my_pizza - 1
        quantity = get_integer_input("How many {} pizza(s) ? ".format(pizza_list[my_pizza][0]))
        order_quantities[my_pizza] += quantity
        print("--------------------")
        cont = get_string_input("(y) order more, (n) finish order, (r) review order", 1, 1)
        if cont =="r":
            cont = review_order(pizza_list)

def review_order(L):
    print("Current order status:")
    print("-"*30)
    global order_total
    order_total = 0
    cont = "y"
    while cont is "y":
        if len(order_quantities) != 0:
            for i in range(0, len(order_quantities)):
                if order_quantities[i] != 0:
                    print("Index:{}\t {} {:20}\t${:6.2f}".format(i,order_quantities[i], L[i][0], L[i][1]).expandtabs(4))
                    order_total += order_quantities[i] * L[i][1]
            if delivery:
                print("\t{:20}\t${:6.2f}".format("Delivery: ", delivery_charge))
            print("\t{} {:^20} \t${:6.2f}".format(" ", "Total price:", order_total).expandtabs(4))
        cont = get_string_input("do you want to do something?",1,1)
    # enter index if needs amendment
    # enter k for continuing with the current order.






def checkout(L):
    global order_total
    order_total = 0
    print("*****************************************")
    for i in range(0, len(order_quantities)):
        if order_quantities[i] != 0:
            print("{} {:20}\t${:6.2f}".format(order_quantities[i],L[i][0],L[i][1]).expandtabs(4))
            order_total += order_quantities[i]*L[i][1]
    if delivery:
        print("{:20}\t${:6.2f}".format("Delivery: ", delivery_charge))
    print("{} {:^20} \t${:6.2f}".format(" ", "Total price:", order_total).expandtabs(4))
    print("-----------------------")
    print("Customer information:")
    print("      ---------       ")
    for i in range(0, len(customer_information)):
        print("{}".format(customer_information[i]))
        print("      ---------       ")
    print("*****************************************")


def get_pick_up_details():
    global customer_information
    name = get_string_input("Please enter customer name: ", 2, 50)
    phone = get_string_input("Please enter phone number: ", 7, 9)
    customer_information.append(name)
    customer_information.append(phone)


def get_full_details():
    global customer_information
    get_pick_up_details()
    address = get_string_input("Please enter address: ", 2, 50)
    customer_information.append(address)
    global order_total
    order_total += 3


def start_order():
    global customer_information
    global delivery
    d = get_string_input("Is this a (d)elivery or (p)ickup ?  ", 1, 1)
    if d == "d":
        get_full_details()
        delivery = True
    elif d == "p":
        get_pick_up_details()
    else:
        print("error with delivery and pick up")


def start_test():
    global customer_information
    global order_total
    global delivery
    delivery = True
    customer_information.append("Paul")
    customer_information.append("021879123")
    customer_information.append("88 Nowhere Place")
    order_total += 3


def main():
    init_method()
    #start_order()
    start_test()
    my_print("Order for {} ".format(customer_information[0]))
    manage_order()
    checkout(pizza_list)


if __name__ == '__main__':
    main()
