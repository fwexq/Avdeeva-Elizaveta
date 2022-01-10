class Dessert:
    def __init__(self, name=None, calories=None):
        self.name = name
        self.calories = calories

    def get_dessert(self):
        return self.name, self.calories

    def set_dessert(self, name, calories):
        self.name = name
        self.calories = calories

    def is_healthy(self):
        if self.calories < 200:
            return True
        else:
            return False

    def is_delicious(self):
        return True


#dessert = Dessert(name='Pie', calories=220)
#print(dessert.name, dessert.calories)
#print(dessert.is_healthy())
#print(dessert.is_delicious())
