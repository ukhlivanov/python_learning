

# for num in range(10):
#     print(num)

# print('------------------')

# for num in range(3,10):
#     print(num)

# print('------------------')

# for num in range(0,10,2):
#     print(num)

# print('------------------')

# print(list(range(0,10,2)))

# idx=0;
# word = 'abcde'

# for _ in word:
#     print(f'At index {idx} the letter is {word[idx]}')
#     print(word[idx])
#     idx +=1

# print('------------------')

# for index, item in enumerate(word):  
#     print(index)
#     print(item)

# print('------------------')

# mylist1 = [1,2,3,4,5]
# mylist2 = ['a','b','c','d','e']
# mylist3 = ['a1','b1','c1','d1','e1']


# for item in zip(mylist1, mylist2, mylist3):
#     print(item)

# print('------------------')

# print(list(zip(mylist1, mylist2)))

# print('------------------')

# print('x' in ['x', 'y','z'])
# print('x1' in ['x', 'y','z'])

# print('------------------')


# print('a' in 'a world')
# print('key' in {'key': 345})

# d = {'key': 345}
# print(345 in d.values())

# print('------------------')

# mylist1 = [1,2,3,4,7]
# print(min(mylist1))
# print(min(10,3))
# print(max(mylist1))
# print(max(10,3))

# print('------------------')
# from random import shuffle

# shuffle(mylist1) # randomly shake list
# print(mylist1)

# print('------------------')

# from random import randint
# print(randint(1,10))

# print('------------------')

# r = input('Enter number: ')
# print(r)
# print(float(r))

# print('------------------')

mylist2 = []

for c in 'abcde':
    mylist2.append(c)

print(mylist2)

mylist2 = [ x for x in 'dsfsdfs']
print(mylist2)

mylist2 = [num for num in range(0,11)]
print(mylist2)

mylist2 = [num**2 for num in range(0,11)]
print(mylist2)

mylist2 = [num**2 for num in range(0,11) if num%2==0]
print(mylist2)


celcius = [0, 10 ,20, 35.6]

for c1 in range(1,5):
    for c2 in range(11,16):
        print(c1+c2)
