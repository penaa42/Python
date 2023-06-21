def countdown (num):
    new_list = []
    for num in range(num, -1, -1):
        new_list.append(num)
    return new_list
print(countdown(6))


def print_and_return(any_list):
    print(any_list[0])
    return any_list[1]
print_and_return([1,2])


def first_plus_length(any_list):
    list_sum = 0
    list_sum = list_sum + any_list[0] + len(any_list)
    return list_sum
print(first_plus_length([1,2,3,4,5]))


def values_greater_than_second(any_list):
    new_list = []
    counter = 0
    if len(any_list) < 2:
        return False
    for num in any_list:
        if num > any_list[1]:
            new_list.append(num)
            counter += 1    
    print(counter)
    return new_list
print(values_greater_than_second([5,2,3,2,1,4]))
print(values_greater_than_second([3]))


def length_and_value(size, value):
    new_list = []
    for num in range(size):
        new_list.append(value)
    return new_list
print(length_and_value(4,7))