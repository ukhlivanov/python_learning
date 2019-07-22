# MAP-------------------
# map applyed function square() every element in list my_nums

def square(num):
    return num**2

my_nums = [1,2,3,4,5]

for item in map(square, my_nums):
    print(item)

res = list(map(square, my_nums))
print(res)
print('-----------------------')
# Filter ---------------
# filter based off condition in function is_even()

def is_even(num):
    return num%2==0

for item in filter(is_even, my_nums):
    print(item)

res = list(filter(is_even, my_nums))
print(res)

print('-----------------------')

#Lambda expressions(LE)0----------------------
# LE is ananymos function, functionality that you intent use one time
square = lambda num: num**2

print(square(3))

res = list(map((lambda num: num ** 2),my_nums))
print(res)

res = list(filter((lambda num: num%2==0), res))
print(res)



res = list(map((lambda x:x[::-1]), ['Liana', 'Sergey', 'Lutik']))
print(res)

print('-----------------------')

