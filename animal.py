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
class Bird(Animals):
    def __init__(self):
        print("Bird is ready")
    def whatisthis(self):
        print("Bird")
    def fly(self):
        print("fly so fast")
class Eagle(Bird):
    def __init__(self):
        print("Eagle is ready")
    def whatisthis(self):
        print("Eagle")
    def run(self):
        print("run so fast")
eagle=Eagle()
eagle.whatisthis()
eagle.fly()
eagle.run()
