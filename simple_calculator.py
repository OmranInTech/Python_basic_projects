def add(*args):
    return sum(args)

def subtract(*args):
    result = args[0]
    for num in args[1:]:
        result -= num
    return result

def multiply(*args):
    result = 1
    for num in args:
        result *= num
    return result

def divide(*args):
    result = args[0]
    for num in args[1:]:
        if num == 0:
            return "Error! Division by zero."
        result /= num
    return result

def calculator():
    print("Simple Calculator with *args")

    while True:
        print("\nSelect operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")

        choice = input("Enter choice (1/2/3/4/5): ")

        if choice == '5':
            print("Exiting...")
            break

        if choice in ['1', '2', '3', '4']:
            try:
                numbers = list(map(float, input("Enter numbers separated by space: ").split()))
                
                if choice == '1':
                    print(f"Result: {add(*numbers)}")
                elif choice == '2':
                    print(f"Result: {subtract(*numbers)}")
                elif choice == '3':
                    print(f"Result: {multiply(*numbers)}")
                elif choice == '4':
                    print(f"Result: {divide(*numbers)}")
            except ValueError:
                print("Invalid input! Please enter numeric values.")
        else:
            print("Invalid input! Please select a valid operation.")

if __name__ == "__main__":
    calculator()
