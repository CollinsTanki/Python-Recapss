# Append add a number at the end of a list
numbers = [5, 2, 1, 7, 4]
numbers.append(20)
print(numbers)

# Inserting at the beginning of a list, Insert takes two values index and an object
numbers = [5, 2, 1, 7, 4]
numbers.insert(0, 10)
print(numbers)

#Removing an item on a list
numbers = [10, 5, 2, 1, 7, 4]
numbers.remove(2)
print(numbers)

#Clearing the list
numbers = [10, 5, 2, 1, 7, 4]
numbers.clear()
print(numbers)

#Removing last item on a list
numbers = [10, 5, 2, 1, 7, 4]
numbers.pop()
print(numbers)

#printing the index of an item on a list
numbers = [10, 5, 2, 1, 7, 4]
print(numbers.index(2))

#check for existence of an item on a list
numbers = [10, 5, 2, 1, 7, 4]
print(50 in numbers)

#count number of items on a list
numbers = [10, 5, 2, 1, 5, 7, 4]
print(numbers.count(5))

#Sort items on a list in ascending order
numbers = [10, 5, 2, 1, 7, 4]
numbers.sort()
print(numbers)


#Sort items on a list in descending order
numbers = [10, 5, 2, 1, 7, 4]
numbers.sort()
numbers.reverse()
print(numbers)

# make a copy of your list
numbers = [10, 5, 2, 1, 7, 4]
numbers2 = numbers.copy()
numbers.append(20)
print(numbers2)

# Removing duplicates on a list
numbers = [2, 2, 4, 6, 3, 4, 6, 1]
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)






