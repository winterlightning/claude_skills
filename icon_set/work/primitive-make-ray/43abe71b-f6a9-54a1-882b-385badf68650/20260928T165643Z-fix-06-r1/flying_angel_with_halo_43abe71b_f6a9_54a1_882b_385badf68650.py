"""Separated the open wing from the robe, restored a swept robe, circular head and open halo."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='43abe71b-f6a9-54a1-882b-385badf68650'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__flying-angel-with-halo/20260928T165643Z-thuan-mac/reference/angel_43abe71b-f6a9-54a1-882b-385badf68650.svg'
AUTHOR='gpt-6'
PLAN='Separated the open wing from the robe, restored a swept robe, circular head and open halo.'
CONSTRUCTION_REFERENCE='human_ref/full_body_ref.png for circular head and robe; supplied reference for wing, pose and halo. No useful local Lucide angel.'
OMISSIONS='Halo uses an open arc to keep its opening clear; face and feather details omitted.'
class Drawing(Solo48):
    icon_id='flying-angel-with-halo'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('flying', 'angel', 'with', 'halo')

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
        # human_ref full_body_ref: circular head. Head bottom=24, body neck=32: 4 ink gap.
        self.circle('head',34,20,4)
        self.path('halo',(26,7),[('A',(42,7),8,3,True)])
        self.path('robe',(34,32),[('C',(27,42),(34,36),(30,40)),('C',(6,32),(18,42),(9,36)),('C',(34,32),(16,32),(27,27))],True)
        self.path('wing',(22,21),[('C',(6,6),(15,18),(9,10)),('C',(15,25),(3,15),(7,23))])
