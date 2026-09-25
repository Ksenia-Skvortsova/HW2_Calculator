
   


 


    


    

def main():
    a, op, b = input('Введите два числа и оператор через пробел: ').split()
    a = float(a)
    b = float(b)

    if op == "+":
        print(add(a,b))
    elif op == "-":
        print(subtract(a,b))
    elif op == "/":
        print(divide(a,b))
    elif op == "*":
        print(multiply(a,b))

main()

# Kutelev Ivan
def divide(a,b):
    return a / b