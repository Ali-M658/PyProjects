
import numpy as np
import math

switch_1 = int(input('Enter elements in 1st number: '))

switch_2 = int(input('Enter elements in 2nd number: '))

element = int(input('How many elements in the magnitude? '))

tuplenumb = input('Enter 1st set 0f numbers with comma: ')

tuplenumb2 = input('Enter 2nd set of numbers with comma: ')

magnitude = input('Enter the magnitude: ')



sw1list = []
sw2list = []
maglist = []

tuplenumb = tuple(tuplenumb.split(','))
tuplenumb2 = tuple(tuplenumb2.split(','))
magnitude = tuple(magnitude.split(','))

for i in range (0, switch_1):
    sw1list.append(0)

for j in range (0, switch_2):
    sw2list.append(0)

for k in range (0, element):
    maglist.append(0)

sw1list = tuplenumb
sw2list = tuplenumb2
maglist = magnitude

converted_list = [int(num) for num in tuplenumb]
converted_list2 = [int(nu) for nu in tuplenumb2]
converted_list3 = [int(nums) for nums in magnitude]

real_conv = [item for item in converted_list for _ in range(len(converted_list3))]
real_conv2 = [item for item in converted_list2 for _ in range(len(converted_list3))]
real_conv = np.array(real_conv) - np.array(converted_list3*len(converted_list))
real_conv2 = np.array(real_conv2) + np.array(converted_list3*len(converted_list2))

def sum_groups(real_conv, num_elements):
    group_size = len(real_conv) / num_elements
    rounded_group_size = math.ceil(group_size)
    return [sum(real_conv[i:i+rounded_group_size]) for i in range(0, len(real_conv), rounded_group_size)]

num_elements = len(converted_list3)
new_list = sum_groups(real_conv, num_elements)
print(new_list)

def sum_groups1(real_conv2, num_elements1):
    group_size1 = len(real_conv2) / num_elements1
    rounded_group_size1 = math.ceil(group_size1)
    return [sum(real_conv2[i:i+rounded_group_size1]) for i in range(0, len(real_conv2), rounded_group_size1)]


num_elements1 = len(converted_list3)
new_list1 = sum_groups(real_conv2, num_elements1)
print(new_list1)

solution = tuple(x-y for x, y in zip(converted_list, converted_list3))
solution1 = tuple(x+y for x, y in zip(converted_list2, converted_list3))
