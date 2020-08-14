class Electronic_device:
    
    def var1(self):
        return "These are all a class of electronic devices"

class Pocket_gadget(Electronic_device):
    
    def var2(self):

        return "Inherited from Electronic_device"

class Phone(Pocket_gadget):
    
    def specs(self):
        name = "Samsaung Galaxy Note 8"
        battery = "3000 MAh"
        return battery


Edevice = Electronic_device()
Pgad = Pocket_gadget()
Cell_Phone = Phone()

print(Cell_Phone.specs())
print(Cell_Phone.var1())
print(Cell_Phone.var2())