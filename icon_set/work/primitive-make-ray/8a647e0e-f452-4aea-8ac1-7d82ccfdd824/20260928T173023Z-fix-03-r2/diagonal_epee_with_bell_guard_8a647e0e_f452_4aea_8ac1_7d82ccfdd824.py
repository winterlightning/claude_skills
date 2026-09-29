'The guard was pinched and its joins distorted the semicircular bell. Rebuilt a balanced curved bell with a smooth blade-root junction and aligned diagonal grip.\nSymbol plan: typed contours, shared radii and exact attachment nodes; paired features use common dimensions.\nConstruction: No useful direct Lucide bell-guard match; supplied silhouette. Keyshape SQUARE; any proportional departure is recorded as an exact-drawing exception.'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='8a647e0e-f452-4aea-8ac1-7d82ccfdd824'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__diagonal-epee-with-bell-guard/20260928T173023Z-thuan-mac/reference/epee_8a647e0e-f452-4aea-8ac1-7d82ccfdd824.svg'
AUTHOR="gpt-6"
PARENT_MODULE='icon_set/work/primitive-fix-thuan/solo__diagonal-epee-with-bell-guard/20260928T173023Z-thuan-mac/before/diagonal_epee_with_bell_guard_8a647e0e_f452_4aea_8ac1_7d82ccfdd824.py'
class Drawing(Solo48):
    icon_id='diagonal-epee-with-bell-guard'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category="primitives-generate"
    aliases=()
    keywords=('epee',)

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
        # Rotated bell: two smooth mirrored curve halves meet tangentially at the blade root.
        self.path('guard',(8,24),[('C',(24,24),(12,20),(20,20)),('C',(24,40),(28,28),(28,36)),('L',(16,32)),('L',(8,24))],True)
        self.add_line('blade',(24,24),(42,6));self.relate('connect','guard','blade')
        self.add_line('grip',(16,32),(6,42));self.relate('connect','guard','grip')
