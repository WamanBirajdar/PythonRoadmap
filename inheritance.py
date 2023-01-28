# inheritance is mechanism to inherited properties and variables or objects of parent class to child class
# types of inheritance are
# 1. single inheritance
# 2.multilevel inheritance

# program to demonstrate inheritance
class person:

    # constructor when i created instance of person class automaticall constructoor called 
    def __init__(self,name,id) -> None:
        self.name=name
        self.id=id

    def prinln(self):
        print('my name is ',self.name)
        print('my id is',self.id)




# child class which is inherited variablse adn methods of parent class

class emp(person):
    def prin(self):
        print("EMp class called")

# created child class object
emp=emp('mayank',103)

# calling parent class print function
emp.prinln()

#calling child class print function
emp.prin()



# demonstrate parent constructor
# parent class
class person:

    # constructor
    def __init__(self,name,idnumber) -> None:
        self.name=name
        self.idnumber=idnumber

    def disply(self):
        print(self.name)
        print(self.idnumber)


# child class
class employee(person):

    #child class constructor

    def __init__(self,name, post,salary, idnumber) -> None:
        self.salary=salary
        self.post=post
        super().__init__(name, idnumber)
    

    


# creating object class or instance of child class

a = employee('Rahul', 886012, 200000, "Intern")
# calling function of parent class
a.println()
print(a.name)



# types of inhertance 
# 1. single inheritance


class base1:
    def __init__(self) -> None:
        self.str1='geeks1'
        print("base1")


class base2:
    def __init__(self) -> None:
        self.str2='geeks2'
        print('base 2')


class derived(base1,base2):

    def __init__(self) -> None:
        base1.__init__(self)
        base2.__init__(self)
    def printstr(self):
        print(self.str1,self.str2)


obj=derived()
obj.printstr()




# 2. multilevel inheritnace 
# child class inheritance from multiple parent classes

class Base:
    # constructor
    def __init__(self,name) -> None:
        self.name=name


    # to get name
    def getname(self):
        return self.name


class child(Base):
    # child consructor

    def __init__(self, name,age) -> None:
        Base.__init__(self,name)# caaling parent consttuctor
        self.age=age

    # to get age
    def gettage(self):
        return self.age


        
class grandchild(child):
    def __init__(self, name, age,address) -> None:
        super().__init__(name, age)
        self.address=address


    # get address
    def getaddress(self):
        return self.address


g=grandchild('waman',23,'noida')
print(g.getname(),g.gettage(),g.getaddress())



# examples of inheritance 

# example of single inheritance
class base:
    def __init__(self,name) -> None:
        self.name=name


    # get name 
    def getname(self):
        return self.name

class child(base):
    def __init__(self, name,age) -> None:
        super().__init__(name)
        self.age=age

    # get age of person
    def getage(self):
        return self.age

single_inheritance=child('waman',22)
print(single_inheritance.getname(),single_inheritance.getage())


# example of multiple inheritance
# derived class inheritas from more than one base class

# base class1
class mother:
    mothername=""

    def mother(self):
        print(self.mothername)

# base class 2
class father:
    fathername=" "

    def father(self):
        print(self.fathername)

# derived class

class son(mother,father):
    def parents(self):
        print(self.mothername)
        print(self.fathername)

s=son()


# Python program to demonstrate
# multiple inheritance
# derived class inherits properties and variables from more than one base class
 
# Base class1
class Mother:
    mothername = ""
 
    def mother(self):
        print(self.mothername)
 
# Base class2
 
 
class Father:
    fathername = ""
 
    def father(self):
        print(self.fathername)
 
# Derived class
 
 
class Son(Mother, Father):
    def parents(self):
        print("Father :", self.fathername)
        print("Mother :", self.mothername)
 
 
# Driver's code
s1 = Son()
s.fathername = "RAM"
s.mothername = "SITA"
s.parents()


# multilevel inheritance
# features of base class and derived class are inherited into the new derived class
# child and grandmother


# base class
class grandfather:

    def __init__(self,grandfathername) -> None:
        self.grandfathername=grandfathername


# intermediate class
class father(grandfather):
    def __init__(self,fathername, grandfathername,) -> None:
        
        # invoking constructor of grandfather
        super().__init__(grandfathername)
        self.fathername=fathername


#derived class


class son(father):
    def __init__(self, sonname,fathername, grandfathername) -> None:
        super().__init__(fathername, grandfathername)
        self.sonname=sonname

    def display(self):
        print("grandfather name",self.grandfathername)
        print("father name",self.fathername)
        print("sonname",self.sonname)


# deriver code


s=son("wmaan",'balaji','Waaman')
s.display()



# hierarchical inheritance
# more than one derived classes created from one base class
# one parent class and two parent class


class baap:
    def fun(self):
        print("ye mera beta hai")

class child1(baap):
    def fun2(self):
        print("child 1")

class child2(baap):
    def fun(self):
        print("child2")


o1=child1()
o1.fun()
o1.fun2()


