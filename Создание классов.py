class Drink:

    
    # Определяем статический атрибут.
    _volume = 200
    
    # Вызываем инициализатор класса и определяем динамические атрибуты.
    def __init__ (self, name, price):
        self.name = name 
        self.price = price
        self._remains = self._volume
    
    # Просим друга сообщить информацию о напитке.
    def drink_info (self):
        print (f'Название: {self.name}. Стоимость: {self.price}. Начальный объём: {self._volume}. Осталось: {self._remains}')
    
    def tell_price (self):
        print (f'Друг объявляет стоимость своего напитка')
        return self.price

    # Служебный метод, позволяющий узнать, достаточно ли напитка.
    def _is_enough (self, need):
        if self._remains >= need and self._remains > 0:
            return True
        print ('Осталось недостаточно напитка')
        return False
    
    # Говорим другу сделать глоток.
    def sip (self):
        if self._is_enough(20) == True:
            self._remains -= 20
            print ('Друг сделал глоток')
            
    # Говорим другу сделать маленький глоток.
    def small_sip (self):
        if self._is_enough(10) == True:
            self._remains -= 10
            print ('Друг сделал маленький глоток')
    
    # Говорим другу выпить напиток залпом.
    def drink_all (self):
        if self._is_enough(0) == True:
            self._remains = 0
            print ('Друг выпил напиток залпом')


class Juice (Drink):

    # Определяем статический атрибут.
    _juice_name = 'сок'    

    # Вызываем инициализатор класса и определяем динамические атрибуты.
    def __init__ (self, price, taste):
        super().__init__ (self._juice_name, price)
        self.taste = taste
        
    # Переопределяем родительский метод drink_info, чтобы он сообщал нам информацию о вкусе сока.
    def drink_info (self):
        print (f'Вкус сока: {self.taste}. Стоимость: {self.price}. Начальный объём: {self._volume}. Осталось: {self._remains}')



tea = Drink ('чай', 500)
print (tea.tell_price()) # Сначала друг объявит стоимость чая.
beetlejuice = Juice (1988, 'жучиный')
print (beetlejuice.tell_price()) # Потом друг объявит стоимость жучиного сока.

#Изменения для github
