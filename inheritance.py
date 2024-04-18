#multilevel inheritance
class box:
    def _init_(self,name,rollno):
        self.n=name
        self.r=rollno
class box2(box):
    def _init_(self,name,rollno,fees):
        self.f=fees
        box._init_(self,name,rollno)
    
    
class box3(box2):
    def _init_(self,sem,name,rollno,fees):
        self.s=sem
        box2._init_(self,name,rollno,fees)


obj = box3(3,"san",47,10000)
print(obj.s)


#single level inheritance
class box:
    def _init_(self,name,rollno):
        self.n=name
        self.r=rollno
class box2(box):
    def _init_(self,name,rollno,fees):
        self.f=fees
        box._init_(self,name,rollno)

obj = box2("san",47,10000)
print(obj.f)

#multiple inheritance
class box:
    def _init_(self,name,rollno):
        self.n=name
        self.r=rollno
class box2:
    def _init_(self,fees):
        self.f=fees
class box3(box,box2):
    def _init_(self,name,rollno,fees,sem):
        self.s=sem
        box._init_(self,name,rollno)
        box2._init_(self,fees)
    

obj = box3("san",47,10000,4)
print(obj.s)
