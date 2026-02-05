tasks =[]

while True :
     print("\nTo do lists")
     print("1.To Add Task")
     print("2.To Remove Task")
     print("3.To View Task")
     print("4. To Exit")

     choice = int(input("Enter what to do : "))

     if choice == 1 :
          task = input("Enter your tasks : ")
          tasks.append(task)
          print("Task added succesfully..!! ")



     elif choice == 2 :
          if len(tasks) == 0 :
               print("No task avaible to remove ..")
          else :
               print("\n Your tasks : ")
               for i, t in enumerate(tasks, start=1):
                    print(i,".",t)
          num = int(input("Enter your task no :"))
          
          if 1 <= num <= len(tasks):
                removed = tasks.pop(num - 1)
                print("Deleted:", removed)
          else:
                print("Invalid task number.")



     elif choice == 3 :
                if len(tasks) == 0:
                     print("No tasks available.")
                else:
                     print("\nYour Tasks:")
                     for i, t in enumerate(tasks, start=1):
                         print(i, ".", t)


     elif choice == 4 :
        print("GoodBye..!!")
        break
     
     
     else :
       print("Invalid choice ..!!")


     
    


