'The tape was too short, and all ruler ticks were missing. Lengthened the extended tape, enlarged the housing hub and restored two measurement ticks.\nSymbol plan: shared dimensions, repeated components and explicit actual attachment nodes.\nConstruction: Lucide ruler.\nKeyshape HRECT_L; intentional source proportions recorded separately when outside the nominal envelope.'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='7bda009e-9307-44d2-81d1-0e1d95fcd9f0'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__retractable-measuring-tape-tool/20260928T171810Z-thuan-mac/reference/tape measure_7bda009e-9307-44d2-81d1-0e1d95fcd9f0.svg'
AUTHOR="gpt-6"
PARENT_MODULE='icon_set/work/primitive-fix-thuan/solo__retractable-measuring-tape-tool/20260928T171810Z-thuan-mac/before/retractable_measuring_tape_tool_7bda009e_9307_44d2_81d1_0e1d95fcd9f0.py'
class Drawing(Solo48):
    icon_id='retractable-measuring-tape-tool'
    keyshape=Keyshape.HRECT_L
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
        # Housing and tape share both attachment nodes; two ruler ticks are visible.
        self.path('housing',(11,8),[('L',(19,8)),('A',(27,16),8,8,True),('L',(27,28)),('L',(27,40)),('L',(7,40)),('A',(3,36),4,4,True),('L',(3,16)),('A',(11,8),8,8,True)],True)
        self.circle('hub',15,22,6)
        self.add_polyline('tape',(27,28),(45,28),(45,40),(39,40),(33,40),(27,40))
        self.relate('connect','housing','tape')
        for x in (33,40):
            self.add_line(f'tick-{x}',(x,40),(x,36));self.relate('connect','tape',f'tick-{x}')

# Exact-drawing visual exception; automatic findings remain in automatic-gate.json.
Drawing.exception = {'reason': 'User authorized agent-selected exceptions in this task. The restored measurement ticks use 2px ink gaps inside a longer tape; the enlarged circular hub retains 2px wall clearance. Expanded horizontal bounds leave 1px canvas margins.', 'approved_by': 'user-authorized-agent', 'approved_on': '2026-09-29', 'svg_sha256': '96dd995de4d320db05cd1530ad6e56b33b7fd1a88104cef1a3f47bdc1ab8db16'}
