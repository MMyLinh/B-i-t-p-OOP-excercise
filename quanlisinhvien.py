from student import Student
sv=[]
while True:
    print(''' vui long chon chuc nang:
                0 thoat
                1 xem danh sach sv
                2 them sinh vien
                3 xoa sv
                4 sua sv
                ...
         ''')
    chon=input('ban chon chuc nang nao?')
    if chon.isdigit():
        chon=int(chon)
        if chon==0:
            break
        elif chon==1:
            if len(sv)==0:
               print('hien chua co sinh vien')
            else :
                for i in sv:
                    i.show()
        elif chon==2:
             id=input('nhap id sv')
             name=input('nhap ten sv')
             sv.append(Student(id,name))
        elif chon==3:
             id=input('nhap id sv muon xoa')
             for i in sv:
                    if i.id==id:
                        sv.remove(i)
        elif chon==4:
             id=input('nhap id sv muon sua')
             for i in sv:
                    if i.id==id:
                     i.set_name(input('nhap ten moi'))
    else:
        print('vui long chon lai')

