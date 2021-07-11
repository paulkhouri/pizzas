
def id_test():
    my_num_one=100
    my_num_two=100
    print("my_num_one id is: {}".format(id(my_num_one)))
    print("my_num_two id is: {}".format(id(my_num_two)))
    print(my_num_one is my_num_two)
    print(my_num_one == my_num_two)



    my_list_one = ["Mary", "James"]
    my_list_two = ["Mary", "James"]
    #my_list_two = my_list_one
    print("my_list_one id is: {}".format(id(my_list_one)))
    print("my_list_two id is: {}".format(id(my_list_two)))
    my_list_one.clear()
    print("my_list_one id is: {}".format(id(my_list_one)))



    print(my_list_one is my_list_two)
    print(my_list_one == my_list_two)

def list_tests():
    list_one_d = ["harry", "megan", "william", "kate", "george"]
    print(id(list_one_d))
    print(list_one_d)
    list_one_d.remove("megan")
    print(list_one_d)
    del list_one_d[0]
    print(list_one_d)
    list_one_d.pop(0)
    print(list_one_d)
    print(id(list_one_d))

def list_test_length():
    my_list=[["Hawaiian", 2, 18.00], ["pepperone", 3, 23.00], ["cheese", 3, 23.00]]
    print(my_list[2])
    popped = my_list.pop(2)
    print(popped)

def assignment_test():
    test_var = None
    if test_var:
        print("something here")
    else:
        print("nothing")


def id_extra():
    num_ = 0
    print(id(num_))
    num_ = 1
    print(id(num_))
    num_ = 0
    print(id(num_))
    print()
    num_ = ["abc", "a"]
    print(id(num_))
    #num_ = 273684
    #print(id(num_))
    pum_ = ["abc", "a"]
    print(id(pum_))

def addition(total,b):
    total = total + b
    print(total)
    return total



def test_param_length(a,b=0):
    print(a)
    print(b)


def main_function():
    total = 10
    print(total)
    total = addition(total, 20)
    print(total)


def var_test():
    my_string = "H"
    x=my_string.replace("H", "A")
    print(id(my_string))
    print(id(x))

def check_structures():
    my_d = {}
    my_l = []
    print(my_d is True, my_l is True)










if __name__ == "__main__":
    check_structures()
    #var_test()
    #test_param_length(2,5)
    #main_function()
    #assignment_test()
    #list_test_length()
    #id_extra()
    #list_tests()
    #id_test()