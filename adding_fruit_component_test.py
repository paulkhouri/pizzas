amy_fruit_bowl = [
        ["Apples", 5],
        ["Pears", 7],
        ["Mangoes", 2],
        ["Kiwi Fruit", 9],
        ["Peasches", 3]
        ]

def get_integer(m, min,max):
    """ message, minimum and maximum returns acceptable integer """
    cont = "y"
    while cont is "y":
        try:
            my_integer = int(input(m))
        except ValueError:
            print("please enter an integer value")
            continue
        if my_integer < min:
            print("The value you have entered is too low")
            continue
        elif my_integer > max:
            print("The value you have entered is too high")
            continue
        return my_integer

def add_fruit(L):
    """print list with item numbers
      get user quantity and add to list
      Argument:
      L -- 2 dimensional list  m x [string, integer]
      """
    header ="{:^12}{:30}{:2}".format("Item #", "Fruit", "Quantity")
    print(header)
    for i in range(0,len(L)):
        row = "{:^12}{:30}{:2}".format(i, L[i][0], L[i][1])
        print(row)
    message = "Please choose an item number to add fruit to?   "
    user_choice = get_integer(message, 0, len(L)-1)
    message = "How many {} would you like to add? (maximum is 10)   ".format(L[user_choice][0])
    user_number = get_integer(message, 1, 10)
    L[user_choice][1] += user_number
    confirmation_message = "You now have {} {} in the fruit bowl".format(L[user_choice][1], L[user_choice][0])
    print(confirmation_message)


def print_fruit(L):
    for i in range(0,len(L)):
        row = "{:^12}{:30}{:2}".format(i, L[i][0], L[i][1])
        print(row)

add_fruit(amy_fruit_bowl)
print_fruit(amy_fruit_bowl)
