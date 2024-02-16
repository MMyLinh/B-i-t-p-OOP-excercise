class Student:
    count = 0
    def __init__(self,id,name):
        self.id=id
        self.name=name
        Student.count+=1
    def get_id(self):
        return self.id
    def set_name(self,name):
        self.name=name
    def get_name(self):
        return self.name
    def show(self):
        print(f'ID: {self.id}')
        print(f'Name : {self.name}')
        