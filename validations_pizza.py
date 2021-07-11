
def get_integer(m, min,max):
    """ message, minimum and maximum returns acceptable integer """
    cont = True
    while cont is True:
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
    cont = True
    while cont is True:
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
    cont = True
    while cont is True:
        response_string = input(m).strip().upper()
        if len(response_string) != 1:
            print("Please enter only one character")
        else:
            return response_string


def get_entry_option_list(m, L, u=True):
    cont = True
    while cont is True:
        choice = input(m)
        if u:
            choice = choice.upper()
        if choice not in L:
            print("Please choose from these options: {}".format(L))
        else:
            return choice


def confirmation(m="Please confirm: Y/N: -> "):
    c = ["Y","N"]
    while True:
        choice = input(m).upper()
        if choice not in c:
            print("Please choose from these options: {}".format(c))
        elif choice == "Y":
            return True
        else:
            return False

def get_phone_string():
    cont = True
    while cont is True:
        phone = input("Please enter phone number (NZ or international mobile, or Wellington landline) : ")
        phone_text = ""
        c = 0
        digit_count = 0
        spaces= [3,7]
        for i in phone:
            if i.isdigit():
                digit_count =+ 1
                c += 1
                phone_text += i
            elif digit_count == 0 and i == "+":
                phone_text += i
            if c in spaces:
                c += 1
                phone_text += " "
        if len(phone_text)>10 and len(phone_text)<15 :
            if phone_text[0:3] in ["021", "022", "021"] or phone_text[0] in ["+","4"]:
                message="The phone number you have entered is {}".format(phone_text)
                print(message)
            else:
                print("Oops, this doesn't look quite right, problem with the prefix")
                continue
            choice = get_entry_option_list("Please confirm Y/N: -> ", ["Y","N"])
            if choice == "Y":
                print("Phone number accepted")
                return phone_text
        else:
            print("Oops, this doesn't look quite right, phone number length not valid")

# testing
if __name__ == "__main__":
    p = "02*****11-2-   4   5  6  78"

    #get_phone_string()
    #get_entry_option_list("Please choose: -> ", ["Y","N"])
    confirmation()

