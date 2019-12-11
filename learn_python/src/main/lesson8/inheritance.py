class Parent(object):
    def __init__(self, value):
        self.value = value

    def spam(self):
        print('Parent.spam', self.value)

    def grok(self):
        print('Parent.grok')
        self.spam()


class Child1(Parent):
    def yow(self):
        print('Child1.yow')

    def spam(self):
        print('Child1.spam', self.value)


class Child3(Parent):
    def spam(self):
        print('Child3.spam')
        super().spam()


class Child4(Parent):
    def __init__(self, value, extra):
        self.extra = extra
        super().__init__(value) # Initialize parent


class Parent2(object):
    def yow(self):
        print('Parent2 yow')


class Child5(Parent, Parent2):
    pass



