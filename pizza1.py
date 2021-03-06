pizza_list=[("Vegetarian", 8.5),("Pepperoni", 8.5),("Hawaiian", 8.5),
            ("Mushroom", 8.5),("Supreme", 13.5),("Artichoke Special", 13.5)]
order_quantities=[]
order_total=0
customer_information=[]


def init_method():
    global order_quantities
    for i in range (0,len(pizza_list)):
        order_quantities.append(0)


def get_string_input(m):
    txt = input(m)
    return txt


def get_integer_input(m):
    txt = input(m)
    try:
        myInt=int(txt)
    except ValueError:
        print("not an integer")
    return myInt

def my_print(m):
    print("---------------------------")
    print(m)
    print("---------------------------")


def print_menu(L):
    for i in range (0,len(L)):
        print("{}. {} @ ${:.2f}".format(i+1,L[i][0],L[i][1]))


def checkout(L):
    global order_total
    for i in range(0, len(order_quantities)):
        if order_quantities[i] != 0:
            print("{} {} pizzas @ ${}".format(order_quantities[i],L[i][0],L[i][1]))
            order_total += order_quantities[i]*L[i][1]
    print("Total price: ${}".format(order_total))
    print("Customer information")
    for i in range(0, len(customer_information)):
        print("{}".format(customer_information[i]))


def main():
    init_method()
    global customer_information
    #name=get_string_input("Please enter customer name: ")
    #phone = get_string_input("Please enter phone number: ")
    name = "Mary"
    customer_information.append(name)
    my_print("Order for {} ".format(name))
    cont = "y"
    while cont == "y":
        print_menu(pizza_list)
        my_pizza=get_integer_input("Enter the pizza number: ")
        my_pizza = my_pizza-1
        quantity = get_integer_input("How many {} pizza(s) ? ".format(pizza_list[my_pizza][0]))
        order_quantities[my_pizza] += quantity
        cont = get_string_input("Would you like to order further pizzas y/n ")
    checkout(pizza_list)


if __name__ == '__main__':
    main()

