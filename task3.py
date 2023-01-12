# 3 Создайте класс IceCream (для заказа мороженого с добавкой или без),
# принимающий 1 аргумент при инициализации (отвечающий за добавку к мороженому).
# В этом классе реализуйте метод info_about_icecream(), выводящий на печать «Мороженное и {ДОБАВКА}»
# в случае наличия добавки, а иначе отобразится следующая фраза: «Обычное мороженое».

class IceCream:
    def __init__(self, dobavka = None):
        if isinstance(dobavka, str):
            self.dobavka = dobavka
        else:
            self.dobavka = None
    def info_about_icecream(self):
        if self.dobavka:
            print(f'Мороженое и {self.dobavka}')
        else:
            print('Обычное мороженое')

ice = IceCream(input("Выберите добавку или отправьте пустую строку: "))
ice.info_about_icecream()
