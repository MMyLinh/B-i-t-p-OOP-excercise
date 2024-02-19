class Animal:
    def __init__(self):
        self.__king_of_animals="lion"
    def king(self):
        print('we call king of animals is : {}'.format(self.__king_of_animals))
    def set_king(self,new_king):
       self.__king_of_animals = new_king
c=Animal()
c.king()
c.__king_of_animals="wolf"
c.king()
c.set_king("wolf")
c.king()