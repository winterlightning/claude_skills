"""A bomb with a short fuse and a foreground explosion.
Symbol plan: bomb: round body, short neck and curved fuse.
Reduction: Explosion reduced to five broad points; shell is interrupted where hidden by the burst.
Keyshape: SQUARE; exact bounds are obtained from the model.
"""
from ._base import Solo48
from ...keyshapes import Keyshape
from icon_set.model.profiles import Profile
SOURCE_ICON_ID='bf3695d0-7417-50cb-93e5-008403f18c82'
SOURCE_PATH='icon_set/work/todo-references/bomb explode_bf3695d0-7417-50cb-93e5-008403f18c82.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='bomb-explode'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'war'
    aliases=()
    keywords=('bomb', 'explode')
    ink_extremes=keyshape.bounds_for(Profile.SOLO48)
    def build(self):
        self.add_arc('shell-left',(14,39),(14,15),radius_x=8,radius_y=12)
        self.add_polyline('neck',(14,15),(16,11),(21,11),(24,11),(24,17))
        self.add_bezier('shell-right',(24,17),((28,19),(29,22),(29,24)))
        self.relate('connect','shell-left','neck');self.relate('connect','shell-right','neck')
        self.add_bezier('fuse',(21,11),((21,8),(23,6),(26,6)),((32,6),(32,12),(39,12)))
        self.relate('connect','fuse','neck')
        self.add_polyline('burst',(29,24),(33,30),(42,27),(37,34),(42,40),(33,38),(28,42),(27,35),(19,32),(27,30),closed=True)
        self.relate('connect','shell-right','burst')

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


    def browser(self):
        self.rounded('window',8,4,40,44,4,breaks={2:[(40,12)],6:[(8,12)]})
        self.add_line('header',(8,12),(40,12));self.relate('connect','header','window')

    def dollar(self,x,y):
        self.add_bezier('dollar',(x+4,y-6),((x+2,y-7),(x+1,y-7),(x,y-7)),((x-7,y-7),(x-7,y),(x,y)),((x+7,y),(x+7,y+7),(x,y+7)),((x-1,y+7),(x-2,y+7),(x-4,y+6)))
        self.add_line('stem-top',(x,y-8),(x,y-7));self.relate('connect','dollar','stem-top')
        self.add_line('stem-bottom',(x,y+7),(x,y+8));self.relate('connect','dollar','stem-bottom')

    def euro(self,x):
        self.add_bezier('euro',(x+3,22),((x-2,19),(x-8,21),(x-8,28)),((x-8,35),(x-2,37),(x+3,34)))
        self.add_polyline('crossbar',(x-11,28),(x-8,28),(x,28));self.relate('connect','euro','crossbar')
