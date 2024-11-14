from animal import Animal
class Cat(Animal):

    legs = 4
    def __init__(self,name="",age=0): # constructor
        self.name = name 
        self.speak()
        #encapsulation = attribut privé
        self.__age = age
    
    def speak(self):
        print(self.name,"Miaou!")
        #print(self.__age) #impossible

    def get_age(self):
        # guetter / Accesseur
        if self.__age >50:
            return 'je dis pas'
        return self.__age
    
    def set_age(self,age):
        if isinstance(age,int) and age >0:
            self.__age = age
        else:
            print("Erreur")

