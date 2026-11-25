""" class Person: def display(self): print("Name: Omkar") print("Age: 21") class Student(Person): def show(self): print("Course:Python") s = Student() s.display() s.show() """

""" class Animal: def sleep(self): print("Animal is sleeping") class Cat(Animal): def meow(self): print("Cat is Meowing") c = Cat() c.sleep() c.meow() """              

""" class Vehicle: def details(self): print("Brand:Maruti Suzuki") print("Model: Swift Dzire") class Car(Vehicle): def color(self): print("Color: Purl White") c = Car() c.details() c.color() """

""" class Mobile: def show(self): print("Brand: Samsung") print("Model: A36") print("Price: 34000") class Smartphone(Mobile): def storage(self): print("Storage: 256GB") s=Smartphone() s.show() s.storage() """

""" class Vehicle: def show(self): print("This is a vehicle") class Car(Vehicle): def car(self): print("This is a car") class Bike(Vehicle): def bike(self): print("This is a bike") c = Car() b = Bike() c.show() c.car() b.show b.bike() """

""" class College: def college(self): print("College: Agasti College") print("Location: Akole") class Student(College): def student_details(self): print("Roll Number: 36") print("Course: BCS") s = Student() s.college() s.student_details() """

""" class Book: def details(self): print("Title: Python") print("Author: John") class LibraryBook(Book): def book_id(self): print("Book ID: 111") b=LibraryBook() b.details() b.book_id() """

""" class ElectronicDevice: def power_on(self): print("Device is ON") class Laptop(ElectronicDevice): def laptop_details(self): print("Brand: HP") print("RAM: 8GB") l=Laptop() l.power_on() l.laptop_details() """    

""" class Father: def show_father(self): print("Father: Atmaram") class Mother: def show_mother(self): print("Mother: Ujwala") class Child(Father,Mother): def show_child(self): print("Child: Omkar") c =Child() c.show_father() c.show_mother() c.show_child() """

""" class Bank: def bank_name(self): print("Bank: HDFC") class Account(Bank): def account_details(self): print("Account Number: 9991") print("Holder: Omkar") a = Account() a.bank_name() a.account_details() """

""" class Person: def name(self): print("Name: Omkar") class Teacher(Person): def subject(self): print("Subject: MCS") t= Teacher() t.name() t.subject() """

""" class Fruit: def color(self): print("Color: Yellow") class Mango(Fruit): def taste(self): print("Taste: Sweet") m = Mango() m.color() m.taste() """

""" class Player: def name(self): print("Player: Virat") class Cricket(Player): def game(self): print("Game: Cricket") c= Cricket() c.name() c.game() """

""" class Animal: def sound(self): print("Animal sound") class Tiger(Animal): def sound(self): print("Roar") d = Tiger() d.sound() """

""" class Father: def __init__(self): print("Father class") class Son(Father): def _init__(self): super().__init__() print("Son class") s = Son() """