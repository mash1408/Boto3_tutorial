# import csv    
# with open('sample1.csv') as csv_file:    
#     csv_reader = csv.reader(csv_file, delimiter=',')    
#     line_count = 0    
#     for row in csv_reader:    
#         if line_count == 0:    
#             print(f'Column names are {", ".join(row)}')    
#             line_count += 1   
# for calendar operations
# import calendar
   
# # using calendar to print calendar of year
# # prints calendar of 2018
# print ("The calendar of year 2018 is : ")
# print (calendar.calendar(2018, 2, 1, 6))

# class MyError(Exception):
 
#     # Constructor or Initializer
#     def __init__(self, value):
#         self.v = value
 
 
 
# try:
#     raise(MyError(3*2))
 
# # Value of Exception is stored in error
# except MyError as e:
#     print('A New Exception occurred: ', e.v)


# from codecs import IncrementalDecoder


# class Hologram:
#     def __init__(self,id,name):
#        self.id=id
#        self.name=name

# class AR(Hologram):
#     def __init__(self,id,name):
#         # self.correspondance=correspondance
#         super().__init__(id,name)
# def main():
#     spark=Hologram(2,'Spark')
#     make=AR('MAKE',5)
#     print(str(isinstance(make,Hologram)))

# if __name__=='__main__':
#         main()


# class Pet:
#         #__init__ is an constructor in Python
#         def __init__(self, name, age):     
#                 self.name = name
#                 self.age = age
  
# # Class Cat inheriting from the class Pet
# class Cat(Pet):         
#         def __init__(self, name, age):
#       
#                 super().__init__(name, age) 
  
# def Main():
#         thePet = Pet("Pet", 1)
#         jess = Cat("Jess", 3)
          
#         # isinstance() function to check whether a class is 
#         # inherited from another class
#         print("Is jess a cat? " +str(isinstance(jess, Cat)))
#         print("Is jess a pet? " +str(isinstance(jess, Pet)))
#         print("Is the pet a cat? "+str(isinstance(thePet, Cat)))
#         print("Is thePet a Pet? " +str(isinstance(thePet, Pet)))
#         print(jess.name)
  
# if __name__=='__main__':
#         Main()


# class Pet:
#     names=[]
#     __hiddenVar=0
#     classVar=0    

#     def __init__ (self,name):
#         self.name = name
#         self.__hello="jhjk"
#         Pet.names.append(self.name)
#         self.__hiddenVar+=7
#         self.classVar+=9

#     def display(self):
#         print(self.__hello)
#         print(self.__hiddenVar)
#         print(self.classVar)
#         print(Pet.__hiddenVar)

#     @classmethod
#     def hiddenMethod(cls,increment):
#         cls.__hiddenVar+=increment


# cat=Pet("bob")
# print(cat.__class__.names)
# Pet.hiddenMethod(50)

# cat.display()


# class CSStudent:
#     stream = 'cse'     # Class Variable
#     def __init__(self, name, roll):
#         self.name = name
#         self.roll = roll
 
# Driver program to test the functionality
# # Creating objects of CSStudent class
# a = CSStudent("Geek", 1)
# b = CSStudent("Nerd", 2)
 
# print ("Initially")
# print ("a.stream =", a.stream )
# print ("b.stream =", b.stream )
 
# # This thing doesn't change class(static) variable
# # Instead creates instance variable for the object
# # 'a' that shadows class member.
# a.stream = "ece"
 
# print ("\nAfter changing a.stream")
# print ("a.attributes =", vars(a) )
# print ("b.attributes =", vars(b) )

# x = [int(x) for x in input("Enter two values: ").split()]
# for i in x:
#     print(i, end ="\t")


# import random
# secret_number = random.randint(1,500)
# print ("Pick a number between 1 to 500")
# while True:
#     res = input("Guess the number: ")
#     if res==secret_number:
#         print ("You win")
#         break
#     else:
#         print ("You lose")
#         continue


print("hello", "this", "is","me",sep="_",end="_____")
print("Google this",end="/")