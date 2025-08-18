try:
    num1 , num2=eval(input("Enter two numbers,seperated by a comma"))
    result=num1/num2
    print(result)
except ZeroDivisionError:
     print("Division by zero is an error")
except SyntaxError:
    print("Comma is missing.enter numbers seperated by commas like:1,2")              
else:             
    print("no exceptions")
finally:
    print("This print statement gets excecuted no matter what")