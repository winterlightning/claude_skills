'The tape was short and blank, with an overly tall case. Restored a lower, wider case, a longer tape and two spaced measurement ticks.\nSymbol plan: shared dimensions, repeated components and explicit actual attachment nodes.\nConstruction: Lucide ruler.\nKeyshape HRECT_M; intentional source proportions recorded separately when outside the nominal envelope.'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='89fb6fa1-89d3-4277-a364-d6e026cea6f2'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__retractable-tape-measure/20260928T171810Z-thuan-mac/reference/tape measure_89fb6fa1-89d3-4277-a364-d6e026cea6f2.svg'
AUTHOR="gpt-6"
PARENT_MODULE='icon_set/work/primitive-fix-thuan/solo__retractable-tape-measure/20260928T171810Z-thuan-mac/before/retractable_tape_measure_89fb6fa1_89d3_4277_a364_d6e026cea6f2.py'
class Drawing(Solo48):
    icon_id='retractable-tape-measure'
    keyshape=Keyshape.HRECT_M
    semantic_role="MAIN"
    semantic_kind="noun"
    category="primitives-generate"
    aliases=()
    keywords=('tape', 'measure')

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

    def build(self):
        # Wider low-profile measure; same shared case/tape construction.
        self.path('housing',(12,10),[('L',(20,10)),('A',(28,18),8,8,True),('L',(28,28)),('L',(28,38)),('L',(8,38)),('A',(4,34),4,4,True),('L',(4,18)),('A',(12,10),8,8,True)],True)
        self.circle('hub',16,23,6)
        self.add_polyline('tape',(28,28),(44,28),(44,38),(40,38),(34,38),(28,38))
        self.relate('connect','housing','tape')
        for x in (34,40):
            self.add_line(f'tick-{x}',(x,38),(x,35));self.relate('connect','tape',f'tick-{x}')
