#working with Operator in python
class Product:
    def __init__(self,pr_id,pr_n):
        self.tcost = 0
        self.p_unit = 0
        self.p_code = pr_id
        self.p_name = pr_n
        if(self.p_name == "laptop"):
            self.p_cost = 25000
        elif(self.p_name == "tab"):
            self.p_cost = 8900
        elif(self.p_name == "penDrive"):
            self.p_cost = 650
        else:
            self.p_cost = 1000
    def ShowProduct(self,un):
        self.p_unit = un
        self.tcost = self.p_unit*self.p_cost
        if(self.tcost >= 35000 and self.tcost <= 50000):
            self.dis = self.tcost*20/100
        elif(self.tcost > 10000 and self.tcost < 35000):
            self.dis = self.tcost*15/100
        else:
            self.dis = self.tcost*10/100

        print("Details..")
        print("pro_name=",self.p_name,"cost=",self.p_cost,"unit=",self.p_unit)
        print("discount=",self.dis)
        print("bill amount",self.tcost-self.dis)

ob = Product(100,"Tab")
ob.ShowProduct(4)                                    