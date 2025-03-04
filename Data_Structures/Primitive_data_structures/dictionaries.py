# Stores key value pairs

elements = {"hydrogen": 1, "helium": 2, "carbon": 6}
print("mithril" in elements)
# get returns None if the element is not present in the disctionary
print(elements.get("dilithium"))

# get with default message when the element is not found
print(elements.get("kryptonite", "There's no such element!"))

animals = {
    "dogs": [20, 10, 15, 8, 32, 15],
    "cats": [3, 4, 2, 8, 2, 4],
    "rabbits": [2, 3, 3],
    "fish": [0.3, 0.5, 0.8, 0.3, 1],
}

elements = {
    "hydrogen": {"number": 1, "weight": 1.00794, "symbol": "H"},
    "helium": {"number": 2, "weight": 4.002602, "symbol": "He"},
}

# todo: Add an 'is_noble_gas' entry to the hydrogen and helium dictionaries
# hint: helium is a noble gas, hydrogen isn't
elements["hydrogen"]["is_noble_gas"] = False
elements["helium"]["is_noble_gas"] = True
print(elements["helium"]["is_noble_gas"])
