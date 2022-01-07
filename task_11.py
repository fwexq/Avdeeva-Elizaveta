class Desert:
    def init(self, name=None, calories=None):
        self.name = name
        self.calories = calories

    def get_desert(self):
        return self.name, self.calories

    def set_desert(self, name, calories):
        self.name = name
        self.calories = calories

    def is_healthy(self):
        if self.calories < 200:
            return True
        else:
            return False

    def is_delicious(self):
        return True


desert = Desert()

desert.set_desert(name='Pie', calories=205)
print(desert.name, desert.calories)
print(desert.is_healthy())
print(desert.is_delicious())
