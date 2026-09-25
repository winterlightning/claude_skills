"""An arched gravestone marked RIP on a rectangular plinth.
Symbol plan: No useful exact tombstone original; coherent arch and hand-authored RIP letter contours.
Reduction: None; all three letters retained.
Keyshape: VRECT_L; model supplies exact ink extremes.
"""
from ._base import Solo48
from ...keyshapes import Keyshape
from icon_set.model.profiles import Profile
SOURCE_ICON_ID='c37f6508-e0df-51bf-9da4-8fafc43e3b54'
SOURCE_PATH='icon_set/work/todo-references/death rip_c37f6508-e0df-51bf-9da4-8fafc43e3b54.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='death-rip'
    keyshape=Keyshape.VRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'war'
    aliases=()
    keywords=('death', 'rip')
    ink_extremes=keyshape.bounds_for(Profile.SOLO48)
    def build(self):
        self.add_line('stone-left',(10,36),(10,18))
        self.add_arc('stone-arch',(10,18),(38,18),radius_x=14)
        self.add_line('stone-right',(38,18),(38,36))
        self.add_contour('stone','stone-left','stone-arch','stone-right')
        self.add_polyline('plinth',(8,36),(10,36),(38,36),(40,36),(40,44),(8,44),closed=True);self.relate('connect','stone','plinth')
        for label,x in [('r',16),('p',31)]:
            self.add_polyline(label+'-stem',(x,29),(x,25),(x,19))
            self.add_arc(label+'-bowl',(x,19),(x,25),radius_x=4,radius_y=3)
            self.relate('connect',label+'-stem',label+'-bowl')
        self.add_line('r-leg',(16,25),(21,29));self.relate('connect','r-leg','r-stem');self.relate('connect','r-leg','r-bowl')
        self.add_line('i',(25,19),(25,29))

    def circle(self,name,cx,cy,r):
        pts=[(cx-r,cy),(cx,cy-r),(cx+r,cy),(cx,cy+r),(cx-r,cy)]
        members=[]
        for i,(a,b) in enumerate(zip(pts,pts[1:])):
            m=f'{name}-{i}';self.add_arc(m,a,b,radius_x=r);members.append(m)
        self.add_contour(name,*members,closed=True)

    def rounded(self,name,l,t,r,b,rad,breaks=None):
        pts=[(l+rad,t),(r-rad,t),(r,t+rad),(r,b-rad),(r-rad,b),(l+rad,b),(l,b-rad),(l,t+rad),(l+rad,t)]
        members=[];breaks=breaks or {}
        for i,(a,z) in enumerate(zip(pts,pts[1:])):
            if i%2:
                m=f'{name}-{i}';self.add_arc(m,a,z,radius_x=rad);members.append(m)
            else:
                nodes=[a]+breaks.get(i,[])+[z]
                for j,(start,end) in enumerate(zip(nodes,nodes[1:])):
                    if start==end:continue
                    m=f'{name}-{i}-{j}';self.add_line(m,start,end);members.append(m)
        self.add_contour(name,*members,closed=True)

