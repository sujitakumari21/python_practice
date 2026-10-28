# count = 1
# while count <= 5:
#     print("Sujita kumari")
#     count +=1


# count = 1
# name = input("Enter your name :")
# while count <= 5:
#     print(name)
#     count +=1

# count = 5
# while count >= 1:
#     print(count)
#     count -= 1

# sum = 0
# count = 1
# while count <= 10:
#     sum = sum+count
#     count = count+1
# print("sum ",sum)
# i = 5
# while i>=1:
#     j=1
#     while j <=i:
#         print("*", end=" ")
#         j+=1
#     print()
#     i -= 1

# for count in 1,2:
#     print("I love to code in python")
# count = 1
# for count in range(1,9,3):
#  print(count)

# sum =0
# for x in range (1,11):
#     sum = sum +x
# print("Sum of x is : ", sum)

# for ch in 'Python':
#     print("current character is :", ch)

# fruits = ['Apple' , 'Banana', 'orange', 'Mango']
# for item in fruits:
#     print(item)
# print("loop finished....")


# num = int(input("Enter a number"))
# even_sum =0
# odd_sum= 0
# for x in range (num):
#     if x%2==0:
#         even_sum = even_sum +x
#     else:
#         odd_sum = odd_sum+x
# print("sum of even number is ",even_sum)
# print("sum of odd number is ", odd_sum)

#FACTORIAL
# n= int(input("Enter any number"))
# fact = 1
# for i in range (1, n+1):
#     fact=fact*i
# print("factorial = ",fact)

#Table of 2
# for i in range(1,2):
#     for j in range(1,11):
#         print("4 x",j,"=",4*j)

# print("Display a triangle of * ")
# for x in range(1,6):
#     for y in range(1, x +1):
#         print("* ",end="" )
#     print()
    

# for x in range (1,11):
#     if x ==5:
#         break
#     print("x = ",x)


#CONTININUE
# for letter in "Python":
#     if letter == "t":
#         continue
#     print("current letter is ",letter)


#BREAK
# for letter in "Python":
#     if letter =="t":
#         break
#     print("current letter is ",letter)

#  evenodd(x):
    
#     if x%2==0:
#         print("number",x, "is even")
#     else:
#         printdef("number",x, "is odd" )

#     evenodd(20)
#     evenodd(15)
    
# MINI_CALCULATOR

# num1 = int(input("Enter first number "))
# num2 = int(input("Enter second number"))

# def add(num1 , num2):
#     add = num1+num2
#     print(add)
# def sub(num1,num2):
#     sub = num1-num2
#     print(sub)
# def multiply(num1,num2):
#     multiply = num1*num2
#     print(multiply)
# def division(num1, num2):
#     division = num1/num2
#     print(division)

# add(num1,num2)
# sub(num1,num2)
# multiply(num1,num2)
# division(num1,num2)

#STUDENT_INFO_USING_FUNCTION

# def studentinfo(name ,gender ="Female"):
#     print("Name",name)
#     print("Gender",gender)

# studentinfo("Sujita")
# studentinfo("kritika",gender = "Female")
 

#SWAP using three variables
# a=25
# b=65
# temp=a
# a=b
# b=temp

# print(a)
# print(b)

# SWAP using two variable
# a=12
# b=96
# c=45
# d= 10
# a,b,c,d = b,a,d,c
# print(a)
# print(b)
# print(c)
# print(d)

#USER INPUT
# a = int(input("Enter first number :"))
# b = int(input("Enter second number :"))
# a,b=b,a
# print("a=",a)
# print("b=",b)

#LEAP YEAR 
# year = int(input("Enter any year :"))
# if year %4==0 :
#     print("Leap year")
# else:
#     print("NON leap year")

#STRING
# msg= "Goodbye"
# print("string :",msg)
# print("First character of string",msg[0])
# print("Second character of string",msg[1])
# print("Third character of string",msg[2])
# print("Last character of string",msg[len(msg)-1])
# print(len(msg))

# str = "Python "
# print("Original string :",str)
# print("ID of original string :",id(str))
# str = str +"programming"
# print("Modified str :",str)
# print("Modified id :",id(str))


#FInd the length of the string withouth using len function
# def main():
#     user_str =input("Enter a string")
#     count_char =0
#     for ch in user_str:
#         count_char += 1
#         print("length of the entered string is",count_char)
#         main()


# str = "file "*4
# print(str)


# first_name= "Sujita "
# middle_name ="Kumari "
# last_name = "Yadav" 
# full_name = ''.join((first_name,middle_name,last_name))
# print("Full_name:",full_name)

# dob =["21","12","2029"]
# my_dob ='/'.join(dob)
# print("Date of birth",my_dob)

# STRING SLICING
# string = "Welcome to scientech easy"
# my_sub1 = slice(7)
# print("my_sub1 object",my_sub1)
# print("Substring from 0 to 7:",string[my_sub1])
# my_sub2 = slice(11,21)
# print("my_sub2 object:",my_sub2)
# print("Substring from 11 to 21:",string[my_sub2])
# my_sub3 = slice(0,20,2)
# print("Substring containing every second elements:",string[my_sub3])


