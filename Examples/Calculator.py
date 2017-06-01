class Calc(object):

    def __init__(self,a,b):
        self.a = a
        self.b = b
    
    def sum(self):
        return self.a + self.b

    def sub(self):
        return self.a - self.b
    
    def mul(self):
        return self.a * self.b
    
    def div(self):
        return self.a / self.b
    
    def exp(self):
        return self.a ** self.b
    
    def sqr(self):
        return self.a ** (1/self.b)