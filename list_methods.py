

board = [['B', 'B', 'B', ' '],['B', 'B', 'B', 'B'],['B', 'B', 'B', 'B']]
#print( any(' ' in b for b in board) )

#print( any(' ' in b for b in board[1:]) )

my_list = ["A", "B", "C", "D", "A", "A", "B", "C"]

#remove each even item
def remove_each_even(my_list):
    temp =[]
    for i in range(1, len(my_list),2):
        print(i)
        print(my_list[i])
        temp.append(my_list[i])
    my_list =temp

i = 0
while i < len(my_list):
    temp = my_list[i]
    j= i+1
    while j < len(my_list):
        if my_list[j] == temp:
            print(my_list[j])
            del my_list[j]
            j -= 1
        j+=1
    i += 1

print(my_list)

my_pizza_list=[['Vegetarian', 8.5, 3],
            ['Artichoke Special', 13.5, 2],
            ['Vegetarian', 8.5, 3],
            ['Artichoke Special', 13.5, 2],
            ['Artichoke Special', 13.5, 0]
            ]


def clean_up_order_list(O):
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
print(my_pizza_list)
remove_zero_orders(my_pizza_list)
print(my_pizza_list)
clean_up_order_list(my_pizza_list)
print(my_pizza_list)

