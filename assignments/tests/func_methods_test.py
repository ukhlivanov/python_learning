import math

def vol(rad):
    return (4/3) * math.pi * rad**3
res = vol(2)
# print(res)

def ran_check(num,low,high):
    # return num>=low and num<=high
    return num in range(low, high)

res = ran_check(0,2,7)    
# print(res)



def up_low(s):
    uppers = list( filter( (lambda x:x.isupper()),s ) ) 
    lowers = list( filter( (lambda x:x.islower()),s ) )
    print(uppers)
    print(len(uppers))
    print(lowers)
    print(len(lowers))


# up_low('Hello Mr. Rogers, how are you this fine Tuesday?')

def unique_list(lst):
    print(list(set(lst)))
    return (list(set(lst)))

# unique_list([1,1,1,1,2,2,3,3,3,3,4,5])


def multiply(numbers):
    tmp = 1  
    for x in numbers:
        tmp = x * tmp
    print(tmp)

# multiply([1,2,3,-4])

def palindrome(s):
    return s == s[::-1]

# print(palindrome('helleh'))
import string

def ispangram(str1, alphabet=string.ascii_lowercase):
    print(alphabet)
    str1 = str1.lower()
    print(type(str1))

    str1 = set(str1)
    print(type(str1))

    str1  = sorted(str1)
    print(type(str1))

    str1 = ''.join(str1)
    print(type(str1))

    str1 = str1.strip()
    print(type(str1))


    # str1 = ''.join(sorted(set(str1.lower()))).strip()
    print(str1)

    return str1 == alphabet

# print(ispangram("The quick brown fox jumps over the lazy dog"))