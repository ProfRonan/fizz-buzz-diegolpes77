número = int(input("digite um número inteiro: "))
if número % 3 == 0 and número % 5 ==0:  
    print("FizzBuzz")
elif número % 3 ==0: 
    print("Fizz")
elif número % 5 == 0:
    print("Buzz")
else: 
    print(número)