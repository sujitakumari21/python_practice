# str1 = "Hello"
# len1 = print(len(str1))
# str2 = "Sujita"
# len2 = print(len(str2))
# final_str = str1+" "+str2
# print(final_str)
# print(len(final_str))



#INDEXING
str = "Hello chennai super kings"
# ch  = str[2]
# print(str)
# print(ch)        
#otherwise we can do like this 
# print(str ,str[0])
# print(str[3])


# SLICING
# str[starting_idx: ending_idx]   # slicing process
# str1 = "Today is special Day"
# str2 = "Python is an easy language"
# print(str2[0:7]) # 0 to 6
# print(str[0:len(str)]) # 0 to ending
# print(str1[0:]) # 0 to ensing

# str3 = "APPLE"
# print(str3[-5:-1])



# STRING FUNCTION
str = "i am studying python from Apnacollege"
# print(str.endswith("ege"))    # str.endswith("er.")    return true if string ends with substr
# print(str.endswith("Apna"))     # return flase if string doesnot ends with substr


# print(str.capitalize())  # Capitalized 1st char wuthout change in old str print both str changing or old
# print(str)
  
# str = str.capitalize()     # capitalized 1st char by changing in old str
# print(str)  


# print(str.replace("o","a"))    #replace all occurance of old
# print(str.replace("python","java"))
# print(str.replace("i am","you are"))

# print(str.find("o"))         # return 1st index of 1st occurer
# print(str.find("from"))
# print(str.find("q"))


# print(str.count("from"))     # count the occurrence of substr
# print(str.count("o"))


#PRACTICE QUESTION
#  1) WAP to input user's first name and print its length.
#  2) WAP to find the occurrence of "$" in a string.

# 1)
# name = input("Enter your name :")
# print("length of your name is",len(name))

# # 2)
# str = "Sujita $kumari is $1264"
# print(str.count("$"))


# CONDITIONAL STATEMENTS

# light = "Yellow"

# if(light=="REd"):
#     print("Stop")
# elif(light=="green"):
#     print("go")
# elif(light=="Yellow"):
#     print("Look")

# print("End of code")


# Age = 16
# if(Age>=18):
#     print("can vote")    #indentation fpr proper spacing instead of curly braces for combining the code
#     print("can drive")
# else:
#     print("can't vote")
#     print("can't drive")


# marks = 74

# if(marks>=90):
#     grade = 'A'
# elif(marks >= 80 and marks < 90):
#     grade = 'B'
# elif(marks >= 70 and marks < 80):
#     grade = 'C'
# else:
#     grade = 'D'
# print("grade of thr student ->",grade)



#take input and print the grade of student
# marks = int(input("Enter the marks of student :"))

# if(marks>=90):
#     grade = 'A'
# elif(marks >= 80 and marks < 90):
#     grade = 'B'
# elif(marks >= 70 and marks < 80):
#     grade = 'C'
# else:
#     grade = 'D'
# print("grade of the student ->",grade)
 

 #nesting
# age = 96

# if(age>=18):
#     if(age >=80):
#         print("cannot drive")
#     else:
#         print("can drive")

# else:
#     print('cannot drive')


#PRACTICE QUESTION

#WAP to check if a number entered by the user is odd or even

# number = int(input("Enter any number"))
# if(number%2==0):
#     print("even")
# else:
#     print("Odd")

#WAP to find the greatest of 3 numbers entered by the user.
# a = int(input("enter 1st number"))
# b = int(input("Enter the 2nd number"))
# c = int(input("enter the 3rd number"))
# if(a>b and a>c):
#     print("first number is largest",a)
# elif(b>a and b>c ):
#     print("Second numberr is largest",b)
# else:
#     print("third number is largest",c)


#WAP to check if a number is multiple of 7 or not.
num = int(input("Enter any  number : "))
if(num % 7 ==0):
    print("Number is multiple of 7")
else:
    print("Number is not multiple of 7")

#WAP to check the number is multiple of 8 or not.

num = int(input("Enter any number :"))
if(num % 8 ==0):
    print("number is multiple of 8")
else:
    print("number is not multiple of 8")

#WAP to check whether number is multiple of 10 or not.
num = int(input("Enter any number :"))
if(num % 10 == 0):
    print("Number is multiple of 10")
else:
    print("Number is not multiple of 10")
    






    