def add(a,b):
      return a + b

def sub(a,b):
      return a - b

def multi(a,b):
      return a * b

def divi(a,b):
      if b != 0:
          return a / b
      else :
            return "enter a valid value"
      

while True :
      print("\n1.add 2.sub 3.multi 4.divi 5.Exit")
      choice = int(input("Enter your choice : "))

      if choice == "5":
            break
      
      a = int(input("Enter the value of a : "))
      b = int(input("Enter the value of b : "))

      if choice == "1":
            print("Result : ",add(a,b))

      elif choice == "2":
            print("Result : ",sub(a,b))

      elif choice == "3":
            print("Result : ", multi(a,b))

      elif choice == "4":
            print("Result : ", divi(a,b))

      elif choice == "4":
            print("Result : ", divi(a,b))

      else :
            print("Invalid choice ")



      