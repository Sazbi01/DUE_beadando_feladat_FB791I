import math

class operation:
    x = 0
    y = 0
    o = ''

    def add(self):
        return float(self.x + self.y)

    def sub(self):
        return float(self.x - self.y)

    def div(self):
        return float(self.x / self.y)

    def multi(self):
        return float(self.x * self.y)

    def sqrt(self, s):
        return float(math.sqrt(s))

    def pi(self):
        return math.pi

    def sin(self):
        return float(math.sin(self.x))

    def cos(self):
        return float(math.cos(self.x))

    def result(self):
        match self.o:
            case '+':
                return self.add()
            case '-':
                return self.sub()
            case '*':
                return self.multi()
            case '/':
                return self.div()