

""" def fizzbuzz(n):
    fizzbuzz_dict = {3: 'Fizz', 5: 'Buzz'}
    for i in range(1, n + 1):
        result = ''
        for key in fizzbuzz_dict:
            if i % key == 0:
                result += fizzbuzz_dict[key]
        if not result:
            result = i
            print(result)
            
fizzbuzz(15) """


fizzbuzz_dict = {
    3: "Fizz",
    5: "Buzz"
}

for num in range(1, 101):
    output = ""
    
    for key in fizzbuzz_dict:
        if num % key == 0:
            output += fizzbuzz_dict[key]
        print(output or num)