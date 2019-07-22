# Scope resolution via LEGB rule :
# In Python, the LEGB rule is used to decide the order in which the namespaces are 
# to be searched for scope resolution.
# The scopes are listed below in terms of hierarchy(highest to lowest/narrowest to broadest):

# Local(L): Defined inside function/class
# Enclosed(E): Defined inside enclosing functions(Nested function concept)
# Global(G): Defined at the uppermost level
# Built-in(B): Reserved names in Python builtin modules

    # Scope
    # 1 Built
    #     2 GLobal
    #         3 Enclosed
    #             4 Local

lambda num: num **2 # num local variable

name = 'GLOBAL'

def greet():
        # name = 'ENCLOSED'

        def hello():
            name = 'LOCAL'
            print('Hello ' + name)

        hello()

# greet()
# print(name)

# 1 Local: looks name in hello()
# 2 Enclosed: looks name in greet()
# 3 Global: looks name outside greet() in clobal scope
# 4 Built: looks name in built? predifuned key words for python

x = 50

def func(x):
    print(f'X is {x}')
    x = 200
    print(f'new local X is {x}')

func(x)

# local scope does not effect to global scope
print(x) # --> 50

print('-----------------')

y = 50

def func():
    global y # We are going to use  y declared globally. AVOID USE GLOBAL KEY WORD
    print(f'y is {y}')
    y = 200 # reassign globall variable y
    print(f'new global y is {y}')

func()

print(y) # --> 200

print('-----------------')

# For reassign global variables

x = 50

def func(x):
    print(f'X is {x}')
    x = 200
    print(f'new local X is {x}')
    return x

x=func(x)

print(x)
