question 1.
string = "Python is a case sensitive language"

# a.
print(len(string)) 

# b.
print(string[::-1]) 

# c.
new = string[10:27]
print(new) 

# d. 
print(string.replace("a case sensitive", "object oriented"))

# e. 
print(string.index("a"))

# f.
print(string.replace(" ", ""))

Python 3.9.10 (tags/v3.9.10:f2f3f53, Jan 17 2022, 15:14:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
= RESTART: C:\Users\Aakash Arora\OneDrive - pec.edu.in\Desktop\Assignments PEC\PYTHON\Assignment_2\Assignment_2_que_1_.py
35
egaugnal evitisnes esac a si nohtyP
a case sensitive 
Python is object oriented language
10
Pythonisacasesensitivelanguage
>>> 




question 2.
name = "Aakash" 
SID = 20105003 
cgpa = 9.9 
department = "ECE" 

print("""Hey, {} Here!
My SID is {}
I am from {} department and my cgpa is {}""".format(name, SID, department, cgpa))  

Python 3.9.10 (tags/v3.9.10:f2f3f53, Jan 17 2022, 15:14:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
= RESTART: C:\Users\Aakash Arora\OneDrive - pec.edu.in\Desktop\Assignments PEC\PYTHON\Assignment_2\Assignment_2_que_2_.py
Hey, Aakash Here!
My SID is 20105003
I am from ECE department and my cgpa is 9.9
>>> 




question 3.
a = 56
b = 10 

# a. 
print(a & b) 

# b. 
print(a | b) 

# c. 
print(a ^ b) 

# d.
print(a << 2) 
print(b << 2)

# e.
print(a << 4) 
print(b << 4) 

Python 3.9.10 (tags/v3.9.10:f2f3f53, Jan 17 2022, 15:14:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
= RESTART: C:\Users\Aakash Arora\OneDrive - pec.edu.in\Desktop\Assignments PEC\PYTHON\Assignment_2\Assignment_2_que_3_.py
8
58
50
224
40
896
160
>>> 




question 4.
num1 = int(input())
num2 = int(input())
num3 = int(input()) 

if (num1 >= num2) and (num1 >= num3):
   largest = num1
elif (num2 >= num1) and (num2 >= num3):
   largest = num2
else:
   largest = num3

print("The largest number is", largest)

Python 3.9.10 (tags/v3.9.10:f2f3f53, Jan 17 2022, 15:14:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
= RESTART: C:\Users\Aakash Arora\OneDrive - pec.edu.in\Desktop\Assignments PEC\PYTHON\Assignment_2\Assignment_2_que_4_.py
7
8
10
The largest number is 10
>>> 




question 5.
a = list(input().split())
b = 0

for i in a:
    if i == 'name':
        b = b + 1 

if b > 0:
    print("YES")
else:
    print("NO") 

Python 3.9.10 (tags/v3.9.10:f2f3f53, Jan 17 2022, 15:14:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
= RESTART: C:\Users\Aakash Arora\OneDrive - pec.edu.in\Desktop\Assignments PEC\PYTHON\Assignment_2\Assignment_2_que_5_.py
my name is aakash.
YES
>>> 




question 6.
def is_triangle(a, b, c):
    if a > (b+c) or b > (a+c) or c > (a+b):
        print("NO")

    else:
        print("YES")

a = int(input("First side of triangle: "))
b = int(input("Second side of triangle: "))
c = int(input("Third side of triangle: ")) 
is_triangle(a, b, c) 

Python 3.9.10 (tags/v3.9.10:f2f3f53, Jan 17 2022, 15:14:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
= RESTART: C:\Users\Aakash Arora\OneDrive - pec.edu.in\Desktop\Assignments PEC\PYTHON\Assignment_2\Assignment_2_que_6_.py
First side of triangle: 7
Second side of triangle: 8
Third side of triangle: 9
YES
>>> 
