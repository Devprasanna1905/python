class student:
    def __init__(self):
        self.studentid=0
        self.studentname=""
        self.mark1=0
        self.mark2=0
        
    def getdetails(self): 
        self.studentid=int(input("enter your student id:"))
        self.studentname=(input("enter your name:"))
        self.mark1=int(input("enter your mark1:"))
        self.mark2=int(input("enter your mark2:"))
class result(student):      
    def showdetails(self):
        self.total=self.mark1+self.mark2
        self.average=self.total/2
        print("STUDENT ID:",self.studentid)
        print("STUDENT NAME:",self.studentname)
        print("MARK IN SUBJECT 1:",self.mark1)
        print("MARK IN SUBJECT 2:",self.mark2)
        print("TOTAL MARK:",self.total)
        print("AVERAGE MARK:",self.average)
show=result()
show.getdetails()
show.showdetails()

