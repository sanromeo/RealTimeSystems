#Лабораторна робота №3.1
#Системи реального часу
#Корсун Роман ІО-71

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.config import Config

Config.set('kivy', 'keyboard_mode', 'systemanddock')


def is_square(x):

    ''' Функція квадратного числа '''

    return (int(x ** 0.5)) ** 2 == x


def prime_number(n):

    ''' Функція простого числа '''

    a = 2
    while n % a != 0:
        a += 1
    return a == n


def ferma_factorize(n, counter=100):

    ''' Функція факторизації Ферма та обробка всіх випадків при введені числа '''

    if prime_number(n):
        return 1, n, 'Це просте число'

    if n <= 1:
        return None, None, 'Помилка: Число має бути більше 0'

    if n % 2 == 0:
        return None, None, 'Помилка: Число має бути непарне'

    if is_square(n):
        return int(n ** 0.5), int(n ** 0.5), 'Операція успішна!'

    x = int(n ** 0.5) + 1
    c = 0
    while not is_square(x * x - n):
        x += 1
        c += 1
        if c > counter:
            return None, None, 'Помилка! \nЗадачу не обраховано'
    y = int((x * x - n) ** 0.5)
    a, b = x - y, x + y
    return a, b, 'Операція успішна!'


class Container(GridLayout):

    ''' За допомогою класу Контейнер ми можемо заповните певне місце
     на екрані певним контентом або замінити цей контент на інший'''

    def calculation(self):

        ''' Функція ОБЧИСЛЕННЯ факторизації Ферма та обробка виключення при вводі букв або символів '''

        try:

            inp_number = int(self.text_input.text)
            a, b, c = ferma_factorize(inp_number, int(self.count_input.text))
            self.first_number.text, self.second_number.text, self.state_factorization.text = str(a), str(b), c

        except:
            self.state_factorization.text = 'Некоректний ввід'


class Lab3_1App(App):

    '''Ківі створює екземпляр підкласу App, він шукає файл .kv. Файл Lab3_1.kv обрано тому що назва підкласу
       App є Lab3_1App, з якого випливає що Ківі повинен намагатися завантажити файл Lab3_1.kv.'''

    def build(self):

        ''' Функція build() викликається коли програму запущено.
            Повертає Container як кореневий віджет з файлу Lab3_1.kv'''

        return Container()


if __name__ == "__main__":

    '''Запуск програми'''

    Lab3_1App().run()