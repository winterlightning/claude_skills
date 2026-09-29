'The arm collapsed into a thin pole and tiny triangular foot; the claw did not match the source. Restored the flared pedestal, outlined arm, round elbow and wide curved claw above the box.\nSymbol plan: shared dimensions, repeated components and explicit actual attachment nodes.\nConstruction: No useful direct Lucide robot-arm match; source geometric construction.\nKeyshape SQUARE; intentional source proportions recorded separately when outside the nominal envelope.'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='f5f94845-109c-419b-b80e-b9dfc0c95900'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__robotic-gripper-above-box/20260928T171810Z-thuan-mac/reference/factory robot arm box_f5f94845-109c-419b-b80e-b9dfc0c95900.svg'
AUTHOR="gpt-6"
PARENT_MODULE='icon_set/work/primitive-fix-thuan/solo__robotic-gripper-above-box/20260928T171810Z-thuan-mac/before/robotic_gripper_above_box_f5f94845_109c_419b_b80e_b9dfc0c95900.py'
class Drawing(Solo48):
    icon_id='robotic-gripper-above-box'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category="primitives-generate"
    aliases=()
    keywords=('factory', 'robot', 'arm', 'box')

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
        # Circular elbow, flared pedestal, outlined horizontal arm and open curved claw.
        self.node('elbow',12,10,5,[(4,-3),(4,3),(-3,4),(3,4)])
        self.path('pedestal',(9,14),[('L',(9,32)),('C',(4,44),(9,37),(6,42)),('L',(24,44)),('C',(15,32),(22,42),(15,37)),('L',(15,14))])
        self.relate('connect','elbow','pedestal')
        self.add_polyline('arm',(16,7),(36,7),(36,13),(16,13))
        self.relate('connect','arm','elbow')
        self.add_line('forearm',(36,13),(36,19));self.relate('connect','forearm','arm')
        self.path('gripper',(30,28),[('L',(28,26)),('A',(36,18),8,8,True),('A',(44,26),8,8,True),('L',(42,28))])
        # Forearm meets the crown at y18.
        self.add_line('wrist',(36,19),(36,18));self.relate('connect','forearm','wrist');self.relate('connect','wrist','gripper')
        self.add_polyline('box',(30,34),(44,34),(44,44),(30,44),closed=True)
