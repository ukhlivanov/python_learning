# Write a brief description of all the following Object Types and Data Structures we've learned about:

import math;

# Numbers: store numeric value.
    # Python support 4 differntnum types
        # int - positive or negative numbers with no decimals
        # long - int with unlimitrd size
        # float numbers with dicimal
        # complex 

# Strings: String literals encloset single quotes or double quotes. python string immutable ds 
            # and can be iterate and can be accesable by []. python does not have char ds

# Lists: mutable, ordered sequence of objects, and defined between sqr brakets ['a', 'b' ,1]

# Tuples: is similar list ds but tuples are immutable

# Dictionaries: is collection which unordered, mutable and indexed. 
    # Python dict writen bt crully brackets and have keys and values


# Numbers
# Write an equation that uses multiplication, division, an exponent, addition, and subtraction that is equal to 100.25.

# Hint: This is just to test your memory of the basic arithmetic commands, work backwards from 100.25

print(5**2 + (50/2) + (100.25-50))

print(type(3 + 1.5 + 4))

print(math.sqrt(25))
print(5**2)

# Strings
s = 'hello'
print(s[1])
print(s[::-1]) #reverse

print(s[-1])
print(s[len(s)-1])

#list

l = []
l.append(0)
l.append(0)
l.append(0)
print(l)

d = None;

d = [0]*3
d[0] = 1
print(d)


list3 = [1,2,[3,4,'hello']]
list3[2][2] = 'goodbye'
print(list3)

list4 = [5,3,4,6,1]
list4.sort()
sorted(list4)

print(list4)

# Dictionaries
d = {'simple_key':'hello'}
print(d['simple_key'])

f = {'k1':{'k2':'hello'}}
print(f['k1']['k2'])

e = {'k1':[
            {'nest_key':['this is deep',['hello']]}
          ]
    }
print(e['k1'][0]['nest_key'][1][0])

g = {'k1':[
            1,2,{
                'k2':['this is tricky',{'tough':[1,2,['hello']]}]}
          ]
    }

print(g['k1'][2]['k2'][1]['tough'][2][0])

list5 = [1,2,2,33,4,4,11,22,3,3,2]

print(set(list5))

# Answer before running cell
# 2 > 3 false
print(2 > 3)
# Answer before running cell
# 3 <= 2 false
print(3 <= 2)


# Answer before running cell
# 3 == 2.0 false
print(3 == 2.0)

# Answer before running cell
# 3.0 == 3 true

print(3.0 == 3)

# Answer before running cell
# 4**0.5 != 2 false
print((4**0.5) != 2)


# two nested lists
l_one = [1,2,[3,4]]
l_two = [1,2,{'k1':4}]

# True or False?
print(l_one[2][0] >= l_two[2]['k1'])