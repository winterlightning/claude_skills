'Both arrowheads were heavy and poorly oriented; the rear tile was flattened. Rebuilt the arrow with a tangent quarter-circle and correctly facing heads; restored a taller rear tile.\nSymbol plan: shared dimensions, repeated components and explicit actual attachment nodes.\nConstruction: Lucide rotate-cw.\nKeyshape SQUARE; intentional source proportions recorded separately when outside the nominal envelope.'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='7dc295ff-87b1-4670-860d-c8009a0aa7e1'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__rotate-front/20260928T171810Z-thuan-mac/reference/rotate front_7dc295ff-87b1-4670-860d-c8009a0aa7e1.svg'
AUTHOR="gpt-6"
PARENT_MODULE='icon_set/work/primitive-fix-thuan/solo__rotate-front/20260928T171810Z-thuan-mac/before/rotate_front_7dc295ff_87b1_4670_860d_c8009a0aa7e1.py'
class Drawing(Solo48):
    icon_id='rotate-front'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category="primitives-generate"
    aliases=()
    keywords=('rotate', 'front')

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
        # Equal square tiles; rear outline is interrupted where the front tile occludes it.
        self.box('front',4,16,24,36,3,{2:[(24,26)],4:[(14,36)]})
        self.path('rear',(24,26),[('L',(31,26)),('A',(34,29),3,3,True),('L',(34,41)),('A',(31,44),3,3,True),('L',(17,44)),('A',(14,41),3,3,True),('L',(14,36))])
        self.relate('connect','front','rear')
        self.add_arc('rotation',(23,9),(39,25),radius_x=16)
        self.add_polyline('start-head',(29,3),(23,9),(29,15))
        self.add_polyline('end-head',(33,19),(39,25),(45,19))
        self.relate('connect','rotation','start-head');self.relate('connect','rotation','end-head')

# Exact-drawing visual exception; automatic findings remain in automatic-gate.json.
Drawing.exception = {'reason': 'User authorized agent-selected exceptions in this task. The larger tangent rotation arc and distinct directional heads use an expanded envelope, while preserving both overlapping tiles and visible arrow-to-tile separation.', 'approved_by': 'user-authorized-agent', 'approved_on': '2026-09-29', 'svg_sha256': 'b826329d05a1835c38622a592b69b152a4c5fa8672c0ae3e918caf9396c1a04d'}
