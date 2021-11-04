def my_func(x, y, z):
    list1 = [x, y, z]
    total = []
    max_1 = max(list1)
    total.append(max_1)
    list1.remove(max_1)
    max_2 = max(list1)
    total.append(max_2)
    print(sum(total))
my_func(-68, 44, 102)