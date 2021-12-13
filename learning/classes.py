class Man:

    def __init__(self, name):
        self.name = name
   
    def __del__(self):
        print(self.name, 'is deleted')

    def disp_info(self):
        print('hi', self.name) #self it is how this in JS

a = Man("miki")

a.disp_info()


class Person:
    def __init__(self, name):
        self.__name = name      # устанавливаем имя
        self.__age = 1          # устанавливаем возраст
 
    def set_age(self, age):
        if age in range(1, 100):
            self.__age = age
        else:
            print("Недопустимый возраст")
 
    def get_age(self):
        return self.__age
         
    def get_name(self):
        return self.__name
 
    def display_info(self):
        print("Имя:", self.__name, "\tВозраст:", self.__age)
         
tom = Person("Tom")
 
tom.display_info()          # Имя: Tom  Возраст: 1
tom.set_age(-3486)          # Недопустимый возраст
tom.set_age(25)
tom.display_info()          # Имя: Tom  Возраст: 25



##############################################################



class Person1:
    def __init__(self, name):
        self.__name = name  # устанавливаем имя
        self.__age = 1      # устанавливаем возраст
 
    @property
    def age(self):
        return self.__age
 
    @age.setter
    def age(self, age):
        if age in range(1, 100):
            self.__age = age
        else:
            print("Недопустимый возраст")
     
    @property
    def name(self):
        return self.__name
         
    def display_info(self):
        print("Имя:", self.__name, "\tВозраст:", self.__age)
         
         
tom = Person1("Tomi")
 
tom.display_info()      # Имя: Tom  Возраст: 1
tom.age = -3486         # Недопустимый возраст
print(tom.age)          # 1
tom.age = 36
tom.display_info()      # Имя: Tom  Возраст: 36


class Employee(Person):
 
    def details(self, company):
        # print(self.__name, "работает в компании", company) # так нельзя, self.__name - приватный атрибут
        print(self.name, "работает в компании", company)
 
 
# tomm = Employee("Tom", 23)
# tomm.details("Google")
# tomm.age = 33
# tomm.display_info()