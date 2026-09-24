"""A horns hand gesture with three lightning accents.
Symbol plan: hand-metal: rounded raised fingers and folded middle fingers; shared human references supply anatomy principles.
Reduction: Fine palm crease omitted; thumb contour and all three lightning accents retained.
Keyshape: SQUARE; model supplies exact ink extremes.
"""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
from icon_set.model.profiles import Profile
SOURCE_ICON_ID='3a11e17f-1153-59b2-b135-910a41a584c7'
SOURCE_PATH='icon_set/work/todo-references/concert rock_3a11e17f-1153-59b2-b135-910a41a584c7.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='concert-rock'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('concert', 'rock')
    ink_extremes=keyshape.bounds_for(Profile.SOLO48)
    def build(self):
        self.add_arc('index-cap',(12,22),(20,22),radius_x=4)
        self.add_line('index-inner',(20,22),(20,30))
        self.add_arc('middle-knuckle',(20,30),(26,30),radius_x=3)
        self.add_arc('ring-knuckle',(26,30),(32,30),radius_x=3)
        self.add_line('little-inner',(32,30),(32,22))
        self.add_arc('little-cap',(32,22),(40,22),radius_x=4)
        self.add_line('right-palm',(40,22),(40,28))
        self.add_arc('palm-right',(40,28),(26,42),radius_x=14)
        self.add_arc('palm-left',(26,42),(12,28),radius_x=14)
        self.add_line('left-palm',(12,28),(12,22))
        self.add_contour('hand','index-cap','index-inner','middle-knuckle','ring-knuckle','little-inner','little-cap','right-palm','palm-right','palm-left','left-palm')
        self.add_bezier('thumb',(32,34),((28,32),(22,32),(22,35)),((22,38),(27,38),(30,38)))
        self.add_line('fold',(26,30),(26,33));self.relate('connect','fold','hand')
        for n,pts in [('left-bolt',[(6,10),(11,14),(6,14)]),('top-bolt',[(26,6),(22,10),(28,10),(24,14)]),('right-bolt',[(42,8),(36,12),(42,12)])]:self.add_polyline(n,*pts)

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

