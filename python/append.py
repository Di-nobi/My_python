my_list = []
list_1 = [1, 2, 3]
list_2 = [4, 5, 6]
list_3 = [7, 8, 9]
my_list.extend([list_1]  + [list_2] + [list_3])
for i in my_list:
    print("{}".format(i))
