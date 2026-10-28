Python 3.14.2 (tags/v3.14.2:df79316, Dec  5 2025, 17:18:21) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> print("Hello_World")
Hello_World
>>> print("I am a student")
I am a student
>>> print(i am a student)
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> print(25)
25
>>> name = "suji"
>>> print(name)
suji
>>> print(name*3)
sujisujisuji
>>> print(name  *  100)
sujisujisujisujisujisujisujisujisujisujisujisujisujisujisujisujisujisujisujisujisujisujisujisujisujisujisujisujisujisujisujisujisujisujisujisujisujisujisujisujisujisujisujisujisujisujisujisujisujisujisujisujisujisujisujisujisujisujisujisujisujisujisujisujisujisujisujisujisujisujisujisujisujisujisujisujisujisujisujisujisujisujisujisujisujisujisujisujisujisujisujisujisujisujisujisujisujisujisujisuji
>>> print(name**2)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    print(name**2)
TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'int'
>>> name =  "Sujita"
>>> course = "python"
>>> college = "GGSESTC"
>>> print(name , course, college)
Sujita python GGSESTC
>>> print(name \n , course\n, college)
SyntaxError: unexpected character after line continuation character
>>> print(name\n course\n college)
SyntaxError: unexpected character after line continuation character
>>> print(name\n ,course\n, college)
SyntaxError: unexpected character after line continuation character
>>> print(name/n course/n college)
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> print(name/n, course/n, college)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    print(name/n, course/n, college)
NameError: name 'n' is not defined
>>> print(name + "\n" + course + "\n" + str(college))
Sujita
python
GGSESTC
>>> print(name + "\n" + course + "\n" + college)
Sujita
python
GGSESTC
print(name  "\n"  course  "\n"  college)
SyntaxError: invalid syntax. Is this intended to be part of the string?
print(name + "\n" + course + "\n" + college)

Sujita
python
GGSESTC
print(f"Name is: {name}\ncourse is:{course}\ncollege is:{college}")
Name is: Sujita
course is:python
college is:GGSESTC
print("python\njava")
python
java
print("suji\nkumari\nyadav")
suji
kumari
yadav
print("Name is :", name \n "course is : ",course\n "college is :", college)
SyntaxError: unexpected character after line continuation character
print("Name is :", name\n "course is : ",course\n "college is :", college)
SyntaxError: unexpected character after line continuation character
print(f"Name is : {name}\n course is : {course}\n college is :{college}")
Name is : Sujita
 course is : python
 college is :GGSESTC
print("Hello\n" + name)
Hello
Sujita
name = "bantu"
age = 1
print(f"Name : {name}\nAge :{age}")
Name : bantu
Age :1
print(name + "\n" + str(age))
bantu
1
print(name + "\n" + age)
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    print(name + "\n" + age)
TypeError: can only concatenate str (not "int") to str

print(name>college)



