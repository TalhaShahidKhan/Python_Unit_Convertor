class Temperature:
    def Celcius_Farenhit(self, C):
        C=float(C)
        res=C/5*9+32
        return res
    def Farenhit_Celcius(self, F):
        F=float(F)
        res=5/9*(F-32)
        return res
    def Farenhit_Kelvin(self, F):
        F=float(F)
        res=5/9*(F-32)+273
        return res
    def Kelvin_Farenhit(self, K):
        K=float(K)
        res=9/5*(K-273)+32
        return res
    def Celcius_Kelvin(self, C):
        C=float(C)
        res1=self.Celcius_Farenhit(C)
        res2=self.Farenhit_Kelvin(res1)
        return res2
    def Kelvin_Celcius(self,K):
        K=float(K)
        res1=self.Kelvin_Farenhit(K)
        res2=self.Farenhit_Celcius(res1)
        return res2
# if '__main__'==__name__:
#     inp1 = Temperature()
#     print(inp1.Kelvin_Celcius(309.9))
#     print(inp1.Celcius_Kelvin(36.9))
#     print(inp1.Farenhit_Kelvin(98.42))
#     print(inp1.Farenhit_Celcious(98.42))
#     print(inp1.Celcius_Farenhit(36.9))
