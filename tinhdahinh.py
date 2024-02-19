class Bird:
    def fly(self):
        print("Bird can fly")
    def swim(self):
        print("Bird can't swim")
class Duck:
    def fly(self):
        print("Duck can't fly")
    def swim(self):
        print("Duck can swim")
def fly_test(bird):
    bird.fly()
def swim_test(duck):
    duck.swim()
bird=Bird()
duck=Duck()
fly_test(bird)
fly_test(duck)
swim_test(bird)
swim_test(duck)
