from bird import Bird

# class Eagle là class con của Class Bird
class Eagle(Bird): 
    def __init__(self):
        print("Eagle is ready")
    def whatisthis(self):
        print("Eagle")
    def run(self):
        print("run so fast")

eagle=Eagle()
eagle.whatisthis()
eagle.fly() #phương thức fly nằm trong class Bird nhưng class con Eagle vẫn có thể gọi sử dụng được
eagle.run()