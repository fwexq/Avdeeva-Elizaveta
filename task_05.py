from datetime import datetime, timedelta
def date_in_future(integer=None):

    if isinstance(integer, list):
        return datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    if isinstance(integer, int):
        return (datetime.now() + timedelta(days=integer)).strftime("%d-%m-%Y %H:%M:%S")


print(date_in_future([])) # => текущая дата
print(date_in_future(2)) # => текущая дата + 2 дня
#