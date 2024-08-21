
""" num = input("Please input a number")

for num in range(1, 101):
    if num % 15 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    elif num % 3 == 0:
        print("FizzBuzz")
    else:
        print(num)
     """
     
     
     # This is Fibonacci sequence in an easy way
n = 20
num1, num2 = 0, 1
count = 0

while count < n:
    print(num1, end=" ")
    nth = num1 + num2
    num1 = num2
    num2 = nth
    count += 1
    
    