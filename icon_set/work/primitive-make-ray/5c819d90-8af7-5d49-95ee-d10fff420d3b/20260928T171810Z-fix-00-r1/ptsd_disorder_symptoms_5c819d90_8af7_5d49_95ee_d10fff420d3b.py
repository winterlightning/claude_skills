'The profile was blocky, with a flat vertical forehead and heavy lightning-like crack. Restored a sloping forehead/nose, rounded jaw, longer neck and finer three-segment crack at the reference location.\nSymbol plan: shared dimensions, repeated components and explicit actual attachment nodes.\nConstruction: human_ref/user.svg; supplied profile (no useful direct Lucide match).\nKeyshape VRECT_L; intentional source proportions recorded separately when outside the nominal envelope.'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='5c819d90-8af7-5d49-95ee-d10fff420d3b'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__ptsd-disorder-symptoms/20260928T171810Z-thuan-mac/reference/ptsd disorder symptoms_5c819d90-8af7-5d49-95ee-d10fff420d3b.svg'
AUTHOR="gpt-6"
PARENT_MODULE='icon_set/work/primitive-fix-thuan/solo__ptsd-disorder-symptoms/20260928T171810Z-thuan-mac/before/ptsd_disorder_symptoms_5c819d90_8af7_5d49_95ee_d10fff420d3b.py'
class Drawing(Solo48):
    icon_id='ptsd-disorder-symptoms'
    keyshape=Keyshape.VRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category="primitives-generate"
    aliases=()
    keywords=('ptsd', 'disorder', 'symptoms')

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
        # Continuous neck and profile; no detached-head gap applies.
        self.path('profile',(13,44),[('L',(13,34)),('C',(8,23),(13,30),(8,28)),('L',(8,20)),('C',(16,6),(8,14),(11,9)),('C',(24,4),(18,5),(21,4)),('C',(36,13),(30,4),(34,7)),('L',(40,25)),('L',(36,26)),('L',(36,32)),('A',(30,38),6,6,True),('L',(28,38)),('L',(28,44))])
        self.add_polyline('crack',(16,6),(22,13),(18,17),(21,20))
        self.relate('connect','profile','crack')
