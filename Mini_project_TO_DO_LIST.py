tasks = []
#Load tasks
try:
    with open("tasks.txt","r")as f:
        task = f.read().splitlines()
except:
    pass

while True:
    print("\n1.Add Task")
    print("2.View Tasks")
    print("3.Delete Task")
    print("4.Exit")

    choice = input("Enter choice :")

    if choice == "1":
        task = input("Enter task:")
        tasks.append(task)
        
        with open("tasks.txt","a") as f:
            f.write(task + "\n")

        print("Task added!")
    elif choice == "2":
        if not tasks:
            print("No tasks available")
        else :
            for i, task in enumerate(tasks, start=1):
                print(i,task)
    elif choice =="3":
        num = int(input("Enter task number:"))
        if 0 < num <= len(tasks):
            removed = tasks.pop(num - 1)

            # rewrite file 
            with open("tasks.txt","w") as f:
                for t in tasks:
                    f.write(t + "\n")

                
            print("Deleted:",removed)
        else:
            print("Invalid number")

    elif choice =="4":
        print("Goodbye!")
        break

    else:
        print("Invslid choice")
            
        