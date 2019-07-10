print('Simple Assignment')
shoplist = ['apple', 'mango', 'carrot', 'banana']
# mylist is just another name pointing to the same object!
mylist = shoplist
# I purchased the first item, so I remove it from the list
del shoplist[0]
print('shoplist is', shoplist)
print('mylist is', mylist)
# Notice that both shoplist and mylist both print
# the same list without the 'apple' confirming that
# they point to the same object
print('Copy by making a full slice')
# Make a copy by doing a full slice

mylist = shoplist[:] # 복사본 참조방법

# mylist = shoplist # 그냥 이름만 바뀜. 같은 객체 참조

# Remove first item
del mylist[0]
print('shoplist is', shoplist)
print('mylist is', mylist)
# Notice that now the two lists are different
'''
슬라이스 연산자를 이용해서 복사본을 생성해야함.
단순히 변수로 할당하면, 같은 객체를 참조
'''
