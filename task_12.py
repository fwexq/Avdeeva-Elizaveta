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

class JellyBean(Dessert):
    def __init__(self, name, calories, flavor=None):
        super().__init__(name, calories)
        self.flavor = flavor

    def is_delicious(self):
        if self.flavor == 'black licorice':
            return False
        else:
            return True

#dessert1 = JellyBean(name='Milk', calories=199, flavor='black licorice')
#print(dessert1.name, dessert1.calories, dessert1.flavor)
#print(dessert1.is_delicious())
