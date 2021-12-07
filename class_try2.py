class Frindes:
    
    def __init__(self,tel_no,adress,e_mail):
        self.all=tel_no,e_mail,adress
        self.tel_no=tel_no
        self.adress=adress
        self.e_mail=e_mail
    def get_details(self):
        return self.all
Ahmed=Frindes("017695721049","cottbus","amz@gmail.com")
Alaa=Frindes("017569855645","senftenberg","alaali@gmail.com")
Belal=Frindes("017655423665","cottbus","beladawwas@gmail.com")
print("Frindes list:")
print("\nAhmed:",Ahmed.tel_no,Ahmed.e_mail,Ahmed.adress)
print("Alaa:",Alaa.tel_no,Alaa.e_mail,Alaa.adress)
print("Belal:",Belal.tel_no,Belal.e_mail,Belal.adress)

print("\ndetails of Ahmed alone:",Ahmed.get_details())

