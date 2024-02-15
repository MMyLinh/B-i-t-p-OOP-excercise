class Dongvat:
    nhom =''
    thuc_an= ''
    def __init__(self,nhom,thuc_an):
        self.nhom = nhom
        self.thuc_an = thuc_an
con_bo = Dongvat("có vú","ăn cỏ")
ca_sau = Dongvat("bò sát", "ăn thịt")
print("con bò là động vật thuộc nhóm {}".format(con_bo.nhom))
print("cá sấu là loài động vật thuộc nhóm {}".format(ca_sau.nhom))
print("con bò {}".format(con_bo.thuc_an))
print("cá sấu {}".format(ca_sau.thuc_an))