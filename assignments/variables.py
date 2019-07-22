# print("Hello world")
# print("Hello Liana")


# x=1
# x=2

# print(x)
# print(type(x))

name = "Hello World"
text = "test message"
n = 5

# STRINGS--------------------------

# print(name[5:])
# print(name[:5])
# print(name[1:7])
# print(name[1:6:2]) # start stop step
# print(name[::-1]) # reverse string
# print("tinker"[:3])

# print(name*2 + " " + text + str(n))

# print(text.split())

# print("This is a string {}".format("INSERTED"))
# print("One two {} {} {}".format('three', 'four', 'five'))
# print("One two {0} {1} {2}".format('three', 'four', 'five'))
# print("One two {2} {1} {1}".format('three', 'four', 'five'))
# print("One two {a} {b} {c}".format(a='three', b='four', c='five'))
# print(f'My string is {text}')

# result = 100/777
# print("The result was {r:1.3f}".format(r=result)) # format floating {value:width.precision f}

#LIST---------------------------------------

# my_list = [1,2,3,4]
# my_str = ['str1', 'str2', 'str3', 'str4']

# print(my_list[2:])

# print(my_list + my_str[2:])
# print((my_list + my_str)[2:])

# tmp = my_str[0]
# tmp = tmp[:3]+str(5)
# my_str[0] = tmp

# print(my_str)

# tmp = my_list.pop()
# print(my_list)
# print(tmp)
# my_list.append(5)
# my_list.append(5)

# print(my_list)
# my_list.insert(0, 6)
# print(my_list)
# my_list.remove(2)
# print(my_list)
# a = my_list.copy()
# b = a.sort()
# print(b)
# print(a)

# a.reverse()
# print(a)
# print(a.count(5))
# del a[1:]
# print(a)
# print(my_list)
# tmp = my_list.pop(1)
# print(my_list)
# print(tmp)

# c = [1,1,[1,2]]
# print(c[2][1])

# d = ['a','b', 'c']
# print(d[1:])


#Dictionaries------------------------------

# obj = {
#     'name' : 'Serg',
#     'age': 33,
#     'moto': {
#         'k': ['BMW', 'Audi'],
#         'm': 'Suzuki'

#     }
# }

# print(obj.values())
# print(obj.keys())
# obj.update({'name': 'LLL'})
# print(obj.values())
# print(obj.get('age'))
# print(obj.items())

# print(obj['name'])

# # print(obj)
# # p = obj.pop('name')
# # print(p)
# # print(obj)

# print(obj['moto']['k'][0].lower())
# obj['loc'] = 'CA'

# print(obj)
# obj['age']= 30
# print(obj)


#TUPLES-------------------------------

# my_tuple = (1,2,3,'a','b','a')# immutable
# my_list = [1,2,3] #mutable

# print(type(my_tuple))
# print(type(my_list))

# print(my_tuple.count('a'))
# print(my_tuple.index('a'))


#SETS-----------------------------------
#unordere collections of unique elements

myset = set()

print(type(myset))

myset.add(1)
myset.add(2)
print(myset)

myset.add(1)  
print(myset)

mylist = [1,1,1,'one','one','one']
print(mylist)
print(set(mylist))

s = 'aabbcc'
print(set(s))




