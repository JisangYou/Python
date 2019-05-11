elements = {'hydrogen': 1, 'helium': 2, 'carbon': 6}
elements['lithium'] = 3
print(elements)
print("carbon" in elements)
print(elements.get("dilithium"))
n = elements.get("dilithium")
print(n is None)
print(n is not None)

population = {"Shanghai": 17.8,
              "Istanbul": 13.3,
              "Karachi": 13.0,
              "Mumbai": 12.5}

a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a == b)
print(a is b)
print(a == c)
print(a is c)
# equality vs. identity

# Python, any immutable object (such as an integer, boolean, string, tuple) is hashable, meaning its value does not change during its lifetime.

elements = {"hydrogen": {"number": 1,
                         "weight": 1.00794,
                         "symbol": "H"},
            "helium": {"number": 2,
                       "weight": 4.002602,
                       "symbol": "He"}}

helium = elements["helium"]  # get the helium dictionary
hydrogen_weight = elements["hydrogen"]["weight"]  # get hydrogen's weight
oxygen = {"number": 8, "weight": 15.999, "symbol": "O"}  # create a new oxygen dictionary
elements["oxygen"] = oxygen  # assign 'oxygen' as a key to the elements dictionary
print('elements = ', elements)
