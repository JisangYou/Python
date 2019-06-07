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
