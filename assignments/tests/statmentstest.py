st = 'Sam Print only the words that start with s in this sentence'
res = [word for word in st.split(" ") if word[0].lower()=='s']
print(res)


res = [x for x in range(0,10) if x%2==0]
print(res)

res = [x for x in range(1,51) if x%3==0]
print(res)


st1 = 'Print every word in this sentence that has an even number of letters'
for index, word in enumerate(st1.split(" ")):
    if len(word)%2==0:
        print(f"{index} even!")


for num in range(1, 100):
    if num%3==0: 
        print("Fizz")
    elif num%5==0:
        print("Buzz")
    elif num%15==0:    
        print("FizzBuzz")
    else:
        print(num)


st = 'Create a list of the first letters of every word in this string'

res = [c[0] for c in st.split(" ")]
print(res)