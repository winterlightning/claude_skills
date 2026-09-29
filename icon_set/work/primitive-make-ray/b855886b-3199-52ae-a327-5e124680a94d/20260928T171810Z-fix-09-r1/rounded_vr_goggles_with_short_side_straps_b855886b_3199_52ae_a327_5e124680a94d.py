'The visor was too tall, nearly square, and its nose opening too deep. Restored a broad low visor, shallow smooth nose notch and short balanced side straps.\nSymbol plan: shared dimensions, repeated components and explicit actual attachment nodes.\nConstruction: Lucide glasses: mirrored contour balance.\nKeyshape HRECT_M; intentional source proportions recorded separately when outside the nominal envelope.'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='b855886b-3199-52ae-a327-5e124680a94d'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__rounded-vr-goggles-with-short-side-straps/20260928T171810Z-thuan-mac/reference/device wearable vr goggles_b855886b-3199-52ae-a327-5e124680a94d.svg'
AUTHOR="gpt-6"
PARENT_MODULE='icon_set/work/primitive-fix-thuan/solo__rounded-vr-goggles-with-short-side-straps/20260928T171810Z-thuan-mac/before/rounded_vr_goggles_with_short_side_straps_b855886b_3199_52ae_a327_5e124680a94d.py'
class Drawing(Solo48):
    icon_id='rounded-vr-goggles-with-short-side-straps'
    keyshape=Keyshape.HRECT_M
    semantic_role="MAIN"
    semantic_kind="noun"
    category="primitives-generate"
    aliases=()
    keywords=('device', 'wearable', 'vr', 'goggles')

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
        # Low, broad visor with mirrored tangent transitions into a shallow nose notch.
        self.path('visor',(15,14),[('L',(33,14)),('A',(40,21),7,7,True),('L',(40,24)),('L',(40,27)),('A',(33,34),7,7,True),('L',(30,34)),('C',(24,29),(27,34),(27,29)),('C',(18,34),(21,29),(21,34)),('L',(15,34)),('A',(8,27),7,7,True),('L',(8,24)),('L',(8,21)),('A',(15,14),7,7,True)],True)
        for n,a,b in [('left-strap',(4,24),(8,24)),('right-strap',(40,24),(44,24))]:
            self.add_line(n,a,b);self.relate('connect','visor',n)

# Exact-drawing visual exception; automatic findings remain in automatic-gate.json.
Drawing.exception = {'reason': 'User authorized agent-selected exceptions in this task. The source visor is substantially flatter than the standard horizontal keyshapes. The broad low visor and shallow smooth nose notch preserve its wearable-device proportions.', 'approved_by': 'user-authorized-agent', 'approved_on': '2026-09-29', 'svg_sha256': 'beec71b89ecb3570d36f68563de67a8a6acb7dff6cab3d87f2b5efa6eb940c35'}
