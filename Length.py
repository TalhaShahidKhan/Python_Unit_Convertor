class Length:

    def Km_M(self,km):
        km=float(km)
        res=km*1000
        return res
    def M_Km(self,m):
        m=float(m)
        res=m/1000
        return res
    def M_Cm(self,m):
        m=float(m)
        res=m*100
        return res
    def Cm_M(self,cm):
        cm=float(cm)
        res=cm/100
        return cm
    def Cm_MM(self,cm):
        cm=float(cm)
        res=cm*10
        return res
    def MM_Cm(self,mm):
        mm=float(mm)
        res=mm/10
        return res
    def Km_Cm(self,Km):
        Km=float(Km)
        res1=self.Km_M(Km)
        res2=self.M_Cm(res1)
        return res2
    def Km_MM(self,Km):
        Km=float(Km)
        res1=self.Km_Cm(Km)
        res2=self.Cm_MM(res1)
        return res2
    def M_MM(self,m):
        m=float(m)
        res1=self.M_Cm(m)
        res2=self.Cm_MM(res1)
        return res2
    def Cm_Km(self,cm):
        cm=float(cm)
        res1=self.Cm_M(cm)
        res2=self.M_Km(res1)
        return res2
    def MM_M(self,mm):
        mm=float(mm)
        res1=self.MM_Cm(mm)
        res2=self.Cm_M(res1)
        return res2
    def MM_Km(self,mm):
        mm=float(mm)
        res1=self.MM_M(mm)
        res2=self.M_Km(res1)
        return res2

# if '__main__'==__name__:
#
#     Convert_Length=Length()
#     print_Con=[
#         Convert_Length.M_Km(1),
#         Convert_Length.M_Cm(1),
#         Convert_Length.M_MM(1),
#         Convert_Length.MM_M(1),
#         Convert_Length.MM_Km(1),
#         Convert_Length.MM_Cm(1),
#         Convert_Length.Cm_M(1),
#         Convert_Length.Cm_Km(1),
#         Convert_Length.Cm_MM(1),
#         Convert_Length.Km_M(1),
#         Convert_Length.Km_Cm(1),
#         Convert_Length.Km_MM(1)
#                ]
#     print(print_Con)