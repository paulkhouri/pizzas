pizza_list=[("Vegetarian", 8.5),("Pepperoni", 8.5),("Hawaiian", 8.5),
            ("Mushroom", 8.5),("Supreme", 13.5),("Artichoke Special", 13.5)]
pizza_order=[]
for i in range(0, len(pizza_list)):
    temp = []
    temp.append(pizza_list[i][0])
    temp.append(pizza_list[i][1])
    temp.append(3)
    pizza_order.append(temp)
print(pizza_order)


for i in range(0, len(pizza_order)):
    price = pizza_order[i][1]*pizza_order[i][2]
    output= "{:<2}{:<30} ${:<20.2f}".format(pizza_order[i][2],pizza_order[i][0], price)
    print(output)