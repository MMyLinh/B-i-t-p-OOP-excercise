class Conchim:
    def __init__(self):
        print("con chim da san sang")
    def daylagi(self):
        print("con chim")
    def chay(self):
        print("chay rat nhanh")
class Daibang(Conchim):
    def __init__(self):
        super().__init__()
        print("dai bang da san sang")
    def daylagi(self):
        print("dai bang")
    def bay(self):
        print("bay rat nhanh")
chim_ung=Daibang()
chim_ung.daylagi()
chim_ung.chay()
chim_ung.bay()