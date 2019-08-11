sentence = ["a", "b", "c", "d", "e", "f"]
for se in sentence:
    print(se)

for i in range(5, 35, 5):
    print(i)

names = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]
usernames = []

for name in names:
    usernames.append(name.lower().replace(" ", "_"))

print(usernames)

# names = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]
#
# for name in names:
#     name = name.lower().replace(" ", "_")
#
# print(names)

usernames = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]

for i in range(len(usernames)):
    usernames[i] = usernames[i].lower().replace(" ", "_")

print(usernames)

tokens = ['<greeting>', 'Hello World!', '</greeting>']

count = 0
for token in tokens:
    print(token[0])
    print(token[1])

    # if token[0] == '<' and token[-1] == '>':
    #     count += 1

print(count)

# 하기는 딕셔너리의 키, 벨류를 모두 뽑아내는
cast = {
    "Jerry Seinfeld": "Jerry Seinfeld",
    "Julia Louis-Dreyfus": "Elaine Benes",
    "Jason Alexander": "George Costanza",
    "Michael Richards": "Cosmo Kramer"
}

for key, value in cast.items():
    print("Actor: {}    Role: {}".format(key, value))

result = 0
basket_items = {'a': 1, 'b': 2, 'c': 3, 'd': 4 }
fruits = ['a', 'b', 'c', 'd', 'e', 'f']

for x, y in basket_items.items():
    if x in fruits:
        result += y

print("There are {} fruits in the basket.".format(result))


# number to find the factorial of
number = 6
# start with our product equal to one
product = 1
# track the current number being multiplied
current = 1

while current <= number:
    # multiply the product so far by the current number
    product *= current
    print("product", product)
    # increment current with each iteration until it reaches number
    current += 1
    print("current", current)

# print the factorial of number
print(product)

# number we'll find the factorial of
number = 6
# start with our product equal to one
product = 1

# calculate factorial of number with a for loop
for num in range(2, number + 1):
    product *= num

# print the factorial of number
print(product)


# For Loops Vs. While Loops

# for loops are ideal when the number of iterations is known or finite.

# while loops are ideal when the iterations need to continue until a condition is met.
