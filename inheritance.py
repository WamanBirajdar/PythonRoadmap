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
