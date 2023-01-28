class Area:
    def Km2_M2(self,km):
        km=float(km)
        res=km*1000**2
        return res
    def M2_Km2(self,m):
        m=float(m)
        res=m/1000**2
        return res
    def M2_Cm2(self,m):
        m=float(m)
        res=m*100**2
        return res
    def Cm2_M2(self,cm):
        cm=float(cm)
        res=cm/100**2
        return cm
    def Cm2_MM2(self,cm):
        cm=float(cm)
        res=cm*10**2
        return res
    def MM2_Cm2(self,mm):
        mm=float(mm)
        res=mm/10**2
        return res
    def Km2_Cm2(self,Km):
        Km=float(Km)
        res1=self.Km2_M2(Km)
        res2=self.M2_Cm2(res1)
        return res2
    def Km2_MM2(self,Km):
        Km=float(Km)
        res1=self.Km2_Cm2(Km)
        res2=self.Cm2_MM2(res1)
        return res2
    def M2_MM2(self,m):
        m=float(m)
        res1=self.M2_Cm2(m)
        res2=self.Cm2_MM2(res1)
        return res2
    def Cm2_Km2(self,cm):
        cm=float(cm)
        res1=self.Cm2_M2(cm)
        res2=self.M2_Km2(res1)
        return res2
    def MM2_M2(self,mm):
        mm=float(mm)
        res1=self.MM2_Cm2(mm)
        res2=self.Cm2_M2(res1)
        return res2
    def MM2_Km2(self,mm):
        mm=float(mm)
        res1=self.MM2_M2(mm)
        res2=self.M2_Km2(res1)
        return res2

# if '__main__'==__name__:
#
#
#     Convert_Area=Area()
#     print_Con=[
#         Convert_Area.M2_Km2(1),
#         Convert_Area.M2_Cm2(1),
#         Convert_Area.M2_MM2(1),
#         Convert_Area.MM2_M2(1),
#         Convert_Area.MM2_Km2(1),
#         Convert_Area.MM2_Cm2(1),
#         Convert_Area.Cm2_M2(1),
#         Convert_Area.Cm2_Km2(1),
#         Convert_Area.Cm2_MM2(1),
#         Convert_Area.Km2_M2(1),
#         Convert_Area.Km2_Cm2(1),
#         Convert_Area.Km2_MM2(1)
#                ]
#     print(print_Con)