#prompting user for numbers and sign and storing the values
num1 = input("Enter a number: ")
num2 = input("Enter another number: ")
sign = input("Enter a sign: ")
#performing addition, subtraction, multiplication, and division based on the sign entered by the user
#displaying the result of the operation
if sign == "+":
    print(int(num1) + int(num2))
elif sign == "-":
    print(int(num1) - int(num2))
elif sign == "*":
    print(int(num1) * int(num2))
elif sign == "/":
    #restricting division by 0
    if num2 == "0":
        print("Cannot divide by 0")
    print(int(num1) / int(num2))
else:
    print("Invalid sign")