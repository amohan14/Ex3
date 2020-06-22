# define the function blocks

def addition4(w = 8, x = 4, y = 2, z = 1):
    op = w + x + y + z
    print(op)

def subtract4(w = 8, x = 4, y = 2, z = 1):
    op = w - x - y - z
    print(op)

def multiply4(w = 8, x = 4, y = 2, z = 1):
    op = w * x * y * z
    print(op)

def divide4(w = 8, x = 4, y = 2, z = 1):
    op = (w / x / y / z)
    print(op)

option = int(input("Enter a number between between 1 to 4 for 1:Add, 2:Subtract, 3:Multiply, 4:Divide "))
if(option > 0 and option < 5):
    num_ip = int(input("How many numbers to enter (max 4):"))
    if(num_ip < 0 ):
        print("Cannot accept negative input, proceeding with no inputs.")
        num_ip = 0
    elif(num_ip > 4):
        print("Max input is 4, proceeding with 4 inputs.")
        num_ip = 4

num_list = []
for i in range(num_ip):
    num = int(input("Enter number:"))
    num_list.append(num)
# map the inputs to the function blocks

def calculator(option):
    if(option == 1):
        addition4(*num_list)
    elif(option == 2):
        subtract4(*num_list)
    elif(option == 3):
        multiply4(*num_list)
    elif(option == 4):
        divide4(*num_list)
    else:
        print("Invalid Input")

calculator(option)

