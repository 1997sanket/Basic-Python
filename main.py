#To print
print("Hello World !")

#List
list = ["mobile", "chair"]
print("List = ", list)



#Tuples (values cannot change)
tuple = (10, 20, 30)
#tuple[0] = 100    gives error
print(tuple[0])



#Dictionary(Map)
map = {"Sanket" : 23,
       "Sonal" : 21,
       "Bhau" : 33 }
print(map)
print(map["Bhau"])
print(map.keys())
print(map.values())



#Taking input and if else logic
print("Enter marks")
#marks = int(input())   #if we don't specify int, the input will be considered String

#if(marks>90) :
#    print("A grad")
#elif(marks > 70) :
#    print("B grade")
#else :
#    print("C grade")




#For loop
for i in range(0, 10) :
    print(i, end=" ")
print()

#Iterating a list
list = [1, 2, 3]
for i in list:
    print(i)



#While loop
i = 5
while(i<10) :
    print(i)
    i = i + 1



#Function
def sum(x,y):
    return x+y

print("Sum = ",sum(10,20))




#OOP

#class
class Employee:
    __name = None
    __salary = 0

    #Constructor
    def __init__(self, __name, __salary):
        self.__name = __name
        self.__salary = __salary

    def getName(self):
        return self.__name

    def getSalary(self):
        return self.__salary


#reference and object
sanket = Employee("Sanket", 800000)
print(sanket.getName())
print(sanket.getSalary())








