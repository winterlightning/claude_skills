'The neck and shoulders were stiff and boxy. Restored a circular U-neck, smooth paired shoulders and clean sleeve seams.\nSymbol plan: typed contours, shared radii and exact attachment nodes; paired features use common dimensions.\nConstruction: Lucide shirt. Keyshape SQUARE; any proportional departure is recorded as an exact-drawing exception.'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='fdc676d2-ae16-4a1e-aed2-83f04934bae5'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__virtual-shopping-fashion-fitting/20260928T173023Z-thuan-mac/reference/virtual shopping fashion fitting_fdc676d2-ae16-4a1e-aed2-83f04934bae5.svg'
AUTHOR="gpt-6"
PARENT_MODULE='icon_set/work/primitive-fix-thuan/solo__virtual-shopping-fashion-fitting/20260928T173023Z-thuan-mac/before/virtual_shopping_fashion_fitting_fdc676d2_ae16_4a1e_aed2_83f04934bae5.py'
class Drawing(Solo48):
    icon_id='virtual-shopping-fashion-fitting'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category="primitives-generate"
    aliases=()
    keywords=('virtual', 'shopping', 'fashion', 'fitting')

    def path(self,n,p,commands,closed=False):
        ids=[]
        for i,c in enumerate(commands):
            k=f'{n}-{i}';q=c[1]
            if c[0]=='L':self.add_line(k,p,q)
            elif c[0]=='A':self.add_arc(k,p,q,radius_x=c[2],radius_y=c[3],sweep=c[4])
            elif c[0]=='C':self.add_bezier(k,p,(c[2],c[3],q))
            ids.append(k);p=q
        self.add_contour(n,*ids,closed=closed)
    def circle(self,n,x,y,r):
        self.path(n,(x-r,y),[('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True)],True)
    def box(self,n,l,t,r,b,rad=4,split=None):
        pts=[(l+rad,t),(r-rad,t),(r,t+rad),(r,b-rad),(r-rad,b),(l+rad,b),(l,b-rad),(l,t+rad)]
        commands=[]
        for i in range(8):
            q=pts[(i+1)%8]
            if i%2:commands.append(('A',q,rad,rad,True))
            else:
                for p in (split or {}).get(i,[]):commands.append(('L',p))
                commands.append(('L',q))
        self.path(n,pts[0],commands,True)

    def node(self,n,x,y,r,extra=()):
        import math
        offsets=set([(-r,0),(0,-r),(r,0),(0,r),*extra])
        offsets=sorted(offsets,key=lambda p:math.atan2(p[1],p[0]))
        pts=[(x+dx,y+dy) for dx,dy in offsets]
        self.path(n,pts[0],[('A',q,r,r,True) for q in pts[1:]+pts[:1]],True)

    def bubble(self):
        self.path('bubble',(22,38),[('L',(22,44)),('C',(40,22),(33,39),(40,31)),('C',(24,4),(40,12),(33,4)),('C',(8,21),(15,4),(8,11)),('C',(22,38),(8,31),(14,37))],True)
    def file(self):
        self.path('page',(12,4),[('L',(28,4)),('L',(40,16)),('L',(40,40)),('A',(36,44),4,4,True),('L',(12,44)),('A',(8,40),4,4,True),('L',(8,8)),('A',(12,4),4,4,True)],True)
        self.path('fold',(28,4),[('L',(28,12)),('A',(32,16),4,4,False),('L',(40,16))]);self.relate('connect','page','fold')

    def build(self):
        # Shared shoulder shape and circular U-neck; preserve the natural rounded shoulder slopes.
        self.path('shirt',(18,6),[('A',(30,6),6,6,False),('C',(38,12),(34,6),(36,8)),('L',(42,22)),('L',(34,25)),('L',(34,42)),('L',(14,42)),('L',(14,25)),('L',(6,22)),('L',(10,12)),('C',(18,6),(12,8),(14,6))],True)
        for x in (14,34):
            self.add_line(f'sleeve-seam-{x}',(x,18),(x,25));self.relate('connect','shirt',f'sleeve-seam-{x}')
