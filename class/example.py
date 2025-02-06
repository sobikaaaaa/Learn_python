# class Animal:
#     def __init__(self):#constructor(It is automagically called whenever the class is instantiated.)
#         self.animal_name="Dog"
#         self.animal_color="Black"

#         print("object initialize") 
#     def sound(self): #method
#         print(self.animal_color)
#     def walk(self):
#         self.animal_name    

# animal=Animal() 
# animal.sound() 

class Car:
    def __init__(self,color,brand):
        self.color=color
        self.brand=brand
    def start(self):
        return f"The {self.color} {self.brand} car is starting"
my_car=Car("Black","Deepal") 
my_second_car=Car("Mint Green","BYD")    
print(my_car.color)  
print(my_car.brand)   
print(my_car.start())  
print(my_second_car.color)
print(my_second_car.brand)
print(my_second_car.start())


