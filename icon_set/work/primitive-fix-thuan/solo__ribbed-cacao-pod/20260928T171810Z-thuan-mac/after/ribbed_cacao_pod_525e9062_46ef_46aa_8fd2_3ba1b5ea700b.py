'The cacao pod was squat and onion-shaped. Restored a tall pointed pod with two long bowed ribs and a curved stem.\nSymbol plan: shared dimensions, repeated components and explicit actual attachment nodes.\nConstruction: Lucide leaf: coherent long curves.\nKeyshape VRECT_M; intentional source proportions recorded separately when outside the nominal envelope.'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='525e9062-46ef-46aa-8fd2-3ba1b5ea700b'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__ribbed-cacao-pod/20260928T171810Z-thuan-mac/reference/cacao_525e9062-46ef-46aa-8fd2-3ba1b5ea700b.svg'
AUTHOR="gpt-6"
PARENT_MODULE='icon_set/work/primitive-fix-thuan/solo__ribbed-cacao-pod/20260928T171810Z-thuan-mac/before/ribbed_cacao_pod_525e9062_46ef_46aa_8fd2_3ba1b5ea700b.py'
class Drawing(Solo48):
    icon_id='ribbed-cacao-pod'
    keyshape=Keyshape.VRECT_M
    semantic_role="MAIN"
    semantic_kind="noun"
    category="primitives-generate"
    aliases=()
    keywords=('cacao',)

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
        # Long pointed pod with two bowed ribs, mirrored around x24.
        self.path('pod',(24,10),[('C',(34,27),(30,15),(34,21)),('C',(24,44),(34,33),(30,39)),('C',(14,27),(18,39),(14,33)),('C',(24,10),(14,21),(18,15))],True)
        for side in (-1,1):
            n=f'rib-{side}';x=24+side*5
            self.path(n,(24,10),[('C',(24,44),(x,18),(x,36))]);self.relate('connect','pod',n)
        self.relate('connect','rib--1','rib-1')
        self.path('stem',(24,10),[('A',(30,4),6,6,True)]);self.relate('connect','stem','pod')
        for side in (-1,1):self.relate('connect','stem',f'rib-{side}')

# Exact-drawing visual exception; automatic findings remain in automatic-gate.json.
Drawing.exception = {'reason': 'User authorized agent-selected exceptions in this task. The reference cacao pod is naturally narrower than SOLO48 keyshapes. Long pointed ribs and stem remain clearly readable without widening the pod back into an onion shape.', 'approved_by': 'user-authorized-agent', 'approved_on': '2026-09-29', 'svg_sha256': 'c808f0c77392c1f79fd72d2dbff27f977aa41a1c350674b9b9721dd61e02a8cd'}
