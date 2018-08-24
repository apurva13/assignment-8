'''
Q.1- Create a circle class and initialize it with radius.
Make two methods getArea and getCircumference inside this class.
'''

class circle:
    def __init__(self,radius):
        self.r=radius
    def getArea(self):
        self.area=3.14*(self.r**2)
        return self.area
    def getCircumference(self):
        self.cir=2*3.14*self.r
        return self.cir
radius=int(input("Enter radius:"))
c=circle(radius)
print("Area of circle is:",c.getArea())
print("Circumference of circle is:", c.getCircumference())

'''
Q.2- Create a Student class and initialize it with name and roll number.
Make methods to : 
1. Display - It should display all informations of the student. 
2. setAge - It should assign age to student
3. setMarks - It should assign marks to the student.
'''
class Student:
    def __init__(self,name,roll):
        self.name=name
        self.roll=roll
    def setAge(self,age):
        self.age=age
    def setMarks(self,marks):
        self.marks=marks
    def display(self):
        print("Name:",self.name)
        print("Roll No.:",self.roll)
        print("Age:",self.age)
        print("Marks:",self.marks)
name=input("Enter Name Of Student:")
roll=int(input("Enter Roll No. Of Student:"))
age=int(input("Enter Age Of Student:"))
marks=int(input("Enter Marks Of Student:"))
s1=Student(name,roll)
s1.setAge(age)
s1.setMarks(marks)
s1.display() 
'''
Q.3- Create a Temprature class and create two methods: 
1. convertFahrenheit - It will take celsius and will print it into Fahrenheit. 
2. convertCelsius - It will take Fahrenheit and will convert it into Celsius.
'''
class Temperature:
    def convertFahrenheit(self,cel):
        fah=((cel*9)/5)+32
        return fah
    def convertCelsius(self,fah):
        cel=(fah-32)/1.8
        return cel
temp=Temperature()
tcel=int(input("Enter Celsius Temperature: "))
tfah=int(input("Enter Fahrenheit Temperature: "))
f=temp.convertFahrenheit(tcel)
c=temp.convertCelsius(tfah)
print(tcel,"Celsius to Fahrenheit:",f)
print(tfah,"Fahrenheit to Celclius:",c) 

'''
Q.4- Create a class MovieDetails and initialize it with artistname,Year of release and ratings . 
#Make methods to 
#1. Display-Display the details. 
#2. Add- Add the movie details.
'''
class MovieDetails:
    def __init__(self,name,year,rating):
        self.artistname=name
        self.release=year
        self.rating=rating        
    def Add(self,movie):
        self.movie=movie
    def Display(self):
        print("Artist Name:",self.artistname)
        print("Year of release:",self.release)
        print("Rating:",self.rating)
        print("Movie Name:",self.movie)
           
name=input("Enter the Artist Name:")
year=int(input("Enter Release Year:"))
rating=int(input("Enter Rating:"))
movie=input("Enter Movie Name:")
detail=MovieDetails(name,year,rating)
detail.Add(movie)
detail.Display()

'''
Q.5- Create a class Animal as a base class and define method animal_attribute.
Create another class Tiger which is inheriting Animal and access the base class method.
'''
class Animal:
    def animal_attribute(self):
        print("Attribute:Tiger")
class Tiger(Animal):
    def tiger_attr(self):
        print("Child Class")
a=Animal()
t=Tiger()
t.animal_attribute()

'''
Q.6- What will be the output of following code.

class A:
    def f(self):
        return self.g()
    def g(self):
        return 'A'
class B(A):
    def g(self):
        return 'B'

a = A()
b = B()
print (a.f(), b.f())
print (a.g(), b.g())
'''
    
'''
The output will be:
A B
A B
when in code the print statement will be like below else invlaid Syntax
print (a.f(), b.f()) 
print (a.g(), b.g())

a.f() calls function def f(self) of class A which calls def g(self) which returns A
b.f() calls function def f(self) of class B which calls def g(self)which returns B
a.g() and b.g() will call def g(self) of class A and B respectively.
'''


'''
Q.7- Create a class Shape.Initialize it with length and breadth Create the method Area.
Create class rectangle and square which inherits shape and access the method Area.
'''
class Shape:
    def __init__(self,l,b):
        self.length=l
        self.breadth=b
    def area(self):
        self.area=self.length*self.breadth
        return self.area
class rectangle(Shape):
    def __init__(self,l,b):
        self.length=l
        self.breadth=b
class square(Shape):
    def __init__(self,a):
        self.length=a
        self.breadth=a
l=int(input("Enter length of rectangle:"))
b=int(input("Enter breadth of rectangle:"))
a=int(input("Enter size of square:"))
r=rectangle(l,b)
s=square(a)
print("Area of rectangle:",r.area())
print("Area of Square:",s.area())

