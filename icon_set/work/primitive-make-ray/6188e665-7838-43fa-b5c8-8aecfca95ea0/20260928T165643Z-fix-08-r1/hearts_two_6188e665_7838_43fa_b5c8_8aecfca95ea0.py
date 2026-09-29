"""Detached the small heart and reopened the large heart on its upper-right edge."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='6188e665-7838-43fa-b5c8-8aecfca95ea0'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__hearts-two/20260928T165643Z-thuan-mac/reference/three hearts_6188e665-7838-43fa-b5c8-8aecfca95ea0.svg'
AUTHOR='gpt-6'
PLAN='Detached the small heart and reopened the large heart on its upper-right edge.'
CONSTRUCTION_REFERENCE='Lucide heart: rounded paired lobes; source: separate diagonal hearts and intentional break.'
OMISSIONS='Large heart upper-right edge intentionally open as in source.'
class Drawing(Solo48):
    icon_id='hearts-two'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('hearts', 'two')

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
        self.path('small',(35,9),[('C',(30,6),(33,6),(31,6)),('C',(28,10),(28,6),(28,8)),('C',(35,20),(28,14),(32,17)),('C',(42,10),(38,17),(42,14)),('C',(40,6),(42,8),(42,6)),('C',(35,9),(39,6),(37,6))],True)
        self.path('large',(24,21),[('C',(18,24),(22,20),(20,22)),('C',(12,20),(16,22),(14,20)),('C',(6,27),(8,20),(6,23)),('C',(20,42),(6,33),(14,38)),('C',(33,29),(26,37),(32,34))])
