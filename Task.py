def sort_list_imperative(numbers: list) -> list:
    for i in range(len(numbers)):
        max = i
        for j in range(i, len(numbers)):
            if numbers[j] > numbers[max]:
                max = j
        temp = numbers[i]
        numbers[i] = numbers[max]
        numbers[max] = temp
    return numbers

def sort_list_declarative(numbers: list) -> list:
    numbers.sort(reverse= True)
    return numbers



list1 = [1, 4, 2, 5, 3, 10, 1, 7, 10]
list2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
list3 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(sort_list_imperative(list1))
print(sort_list_imperative(list2))
print(sort_list_imperative(list3))
print()

list1 = [1, 4, 2, 5, 3, 10, 1, 7, 10]
list2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
list3 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


print(sort_list_declarative(list1))
print(sort_list_declarative(list2))
print(sort_list_declarative(list3))