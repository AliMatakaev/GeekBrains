class Date:
    def __init__(self, day_month_year):
        self.day_month_year = str(day_month_year)

    @classmethod
    def extract(cls, day_month_year):
        my_date = []

        for i in day_month_year.split():
            if i != '-':
                my_date.append(i)

        return int(my_date[0]), int(my_date[1]), int(my_date[2])

    @staticmethod
    def valid(day, month, year):

        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 2019 >= year >= 0:
                    return f'Valid date'
                else:
                    return f'Неверно указан год'
            else:
                return f'Неверно указан месяц'
        else:
            return f'Неверно указан день'

    def __str__(self):
        return f'Текущая дата {Date.extract(self.day_month_year)}'


today = Date('11 - 1 - 2001')
print(today)
print(Date.valid(11, 11, 2022))
print(today.valid(11, 13, 2011))
print(Date.extract('11 - 11 - 2011'))
print(today.extract('11 - 11 - 2020'))
print(Date.valid(1, 11, 2000))
