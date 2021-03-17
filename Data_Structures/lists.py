# LISTS

#''' Data structures are containers that organize and group data types together in different ways. 
# A list is one of the most common and basic data structures in Python.'''

list_of_random_things = [1, 3.4, 'a string', True]
print(list_of_random_things[-2])

# Using slicing to get a subset of the list
# Lower bound is inclusive and Upper bound is exclusive
 
print(list_of_random_things[:3])
print(list_of_random_things[:-1])

# Checking if an element is in the list or not

print('2' in list_of_random_things)
print('3.4' in list_of_random_things)

# Strings are immutable and Lists are mutable
# Both strings and lists are ordered 
# order -> we can access the vlaue using indices

lort = list_of_random_things
lort[0] = 10
print('lort is equal to list_of_random_things : ',lort == list_of_random_things)

numbers = [1,2,3,4,5,12,32,4,22]
print('The largest number in the list {} is {}'.format(sorted(numbers, reverse = True), max(numbers)))
print('The smallest number in the list {} is {}'.format(sorted(numbers), min(numbers)))

# Join method joins the elements of the given list with the separator defined before the method.
list_random = " ".join(str(list_of_random_things))
print(list_random)