
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
    """ message, maximum number of characters returns acceptable string """
    cont = "y"
    while cont is "y":
        response_string = input(m)
        if len(response_string) <4:
            print("No proper value has been entered")
            continue
        elif len(response_string) > max:
            print("Too many characters for a fruit name")
            continue
        else:
            return response_string

def get_single_entry(m):
    cont = "y"
    while cont is "y":
        response_string = input(m).strip().upper()
        if len(response_string) != 1:
            print("Please enter only one character")
        else:
            return response_string


def get_single_entry_two_option(m, op1, op2):
    cont = "y"
    while cont is "y":
        choice = get_single_entry(m)
        if choice!= op1 and choice != op2:
            print("please choose either {} or {}".format(op1, op2))
        else:
            return choice

def get_phone_string(m):
    cont = "y"
    while cont is "y":
        phone = get_string(m,16)
        for i in "- *":
            phone= phone.replace(i, "")
        if phone.isdigit():
            #print(phone)
            return phone
        else:
            print("please enter phone number again")

if __name__ == "__main__":
    p = "02*****11-2-   4   5  6  78"
    get_phone_string("Phone")

