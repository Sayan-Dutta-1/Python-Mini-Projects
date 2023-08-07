#Adding Function
def add (num1,num2):
    '''This function adds 2 numbers''' 
    return num1+num2

#Subtracting Function
def subtract (num1,num2):
    '''This function subtracts 2 numbers''' 
    return num1-num2

#multiplying Function
def multiply (num1,num2):
    '''This function multiplies 2 numbers''' 
    return num1*num2

#Dividing Function
def divide (num1,num2):
    '''This function divides 2 numbers''' 
    return num1/num2

Calc_ops = {"+" : add, "-" : subtract, "*" : multiply, "/" : divide }

def calculator():
    number1 = float(input("Enter the First number: ")) 
    for operation in Calc_ops:
        print(operation)
    continuation_Choice = True
    while continuation_Choice:
        Chose_operation = input("Chose what operation do you want to perform: ")

        number2 = float(input("Enter the other number: "))

        operation_function = Calc_ops[Chose_operation]
        answer = round(operation_function(number1, number2),2) 
        print(f"{number1} {Chose_operation} {number2} = {answer}")
        choice = input(f"Do you want to continue the calculation with {answer} - 'Yes/No'.\nEnter 'quit' to stop calculating.\n")
        if choice.lower() == "yes":
            continuation_Choice = True
            number1 = answer
        elif choice.lower() == "no" :
            continuation_Choice = False
            calculator()
        else:
            exit()
calculator()
