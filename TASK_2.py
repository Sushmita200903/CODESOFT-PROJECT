first= input("Enter the first input number:")
operator = input("enter your operator:(+,-,%,,*,/):")
second= input("Enter the second input number:")
first= int(first)
second=int(second)
if operator == "+":
    print(first + second)
elif operator == "-":
    print(first - second)
elif operator == "*":
    print(first * second)
elif operator == "%":
    print(first % second)
elif operator == "/":
    print(first / second)
elif operator == "":
    print(first ** second)
else:
    print("Invalid Operator")