def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    try:
        return x/y
    except ZeroDivisionError:
        print("Division by zero is not allowed")
        return None

if __name__ == "__main__":
    
    print("Enter two numbers")
    x = int(input())
    y = int(input())
    print("Enter operation to be performed")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    choice = int(input())
    if choice == 1:
        print(add(x,y))
    elif choice == 2:
        print(sub(x,y))
    elif choice == 3:
        print(mul(x,y))
    elif choice == 4:
        print(div(x,y))
    else:
        print("Invalid choice")