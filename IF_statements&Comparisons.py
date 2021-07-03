num1 = float(input("Enter the value for num1 = ") )# In python if the user enter the valve it will convects into string
#if you want convert the string into intger you need to use this operation (float()).
num2 = float(input("Enter the value for num2 = "))
num3 = float(input("Enter the value for num3 = "))
def max_num(num1, num2, num3):
    if num1>=num2 and num1>=num3:#
        return num1#The return will stroe the excuted parament in retrun and retrun it to the calling function.
    elif num2>=num1 and num2>=num3:
        return num2
    elif num3>=num1 and num3>=num1:
        return num3
    else:
        return print("you are wrong")
result = max_num(num1, num2, num3)
print(result)#calling the function.

