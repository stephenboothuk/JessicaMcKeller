class Greeter(object):
    def __init__(self, name):
        self.name = name

    def sayHello(self):
        print("Hello " + self.name)

    def waveGoodbye(self):
        print("Goodbye " + self.name)

g = Greeter("AAAAAA")
g.sayHello()
g.waveGoodbye()

h = Greeter("BBBB")
h.sayHello()
h.waveGoodbye()

