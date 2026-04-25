a = int(input("Pehla number: "))
b = int(input("Doosra number: "))
op = input("Operation (+, -, *, /): ")

if op == "+":
    print("Jawab:", a + b)
elif op == "-":
    print("Jawab:", a - b)
elif op == "*":
    print("Jawab:", a * b)
elif op == "/":
    print("Jawab:", a / b)
else:
    print("Galat operation!")
