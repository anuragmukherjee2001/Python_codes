class Dad:
    basketball = 1

class Son(Dad):
    dance = 1

    def isdance(self):
        return f"Hurray I like dancing and I dance {self.dance} no. of times"

class Grandson(Son):
    dance = 6

    def isdance(self):
        return f"Hurray I like dancing and I dance {self.dance} no. of times, Awesome"


anurag = Dad()
davison = Son()
Hasting = Grandson()

print(Hasting.basketball)

print(Hasting.isdance())