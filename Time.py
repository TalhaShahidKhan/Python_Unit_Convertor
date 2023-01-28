class Time:
    def H_M(self,h):
        h=float(h)
        res=h*60
        return res
    def M_S(self,m):
        m=float(m)
        res=m*60
        return res
    def S_M(self,s):
        s=float(s)
        res=s/60
        return res
    def M_H(self,m):
        m=float(m)
        res=m/60
        return res
    def H_S(self,h):
        h=float(h)
        res1=self.H_M(h)
        res2=self.M_S(res1)
        return res2
    def S_H(self,s):
        s=float(s)
        res1=self.S_M(s)
        res2=self.M_H(res1)
        return res2

# if '__main__'==__name__:
#
#
#     calcTime=Time()
