# Unordered unique set of elements

a = [1,2,2,3,3,3,4,4,4,4]
b = set(a)
# print(len(a) - len(b)) 
b.add(5)
b.pop()
print(b)