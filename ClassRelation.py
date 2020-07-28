#working with class Relation

class Dept:
    def __init__(self, da, loc):
        self.dept_name = da
        self.dept_place = loc

    def ShowDept(self):
        print("dept details")
        print("dept name = ",self.dept_name,"located =",self.dept_place)

class Emp(Dept):
    def __init__(self,da,loc,eid,eu,epay):
        Dept.__init__(self,da,loc)
        self.emp_code = eid
        self.emp_name = eu
        self.emp_pay = epay

    def ShowReport(self):
        print("Emp results")
        print("code =",self.emp_code,"Name=",self.emp_name,"pay =",self.emp_pay)
        Dept.ShowDept(self)

ob = Emp("Accounts","Mumbai",101,"joy","195000")
ob.ShowReport()                        