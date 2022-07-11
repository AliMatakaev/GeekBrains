class Error:
    def __init__(self, *args):
        self.my_list = []

    def my_input(self):
        while True:
            try:
                val = int(input('Введите данные и нажмите Enter - '))
                self.my_list.append(val)
                print(f'Текущий список - {self.my_list} \n ')
            except:

                print(f"Допустимы только числовые данные")
                user_input = input(f'Введите данные. Для выхода введите "stop" ')

                if user_input == 'stop':
                    print(f'Вы вышли. Текущий список - {self.my_list} \n ')
                    break


try_except = Error(1)
print(try_except.my_input())

