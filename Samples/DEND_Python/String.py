first_word = "Hello"
second_word = "There"

print(first_word + second_word)
print((first_word + second_word) * 3)
print(len(first_word))
print(first_word[2])

ford_quote = 'Whether you think you can, or you think you can\'t--you\'re right.'
ford_quote = "Whether you think you can, or you think you can\'t--you\'re right."

print(ford_quote)

coconut_count = "34"
mango_count = "15"
tropical_fruit_count = coconut_count + mango_count
print(tropical_fruit_count)
# print(len(835)) error


print(type(633))
print(type("633"))
print(type(633.0))

print(type(len("my_string")))

print(type("hippo" * 12))

mon_sales = "121"
tues_sales = "105"
wed_sales = "110"
thurs_sales = "98"
fri_sales = "95"

weekly_sales = int(mon_sales) + int(tues_sales) + int(wed_sales) + int(thurs_sales) + int(fri_sales)
weekly_sales = str(weekly_sales)  # convert the type back!!
print("This week's total sales: " + weekly_sales)

print(13.37.is_integer())

print("hi".encode())

verse = "If you can keep your head when all about you\n  Are losing theirs and blaming it on you,\nIf you can trust yourself when all men doubt you,\n  But make allowance for their doubting too;\nIf you can wait and not be tired by waiting,\n  Or being lied about, don’t deal in lies,\nOr being hated, don’t give way to hating,\n  And yet don’t look too good, nor talk too wise:"
print(verse, "\n")
print("Verse has a length of {} characters.".format(len(verse)))
print("The first occurence of the word 'and' occurs at the {}th index.".format(verse.find('and')))
print("The last occurence of the word 'you' occurs at the {}th index.".format(verse.rfind('you')))
print("The word 'you' occurs {} times in the verse.".format(verse.count('you')))
print(verse.__len__())
print(verse.find('and'))
print(verse.rfind('you'))
print(verse.count('you'))
