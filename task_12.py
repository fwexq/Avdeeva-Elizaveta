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


class JellyBean(Desert):
    def init(self, flavor=None):
        super(JellyBean, self).init()
        self.flavor = flavor

    def is_delicious(self):
        if self.flavor == 'black licorice':
            return False
        else:
            return True