'''
list
'''
a = list('cat')
print("")
print(a)
print("")
print("==============")

marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
others = ['Gummo', 'Karl']
marxes2 = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
others2 = ['Gummo', 'Karl']
marxes.extend(others)
marxes2.append(others2)
print("")
print(marxes)
print("")
print(marxes2)
print("==============")

'''
dict
'''
tol = (['a', 'b'], ['c', 'd'], ['e', 'f'])
print("")
print(dict(tol))
print("")
print("==============")
print("")
'''
tuple
'''
marx_tuple = ('Groucho', 'Chico', 'Harpo')
a, b, c, = marx_tuple
print(a)
print(b)
print(c)
print(marx_tuple)
print("")
print("==============")
