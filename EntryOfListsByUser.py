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

#     print(slist)
#     max = -1
#     s1 = ""

for s in slist:
    s.displayS()

# if s.marks > max:
#     max = s.marks
#     s1 = s.name
#     print("student with marks:",s1)                    