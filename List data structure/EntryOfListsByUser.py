class pgstudent:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def displayS(self):
        print("name:",self.name,"marks:",self.marks)

slist=[]
j = int(input("Enter the number of students you want to enter"))
for i in range(j):
        n = input("Enter name of the student:")
        m = int(input("Enter the marks of the student:"))
        s = pgstudent(n,m)
        slist.append(s)



for s in slist:
    s.displayS()

            