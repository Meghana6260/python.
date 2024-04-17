class Box:
    def __init__(self,Name,Rollno,DBMSmarks,Pythonmarks,Cmarks,OSmarks,CNmarks):
        self.name=Name
        self.rollno=Rollno
        self.dbms=DBMSmarks
        self.python=Pythonmarks
        self.cmarks=Cmarks
        self.osmarks=OSmarks
        self.cnmarks=CNmarks
        
    def alldetails(self):
        print(self.name,end=" ")
        print(self.rollno,end=" ")
        print(self.dbms,end=" ")
        print(self.python,end=" ")
        print(self.cmarks,end=" ")
        print(self.osmarks,end=" ")
        print(self.cnmarks,end=" ")
        print()
        
Student1=Box("Harika","5A1",78,67,77,89,46)
Student1.alldetails()


Student2=Box("Swapna","5A2",38,65,97,59,41)
Student2.alldetails()


Student3=Box("Sushma","5A3",88,97,47,89,31)
Student3.alldetails()
