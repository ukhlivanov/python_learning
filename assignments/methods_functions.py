myList = [1,2,3]
def myfunction(n1,n2):
    '''
        DOCSTRINGS: information about the function
        INPUT: number1(int) and number2(int)
        OUTPUT: number
    '''
    return n1+n2


# res = myfunction(3,4)
# print(res)

def pig_latin(word):
    vowels= ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
    if word[0] in vowels:
        return word + 'ay'
    else:
        return word[1:] + word[0] + 'ay'

# res = pig_latin('apple')
# print(res)

def myfunc1(*args):
    return sum(args) * 0.05 #return tuple

# print(myfunc1(10, 20,30, 1000))

def myfunc2(**kwargs): #key word arguments
    print(kwargs)
    if 'fruit' in kwargs:
        return ('bla bla {}'.format(kwargs['fruit'])) #return object or dictionarie
    else: return('bla bla')

# print(myfunc2(fruit='apple', veggie = 'tomat'))
def myfunc(s):
    res=''
    for index, l in enumerate(s):
        if index%2==0: 
            res=res + l.upper()
        else:
            res=res + l.lower()
    return res

print(myfunc('Liana'))