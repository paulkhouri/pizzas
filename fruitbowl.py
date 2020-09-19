fruit_bowl=[
    ["apples", 0],
    ["pears",0],
    ["quinces", 0],
    ["lemons", 0]
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

def get_string(m, max):
    cont = "y"
    while cont is "y":
        response_string = input(m)
        if len(response_string) <4:
            print("No proper fruit name has been entered")
            continue
        elif len(response_string) > max:
            print("Too many characters for a fruit name")
            continue
        else:
            return response_string



def print_fuits_with_options(F):
    for i in range(0,len(F)):
        my_string = "{:<5}{:10}".format(i, F[i][0])
        print(my_string)


def current_fruit_bowl(F):
    print("{:20}{:^20}".format("Fruit","Pieces of:"))
    for i in F:
        my_fruit = "{:20}{:^20}".format(i[0],i[1])
        print(my_fruit)


def get_option(F):
    print("-"*60)
    print("Choose your option")
    options_list = [
        ["A", "Add fruit"],
        ["E", "Eat fruit"],
        ["R", "Review fruit"],
        ["T", "Total fruit"],
        ["N", "New fruit"],
        ["Q", "Quit"]
    ]
    for i in range(0, len(options_list)):
        my_options ="{:3}{:10}".format(options_list[i][0], options_list[i][1])
        print(my_options)
    print("-" * 60)
    option = input("Please choose your option")
    if option == "A":
        add_fruit(F)
        return
    elif option == "E":
        eat_fruit(F)
        return
    elif option == "R":
        current_fruit_bowl(F)
        return
    elif option == "T":
        add_up_fruit(F)
        return
    elif option == "N":
        new_fruit(F)
        return
    elif option == "Q":
        return option
    else:
        print("Not an option")


def add_fruit(F):
    print("-" * 60)
    for i in range(0, len(F)):
        my_string = "{:<5}{:10}".format(i, F[i][0])
        print(my_string)
    print("-" * 60)
    option = get_integer("Choose option number of fruit to add", 0, len(F))
    my_amount = get_integer("How many {} would you like to add?".format(F[option][0]), 0, 10)
    F[option][1]=F[option][1]+my_amount
    response_string = "You now have {} {} in the fruitbowl".format(F[option][1], F[option][0])
    print(response_string)

def eat_fruit(F):
    print("-" * 60)
    for i in range(0, len(F)):
        my_string = "{:<5}{:10}".format(i, F[i][0])
        print(my_string)
    print("-" * 60)
    option = get_integer("Choose option number of fruit to eat", 0, len(F))
    my_amount = get_integer("How many {} would you like to eat?".format(F[option][0]), 0, F[option][1]-95)
    F[option][1]=F[option][1]-my_amount
    response_string = "You now have {} {} in the fruitbowl".format(F[option][1], F[option][0])
    print(response_string)


def add_up_fruit(F):
    total_fruit = 0
    for i in range(0, len(F)):
        total_fruit += total_fruit + F[i][1]
    print("You have {} pieces of fruit in the fruit bowl".format(total_fruit))

def new_fruit(F):
    cont = "y"
    while cont is "y":
        fruit_name = get_string("Please enter the name of your fruit:", 20)
        fruit_amount = get_integer("Please enter how much fruit you have:",0,10)
        print( "You have entered {} with {} pieces".format(fruit_name, fruit_amount) )
        confirm = input("press (y) to confirm, (n) to re-enter again or (e) to exit without changes")
        if confirm == "y":
            F.append([fruit_name, fruit_amount])
            return
        elif confirm == "n":
            continue
        elif confirm == "e":
            return
        else:
            print("not a valid entry")
            continue





cont = "y"
current_fruit_bowl(fruit_bowl)
while cont=="y":
    response = get_option(fruit_bowl)
    if response is "Q":
        cont = "n"


