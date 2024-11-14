from animal import Animal
class Dog(Animal):
    def __init__(self,name):
        self.name = name

    def speak(self):
        print(self.name,"Woof!")

if __name__ == "__main__":
    # Ne s'execute que si dog.py est le fichier principal
    my_dog = Dog("Chien")
    my_dog.speak()

