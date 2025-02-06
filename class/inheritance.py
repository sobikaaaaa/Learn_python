class Animal:
    def __init__(self,name,breed,color):
        self.name=name
        self.color=color
        self.breed= breed
    def sound(self):
        return "some generic sound"  
class Dog(Animal):
    def __init__(self, name, breed,color):
        self.name="Lucky"
        super().__init__(name,breed,color)

        self.breed=breed
        self.color="white"
    def get_info(self):

        return f"{self.name} is {self.breed} with color {self.color}"
    # def speak(self):
    #     return self.sound()
    def sound(self):
        return "Bark"
        
dog=Dog("Entertainment","Golden Retriever","Black")
print(dog.get_info())
print(dog.sound())