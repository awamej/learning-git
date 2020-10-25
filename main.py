print("zadanie")
num_list = [2, 0, 0, 0, 1, 0, 0, 0, 0, 0, 2, 3, 0, 0]
new_list1 = num_list[1:4] + num_list[5:10] + num_list[-2:]
print(new_list1)
new_list2 = list([num_list[0]]) + list([num_list[4]]) + num_list[-4:-2]
print(new_list2)
# sprawdzenie
check = new_list1 + new_list2
print("Sprawdzenie: " + str(bool(sorted(num_list) == sorted(check))))
