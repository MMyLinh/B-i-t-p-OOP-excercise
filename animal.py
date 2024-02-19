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
