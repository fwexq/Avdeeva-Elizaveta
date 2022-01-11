class Dessert:
    def __init__(self, name='', calories=0):
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
        if isinstance(self.calories, int) or isinstance(self.calories, float):
            if self.calories < 200:
                return True
            else:
                return False
        else:
            return False

    def is_delicious(self):
        return True

class JellyBean(Dessert):
    def __init__(self, name=None, calories=None, flavor=None):
        super().__init__(name, calories)
        self.flavor = flavor

    def is_delicious(self):
        if self.flavor == 'black licorice':
            return False
        else:
            return True

dessert1 = JellyBean(name='Milk', calories=0, flavor='black licorice')
print(dessert1.name, dessert1.calories, dessert1.flavor)
print(dessert1.is_delicious())
