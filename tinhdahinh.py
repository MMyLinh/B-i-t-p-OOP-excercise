class Conchim:
    def bay(self):
        print("con chim biet bay")
    def boi(self):
        print("con chim khong biet boi")
class Convit:
    def bay(self):
        print("con vit khong biet bay")
    def boi(self):
        print("con vit biet boi")
def bay_test(chim):
    chim.bay()
def boi_test(vitcon):
    vitcon.boi()
conchim=Conchim()
convit=Convit()
bay_test(conchim)
bay_test(convit)
boi_test(conchim)
boi_test(convit)
