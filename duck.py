from bird import Bird

# tính đa hình
# cùng một phương thức nhưng có thể cho hành động của class cha và class con khác nhau
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