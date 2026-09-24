
def add(a,b): 
    return a+b

def main():
    a = float(input("First number: "))
    op = input("Operation: ")
    b = float(input("Second number: "))

    if op == "+":
        print(add(a,b))
    elif op == "-":
        print(subtract(a,b))
    elif op == "/":
        print(divide(a,b))
    elif op == "*":
        print(multiply(a,b))

main()
