try:
    age=int(input("Enter the age:"))
    if(age<18):
      raise ValueError
    else:
        print("Age is not valid")
except ValueError:
   print("The age is not valid")