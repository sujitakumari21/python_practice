# name="Sujita Kumari"
# print(name)
# name="Shristi"
# print(name)

# x="Hello"  #Print and type is built in function
# print(type(x))
# x=100
# print(type(x))

#reassign- overwrite a variabble with a new value
# name="Suresh"   
# print(name)
# name="Tamesh"
# print(name)

# #calulate
# a=10
# b=20
# c=a+b          
# print(c)


#DATATYPE
# ab))=20 # int
# b="terah"#str
# c=2.0   #float
# d=True  #bool(T/F)
# h=None   #NoneType

# #Dyanamic Python re-detect

# a=None
# b=58.3
# print(type(a))  #Builtin function
# print(type(

# fruit =["apple","Mango","Orange"] # list
# print(fruit)

# nums = [1,2,3] #list
# pair =(1,2) # tuple
# uniq ={1,2,3} #set
# info = {"a":1}  #dict
# print(type(info))

# 1. Escape  - use\ before the inner quote
# print("Hi\"Python\"")

# #2 Mix quote type  - outer single , inner double(vice versa)
# print("Hi 'Python'")

# #3 triple quote  preserve line breaks
# print("""Hi
 
#  python""")

#Built - in functions INPUT & OUTPUT
# name =input("Enter a name :")
# print(name)
# age =input("Enter your age :")

#PRINT FUNCTION
# print("Sujita loves kurkure")

# #Multiple value
# print("sum=",10+89)
# print("Done!")

#print()
# total_qty=35
# price=100
# revenue=price*total_qty
# print(revenue)

# print("""learning path :
#  -python basics
#  -data engineering
#  -AI engineering""")

# name =input("Enter your name :")
# print("Hello", name)

# #Read a number
# age =int(input("Your age :"))
# print("Next year:",age+1)


# Functions and Methods
# text = "Manish"
# num=90
#  # Function - work on either
# print(type(text))
# print(len(text))
#  # Method
# print(text.upper())
# print(num.bit_length)

# #Without  variable
# print("My name id sujita :")
# print("Sujita loves Python")

# #with Variables
# name = "Sujita"
# language = "Python"
# print(f"My name is {name}")
# print(f"{name} loves {language}")

# print("Line1\nLine2")
# print("Hi\tEveryone")
# print("Path:C:\\Users")
# print("She said \"Hi\"")

# print("C:\\Users\\sujita kumari\\Desktop\\python")

# date ="2026/05/10"
# print(date.replace("/","-")) # using .replace() method to update format of ant thing

# first= "Manish";last = "Raj"
# print(f"{first}{last}")

# csv = "Manish,25,USA"
# print(csv.split(","))  # using .split() method 

# print("="*20)

# code = "Manish-25"
# print(code[0])  #M
# print(code[-1])  #5
# print(code[0:6]) #Manish
# print(code[-2]) #25

# date ="2026-05-29"
# print(date[0:4],date[5:7],date[-2:])

# print(code[0:9:2])


# name ="Manish"
# print(name.strip())
# print(name.lstrip())
# print(name.rstrip())

# #Strip specific chars
# print("$Manish$".strip("$"))

# #Case insensitive 







phone = "+48-176-12345"
print(phone.startswith("+48"))

file="data_backup.csv"
print(file.endswith(".csv"))

email="manish@gmail.com"
print(email.find("@"))
print("@"in email)

#user find() to slice dyanamically
print(phone[phone.find("-")+1:])



#VALIDATION
# a ="name"
# b="12"
# print(a.isalpha)    # isalpha and isnumeric both are used for string
# print(b.isnumeric)