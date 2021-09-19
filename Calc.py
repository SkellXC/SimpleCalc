num1 = int(input("Please enter a number: "))
num2 = int(input("Please enter another number: "))
while True:
    numFunc = input("Please enter a function: ")
    if numFunc in ("+","-","/","*"):
            break
else:
            print("incorrect function... ")

if numFunc == "*":
                  print("The answer is:",num1 * num2)
elif numFunc == "+":
    print("The answer is:",num1 + num2)
elif numFunc == "-":
    print("The answer is:",num1 - num2)
elif numFunc == "/":
    print("The answer is:",num1 / num2)

