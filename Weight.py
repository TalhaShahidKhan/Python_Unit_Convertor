class Weight:
    def KG_G(self,kg):
        kg=float(kg)
        res=kg*1000
        return res
    def G_MlG(self,g):
        g=float(g)
        res=g*1000
        return res
    def MlG_G(self,mLg):
        mLg=float(mLg)
        res=mLg/1000
        return res
    def G_KG(self,g):
        g=float(g)
        res=g/1000
        return res
    def KG_MlG(self,kg):
        kg=float(kg)
        res1=self.KG_G(kg)
        res2=self.G_MlG(res1)
        return res2
    def MlG_KG(self,mLg):
        mLg=float(mLg)
        res1=self.MlG_G(mLg)
        res2=self.G_KG(res1)
        return res2


