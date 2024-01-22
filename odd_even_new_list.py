# Given two list of numbers, write a program to create a new list such that the new list should contain odd numbers 
# from the first list and even numbers from the second list.

# pseudo code

# create 2 lists and a placeholder for the new lists
list_1 = [10, 20, 25, 30, 35]
list_2 = [40, 45, 60, 75, 90]
new_list = []
# use for i to get the odd numbers from the first list
for i in list_1:
    if int(i) % 2 != 0:
        # append it to the new list
        new_list.append(i)

# use for i to get the even numbers from the second list
for i in list_2:
    if int(i) % 2 == 0:
        # append it to the new list
        new_list.append(i)
# print the new list
print(f"Your new list now contains the following: ",new_list)
