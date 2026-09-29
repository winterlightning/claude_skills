"""Restored broad heart lobes and a circular user head above smooth open shoulders."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='e7e97355-bccb-465c-ae55-5037fd70d291'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__heart-user/20260928T165643Z-thuan-mac/reference/heart user_e7e97355-bccb-465c-ae55-5037fd70d291.svg'
AUTHOR='gpt-6'
PLAN='Restored broad heart lobes and a circular user head above smooth open shoulders.'
CONSTRUCTION_REFERENCE='Lucide heart: broad lobes and tapered point; human_ref/user.svg: circular head and open shoulders.'
OMISSIONS='None.'
class Drawing(Solo48):
    icon_id='heart-user'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('heart', 'user')

    def path(self,n,start,commands,closed=False):
        here=start; ids=[]
        for i,(kind,end,*a) in enumerate(commands):
            ident=f'{n}-{i}';ids.append(ident)
            if kind=='L': self.add_line(ident,here,end)
            elif kind=='A': self.add_arc(ident,here,end,radius_x=a[0],radius_y=a[1],sweep=a[2])
            elif kind=='C': self.add_bezier(ident,here,(a[0],a[1],end))
            here=end
        self.add_contour(n,*ids,closed=closed)
    def circle(self,n,x,y,r):
        self.path(n,(x-r,y),[('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True)],True)
    def box(self,n,l,t,r,b,k=4):
        self.path(n,(l+k,t),[('L',(r-k,t)),('A',(r,t+k),k,k,True),('L',(r,b-k)),('A',(r-k,b),k,k,True),('L',(l+k,b)),('A',(l,b-k),k,k,True),('L',(l,t+k)),('A',(l+k,t),k,k,True)],True)
    def phone(self,band=True):
        # Shared outline owns width, corner radius and band attachment nodes.
        l,r,t,b,k,y=10,38,4,44,4,36
        self.path('phone',(l+k,t),[('L',(r-k,t)),('A',(r,t+k),k,k,True),('L',(r,y)),('L',(r,b-k)),('A',(r-k,b),k,k,True),('L',(l+k,b)),('A',(l,b-k),k,k,True),('L',(l,y)),('L',(l,t+k)),('A',(l+k,t),k,k,True)],True)
        if band:
            self.add_line('band',(l,y),(r,y));self.relate('connect','phone','band')

    def build(self):

        self.path('heart',(24,10),[('C',(15,6),(21,7),(18,6)),('C',(6,16),(9,6),(6,10)),('C',(24,42),(6,34),(14,39)),('C',(42,16),(34,39),(42,34)),('C',(33,6),(42,10),(39,6)),('C',(24,10),(30,6),(27,7))],True)
        self.circle('head',24,20,3)
        # user.svg: head bottom23, shoulders top31 = exact 4 ink gap.
        self.path('shoulders',(20,33),[('A',(24,31),4,2,True),('A',(28,33),4,2,True)])

