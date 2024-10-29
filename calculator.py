import re

def add(x, y): return x + y
def subtract(x, y): return x - y
def multiply(x, y): return x * y
def divide(x, y): return x / y

OPERATIONS = {"+": add, "-": subtract, "*": multiply, "x": multiply, "/": divide}

def get_user_math_problem():
    while True:
        expression = input("Enter a math problem: ")
        problem = re.split(r'([+\-*x/])', expression)
        
        if len(problem) == 3:
            try:
                a = float(problem[0].strip())
                b = float(problem[2].strip())
                operator = problem[1].strip()

                if operator in OPERATIONS:
                    return OPERATIONS[operator](a, b)
                else:
                    print("Invalid operator.")
            except ValueError:
                print("Please enter valid numbers.")
            except ZeroDivisionError:
                print("Division by zero not allowed.")
        else:
            print("Please only one operation at a time.")

def main():
    result = get_user_math_problem()
    if result is not None:
        print(int(result) if result.is_integer() else round(result, 3))


if __name__ == "__main__":
    main()