# healthy_juice = "Mangoo juice"
# print("original string :",healthy_juice)
# my_sub1 = healthy_juice[0:4]
# print("substrings from 0 to 4",my_sub1)
# my_sub2 = healthy_juice[:6]
# print("substring  upto 6:",my_sub2)
# my_sub3 = healthy_juice[6: ]
# print("substring upto end :",my_sub3)
# my_sub4 = healthy_juice[:]
# print("Entire substring :",my_sub4)
# my_sub5 = healthy_juice[4:4]
# print("Empty string :", my_sub5)
# my_sub6 = healthy_juice[6:12]
# print("substring up to end :",my_sub6)

# matrix = [[2,5,6],[2,6,5],[7,9,6]]
# print(matrix)

# x = [1, 2, 3, 4]
# y = [5, 6, 7, 8]
# result = x + y # Adding the lists x and y.
# print(result)

# x = ('Hello', 20)
# y = (20.50, 'Hi')
# z = (20, 89)
# result = x + y + z
# print(result)

# x="Rahul"
# y=" 45"
# result = x + y
# print(result)

# x= 20
# y = 30.60
# sub = x-y
# print("Subtraction :", sub)

# x=25
# y =5
# z=x*y
# print("multiplication:",z)

# text = "Hello "
# y = 2
# result = text*y
# print("Result :",result)

# list = ["python" , "Programming"]
# y=2
# result = list*y
# print("Result",result)

# x =5
# y =5
# z =x/y
# print(z)

# x = 2.4
# y =1.2
# z = x/y
# print(z)

# num_1=23
# num_2 = 5
# num = num_1 % num_2
# print(num)

# num1 = 2
# num2 = 4
# exp = num1**num2
# print("Result :",exp)

# num1 = 2
# num2 = 4
# exp = num1 ** num2
# print("Result: ", exp)

# x = 1.2
# y = 3
# exp = x ** y
# print("Result: ", exp)

# num1 = 5
# num2 = 2
# num = num1 // num2
# print("Result: ", num)

# x = 12.2
# y = 3.1
# z = x // y
# print("Result: ", z)

# num1 = int(input("Enter the first number: "))
# num2 = int(input("Enter the second number: "))

# print("Addition (num1 + num2): ", (num1 + num2))
# print("Subtraction (num1 - num2): ", (num1 - num2))
# print("Multiplication (num1 * num2): ", (num1 * num2))

# print("Division (num1 / num2): ", (num1 / num2))
# print("Floor division (num1 // num2): ", (num1 // num2))

# print("Modulus (num1 % num2): ", (num1 % num2))
# print("Exponential (num1 ** num2): ", (num1 ** num2))

#Add and Assignment Operator (+=)

# x = 20
# y = 5
# z = 10
# x += y
# print("Result of (x = x + y) = ", x)
# z += x + y
# print("Result = ", z)

#Subtract and Assignment Operator (-=)

# x = 20
# y = 5
# z = 10
# x -= y
# print("Result of (x = x - y) = ", x)
# z -= x + y
# print("Result = ", z)

#Multiply and Assignment operator (*=)

# x = 2
# y = 5
# z = 3
# x *= y
# print("Result of (x = x * y) = ", x)
# z *= x * y
# print("Result = ", z)

# Divide and Assignment Operator (/=)

# x = 20
# y = 5
# z = 100
# x /= y
# print("Result of (x = x / y) = ", x)
# z /= x * y
# print("Result = ", z)

balance = 0
transaction_history = []
def deposit():
    global balance
    amount= float(input("Enter amount is deposit :"))
    if amount >0:
        balance += amount 
        transaction_history.append(f"Deposited ${amount:.2f}")
        print("Deposit successfull")
    else:
        print("Invalid amount")

def withdraw():
    global balance
    amount = float(input("Enter amount to Withdraw : $"))

    if amount <= 0:
        print("Invalid amount !")
    elif amount > balance:
        print ("Insufficient Balance !")
    else:
        balance -= amount
        transaction_history.append(f"Withdraw ${amount:.2f}")
        print("Withdrawal successfull !")

def show_transation():
        print(f"\ncurrent Balance : ${balance :.2f}")

    
def show_transaction():
    if len(transaction_history)==0:
            print("\nNo transation available.")
    else:
            print("\n ----Transaction History----")

            for transation in transaction_history:
                print("transaction")

    #Main program
while True:
        print("\n========Simple Banking Systen")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check")
        print("4.Transaction History")

        choice = input("Enter your choice (1-5):")
        if choice == "1":
         deposit()
        elif choice == "2":
             withdraw()
        
        elif choice == "4":
             show_transaction()
        elif choice =="5":
            print("\nThank you for using our Bank System!")
            break

        else:
             print("Invalid choice please try again!")

             
