class WeekDayError(Exception):
    pass
	

class Weeker:
    __priv = ['Mon', 'Tue', 'Wed', 'Thur', 'Fri', 'Sat', 'Sun']

    def __init__(self, day):
        try:
            self.__value = Weeker.__priv.index(day)
        except ValueError:
            raise WeekDayError

    def __str__(self):
        return Weeker.__priv[self.__value]

    def add_days(self, n):
        self.__value += n % 7

    def subtract_days(self, n):
        self.__value -= n % 7


try:
    weekday = Weeker('Mon')
    print(weekday)
    weekday.add_days(15)
    print(weekday)
    weekday.subtract_days(23)
    print(weekday)
    weekday = Weeker('Monday')
except WeekDayError:
    print("Sorry, I can't serve your request.")