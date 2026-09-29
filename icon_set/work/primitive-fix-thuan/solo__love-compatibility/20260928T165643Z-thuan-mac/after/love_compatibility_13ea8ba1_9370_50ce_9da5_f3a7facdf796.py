"""Redrew the rear heart with flowing flanks and a balanced point, retaining the smaller overlapping foreground heart."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='13ea8ba1-9370-50ce-9da5-f3a7facdf796'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__love-compatibility/20260928T165643Z-thuan-mac/reference/love compatibility_13ea8ba1-9370-50ce-9da5-f3a7facdf796.svg'
AUTHOR='gpt-6'
PLAN='Redrew the rear heart with flowing flanks and a balanced point, retaining the smaller overlapping foreground heart.'
CONSTRUCTION_REFERENCE='Lucide heart: smooth lobe-to-flank curves; original: two overlapping hearts.'
OMISSIONS='Hidden rear-heart edge omitted behind the foreground heart.'
class Drawing(Solo48):
    icon_id='love-compatibility'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('love', 'compatibility')

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
        self.path('front',(31,22),[('C',(37,18),(33,19),(35,18)),('C',(42,24),(40,18),(42,20)),('C',(31,42),(42,31),(36,37)),('C',(23,33),(27,38),(25,36)),('C',(20,24),(21,30),(20,27)),('C',(25,18),(20,20),(22,18)),('C',(31,22),(27,18),(29,19))],True)
        self.path('rear',(23,33),[('C',(17,40),(20,35),(18,38)),('C',(6,19),(11,34),(6,26)),('C',(14,6),(6,10),(9,6)),('C',(22,11),(18,6),(20,8)),('C',(29,6),(24,8),(26,6)),('C',(37,18),(34,6),(37,11))])
        self.relate('connect','rear','front')
