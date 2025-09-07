def add(x,y):
    return x + y
def sub(x,y):
    return x - y
def mul(x,y):
    return(x * y)
def div(x,y):
    if y == 0:
        return "Error! Division by zero."
    return(x / y)
def mod(x,y):
    if y == 0:
        return "Error! Division by zero."
    return(x % y)
def floor(x,y):
    if y == 0:
        return "Error! Division by zero."
    return(x // y)
def power(x,y):
    if y == 0:
        return "Error! Division by zero."
    return(x ** y)

print("Select operation.")
print("1. Add")
print("2. Sub")
print("3. Multiply")
print("4. Division")
print("5. Modulus")
print("6. Floor Division")
print("7. Power")

while True:
    choice = input("Enter choice: ")

    if choice in ('1','2','3','4','5','6','7'):
        try:
            num1 = float(input("Enter 1st num: "))
            num2 = float(input("Enter 2nd num: "))
        except ValueError:
            print("Invalid input. Please enter a number again.")
            continue
        if choice == '1':
            print(num1, "+", num2, "=", add(num1,num2))
        elif choice == '2':
            print(num1, "-", num2, "=", sub(num1,num2))
        elif choice == '3':
            print(num1, "*", num2, "=", mul(num1,num2))
        elif choice == '4':
            print(num1, "/", num2, "=", div(num1,num2))
        elif choice == '5':
            print(num1, "%", num2, "=", mod(num1,num2))
        elif choice == '6':
            print(num1, "//", num2, "=", floor(num1,num2))
        elif choice == '7':
            print(num1, "**", num2, "=", power(num1,num2))
        else:
            print("Invalid")
        
        nxt_cal = input("Let's do next calculation: [y/n]: ")
        if nxt_cal.lower() == "n":
            break
    else:
        print("Invalid inputs.....")  