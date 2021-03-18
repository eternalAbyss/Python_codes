# Returns an iterator that combines multiple iterables into one sequence of tuples. Each tuple contains the elements in 
# that position from all the iterables.

items = ['bananas', 'mattresses', 'dog kennels', 'machine', 'cheeses']
weights = [15, 34, 42, 120, 5]
print(list(zip(items, weights)))
item_list = list(zip(items, weights))

# print(dict(zip(items, weights))) 
# print(list(zip(*item_list)))

for i, item in enumerate(items):
    print(i,item)

# Transpose trick
data = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (9, 10, 11))

data_transpose = tuple(zip(*data))
print(data_transpose)