class Hanhdong:
    def __init__(self,hanhdong):
        self.hanhdong=hanhdong
    def hat(self,sing):
        return"{} dang hat {} ".format(self.hanhdong,sing)
    def nhay(self,nhun):
        return"{} cung dang nhay {}" .format(self.hanhdong,nhun)
tho= Hanhdong("tho con")
print(tho.hat("vui ve"))
print(tho.nhay("rat sung"))