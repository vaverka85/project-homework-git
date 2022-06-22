class Mycalc:
    def __init__(self):
        self.func()
    def add(self):
        return self.x + self.y
    def subtract(self):
        return self.x - self.y
    def multiply(self):
        return self.x * self.y
    def sqrt(self):
        return self.x ** self.y
    def divide(self):
        if self.y == 0:
            return 'Ошибка деления на 0'
        else:
             return self.x / self.y
    def func(self):
        self.x = int(input('Введите первое число: '))
        self.y = int(input('Введите второе число: '))

while True:
    print('Введите знак операции: +,-,*,**,/')
    c = input()
    if c != '+' and c != '-' and c != '*' and c != '**' and c != '/':
        print('Ошибка. Выход из программы!')
        break
    print('Числа:')
    actions = Mycalc()
    if c == '+':
        print('Результат: ', actions.add())
    if c == '-':
        print('Результат: ', actions.subtract())
    if c == '*':
        print('Результат: ', actions.multiply())
    if c == '**':
        print('Результат: ', actions.sqrt())
    if c == '/':
        print('Результат: ', actions.divide())



