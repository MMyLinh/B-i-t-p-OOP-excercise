class Animals:
    group =''
    food= ''
    def __init__(self,group,food):
        self.group = group
        self.food = food
cow = Animals("mammal","grass")
crocodile = Animals("reptiles", "meats")
print("Cows belong to the group of  {} and eat {}".format(cow.group,cow.food))
print("crocodile belong to the group of  {} and eat {}".format(crocodile.group,crocodile.food))
class Bird(Animals): #class Bird là class con của class Animals 
    def __init__(self):
        print("Bird is ready")
    def whatisthis(self):
        print("Bird")
    def fly(self):
        print("Bird can fly")
    def swim(self):
        print("Bird can't swim")
    def fly(self):
        print("fly so fast")
class Eagle(Bird):  # class Eagle là class con của Class Bird
    def __init__(self):
        print("Eagle is ready")
    def whatisthis(self):
        print("Eagle")
    def run(self):
        print("run so fast")
class Duck(Bird):
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
eagle=Eagle()
eagle.whatisthis()
eagle.fly() #phương thức fly nằm trong class Bird nhưng class con Eagle vẫn có thể gọi sử dụng được
eagle.run()

