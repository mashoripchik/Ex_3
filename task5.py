# 5 Создать класс Animal и определить в нем метод make_a_sound(). Метод должен вывоводить строку "Издает звук"
# Cоздать классы Cat и Dog с методами scratch() и dig() соответственно. # Метод scratch должен выводить строку "Царапать мебель".
# Метод dig должен выводить строку "Рыть землю". # в классах Cat и Dog переопределите метод make_a_sound() базового класса Animal.
# (Cat: make_a_sound() -> '<...>', Dog: make_a_sound() -> '<...>')
class Animal:
    def make_a_sound(self, sound):
        self.sound = sound
        print(f'Издает звук {sound}')
        return sound

class Cat(Animal):
    def scratch(self):
        print('Царапать мебель')
    default_sound = 'Мяу'
    def make_a_sound(self, sound = None):
        super().make_a_sound(Cat.default_sound)

class Dog(Animal):
    def dig(self):
        print('Рыть землю')
    default_sound = 'Гав'
    def make_a_sound(self, sound = None):
        super().make_a_sound(Dog.default_sound)
scr = Cat()
dig = Dog()
snd_dog = Dog()
snd_cat = Cat()
scr.scratch()
snd_cat.make_a_sound()
dig.dig()
snd_dog.make_a_sound()

