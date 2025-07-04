#conceptual example of multiple inheritance
class Animal:
    def hunt(self):
        print("I can hunt")
    def run(self):
        print("I can run")
class Bird:
    def sing(self):
        print("i can sing")
    def fly(self):
        print("I can fly")
class Bat(Animal,Bird):
    def hang(self):
        print("I can hang")
    def whatICanDo(self):
        super().hunt()
        super().run()
        super().fly()
        super().sing()
        self.hang()

b1 = Bat()
b1.whatICanDo()

