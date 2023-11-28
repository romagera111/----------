#Инкапсуляция
#Инкапсуляция в Python - это принцип объектно-ориентированного программирования, который позволяет упаковать данные и методы,
#работающие с этими данными, внутри одного объекта. Простыми словами, это означает "упаковку" данных и кода в единый блок.
class Cat():
  def __init__(self, breed, color, age):
     self._breed = breed
     self._color = color
     self._age = age

  @property
  def breed(self):
    return self._breed
    
  @property
  def color(self):
    return self._color
    
  @property
  def age(self):
    return self._age
  
  @age.setter
  def age(self, new_age):
    if new_age > self._age:
      self._age = new_age
    return self._age

cat = Cat('Абиссинская', 'Рыжая', 4)
print(cat.breed) # Абиссинская
print(cat.color) # Рыжая
cat.age = 5
print(cat.age) # 4

#Наследование
#создание нового класса, который будет использовать характеристики и функциональность уже существующего класса.
class HomeCat(Cat):
  def __init__(self, breed, color, age, owner, name):
    super().__init__(breed, color, age)
    self._owner = owner
    self._name = name
  
  @property
  def owner(self):
    return self._owner
    
  @property
  def name(self):
    return self._name
  
  def getTreat(self):
    print('Мяу-мяу')
  def purr(self):
    print('Мрррр')

my_cat = HomeCat('Сиамская', 'Белая', 3, 'Иван', 'Роза')
print(my_cat.owner)
print(my_cat.breed)
my_cat.getTreat() # Мяу-мяу
my_cat.purr() # Мрррр


#Полиморфизм
#Этот принцип позволяет применять одни и те же команды к объектам разных классов, даже если они выполняются по-разному.
class Cat:
  def sleep(self):
    print('Свернулся в клубок и сладко спит.')

class Parrot:
  def sleep(self):
    print('Сел на жёрдочку и уснул.')

def homeSleep(animal):
  animal.sleep()

cat = Cat()
parrot = Parrot()
homeSleep(cat) # Свернулся в клубок и сладко спит.
homeSleep(parrot) # Сел на жёрдочку и уснул.

#Абстракция
#абстракция позволяет представить сложные системы или объекты с более простой, высокоуровневой точки зрения.
class Predator:
  def hunt(self):
    print('Охотится...')
class Cat(Predator):
  def __init__(self, name, color):
     super().__init__()
     self._name = name
     self._color = color

  @property
  def name(self):
    return self._name

  @property
  def color(self):
    return self._color
  
cat = Cat('Даниэла', 'Чёрный')
cat.hunt() # Охотится…

#Изменения для гитхаб