"""Restored a flatter almond with a straight ascending slash and exact shared crossing nodes."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='90c55c1b-6141-40f9-8dfb-e0b9bed3cb5e'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__hidden-visibility-eye-symbol-solo/20260928T171324Z-thuan-mac/reference/eye slash_90c55c1b-6141-40f9-8dfb-e0b9bed3cb5e.svg'
AUTHOR='gpt-6'
PLAN='Restored a flatter almond with a straight ascending slash and exact shared crossing nodes.'
CONSTRUCTION_REFERENCE='Lucide eye-off: almond silhouette and diagonal state stroke; supplied source uses the opposite slash direction and no pupil.'
OMISSIONS='None.'
class Drawing(Solo48):
    icon_id='hidden-visibility-eye-symbol-solo'
    keyshape=Keyshape.HRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('hidden', 'visibility', 'eye', 'symbol', 'solo')

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
        self.path('eye',(4,24),[('C',(24,10),(10,16),(17,10)),('C',(34,14),(28,10),(32,12)),('C',(44,24),(38,17),(41,20)),('C',(24,38),(38,32),(31,38)),('C',(14,34),(20,38),(16,36)),('C',(4,24),(10,31),(7,28))],True)
        self.add_polyline('slash',(8,40),(14,34),(34,14),(40,8))
        self.relate('connect','eye','slash')
