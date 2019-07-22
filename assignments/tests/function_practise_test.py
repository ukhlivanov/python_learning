def lesser_of_two_evens(a,b):
    if a%2==0 and b%2==0:return min(a,b)
    else: return max(a,b)

# print(lesser_of_two_evens(2,4))
# print(lesser_of_two_evens(2,5))

def animal_crackers(s):
    c = s[0]
    for w in s.lower().split(" "):
        if s[0] != w[0]: 
            return False 
            break
    return True

# print(animal_crackers("Levelheaded Llama"))
# print(animal_crackers("Levelheaded Llama Ksda"))

def makes_twenty(a,b):
    return (a==20 or b ==20) or (a+b==20)
        
# print(makes_twenty(20,10) )
# print(makes_twenty(12,8) )
# print(makes_twenty(2,3) )

def old_macdonald(s):
    return(s[0].upper() + s[1:3] + s[3].upper() + s[4::])
# print(old_macdonald('macdonald'))

def master_yoda(s):
    rev = s.split(" ")[::-1]
    res = ' '.join(rev)
    return res

# print(master_yoda('I am home'))
# print(master_yoda('We are ready'))

def almost_there(n):
    return (n>89 and n<111) or (n>189 and n<211)

# print(almost_there(90) )
# print(almost_there(104))
# print(almost_there(150))
# print(almost_there(209))

def has_33(mylist):
    idx=1
    while idx<len(mylist):
        if mylist[idx] == mylist[idx-1]: 
            return True
        idx = idx+1
    return False

# print(has_33([1, 3, 3]) )
# print(has_33([1, 3, 1, 3]))
# print(has_33([3, 1, 3]))

def paper_doll(s):
    res=''
    for l in s:
        res = res + l*3
    return res

# print(paper_doll('Hello') )
# print(paper_doll('Mississippi') )

from random import randint
def blackjack(a,b,c):
    arr = [a,b,c]
    print(arr)
    if sum(arr) <= 21: return sum(arr)
    elif sum(arr)<=31 and 11 in arr: return sum(arr) - 10
    else : return 'BUST'

# print(blackjack(randint(1,11),randint(1,11),randint(1,11)))

# print(blackjack(5,6,7)) 
# print(blackjack(9,9,9) )
# print(blackjack(9,9,11) )

def summer_69(arr):
    s=0;
    for x in arr:
        if (x>=6 and x<=9) == False:  s = s+x
    return s;

# print(summer_69([1, 3, 5]))
# print(summer_69([4, 5, 6, 7, 8, 9]))
# print(summer_69([2, 1, 6, 9, 11]))


def spy_game(mylist):
    # num=[0,0,7]
    # c=0
    # for n in num:
    #     if n in mylist and mylist.index(n)>c:
    #         c = mylist.index(n)
    #         mylist[c] = 'None'
    #     else: return False    
    # return True 
    #   
    code = [0,0,7,'x']

    for n in mylist:
        if n == code[0]:
            code.pop(0)
    return len(code) == 1        


# print( spy_game([1,2,4,0,0,7,5]) )
# print( spy_game([1,0,2,4,0,5,7]) )
# print( spy_game([1,7,2,0,4,5,0]) ) 

def count_primes(num):
    if num < 2: return 0;
    primes = [2]
    x=3

    while x <= num:
        for y in primes:
            if x%y == 0:
                x=x+2
                break
        else:
            primes.append(x)
            x=x+2
    print(primes)
    return len(primes)

count_primes(100)


# for x in range(3,10,2):
#     print(x)
