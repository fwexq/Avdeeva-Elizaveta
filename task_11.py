class Dessert:
    def __init__(self, name=None, calories=None):
        self.name = name
        self.calories = calories

    def get_name(self):
        return self.name

    def get_calories(self):
        return self.calories

    def set_name(self, name):
        self.name = name

    def set_calories(self,calories):
        self.calories = calories

    def is_healthy(self):
        if isinstance(self.calories, int):
            if self.calories < 200:
                return True
            else:
                return False
        else:
            return False

    def is_delicious(self):
        return True

#dessert = Dessert(name='Pie', calories='170')
#print(dessert.name, dessert.calories)
#print(dessert.is_healthy())
#print(dessert.is_delicious())
