def fizz_buzz(n):
    for i in range(1, n+1):  # Loop from 1 to n
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

# Call the function with 100 to run the classic FizzBuzz
fizz_buzz(100)
