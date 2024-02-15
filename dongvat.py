class Dongvat:
    nhom =''
    thuc_an= ''
    def __init__(self,nhom,thuc_an):
        self.nhom = nhom
        self.thuc_an = thuc_an
con_bo = Dongvat("có vú","ăn cỏ")
ca_sau = Dongvat("bò sát", "ăn thịt")
print("con bò là động vật thuộc nhóm {} và {}".format(con_bo.nhom,con_bo.thuc_an))
print("cá sấu là loài động vật thuộc nhóm {} và {}".format(ca_sau.nhom,ca_sau.thuc_an))