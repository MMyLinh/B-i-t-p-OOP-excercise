from animal import Animal

# class Bird là class con của class Animal
# tính thừa kế: class con dùng lại phương thức của class cha
class Bird(Animal):
    def __init__(self):
        self.__king_of_birds="eagle"  #
        print("Bird is ready")
    def whatisthis(self):
        print("Bird")
    def fly(self):
        print("Bird can fly")
    def swim(self):
        print("Bird can't swim")
    def fly(self):
        print("fly so fast")

    def king(self):
        print('we call king of birds is : {}'.format(self.__king_of_birds))
    def set_king(self,new_king):
       self.__king_of_birds = new_king

c=Bird()
c.king()
c.__king_of_birds="chicken"
c.king()
c.set_king("chicken")
c.king()

# tính đóng gói

# private, public và protected thể hiện tính đóng gói trong Ruby.

# private sẽ chỉ cho gọi method ở trong class kể từ lúc định nghĩa

# protected cũng tương tự như private, nhưng cho phép 1 số class khác kế thừa từ class định nghĩa truy cập thêm(bao gồm cả chính class ấy, kí hiệu là self)

# public là cho phép method đó được truy cập ở mọi nơi.