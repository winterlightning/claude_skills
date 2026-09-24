"""A band saw frame with a toothed wheel and base.
Symbol plan: cog: repeated radial teeth and central hole; source determines the nested machine frame.
Reduction: Tooth count reduced to six broad teeth; ledge shortened where occluded by the wheel.
Keyshape: SQUARE; exact bounds are obtained from the model.
"""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
from icon_set.model.profiles import Profile
SOURCE_ICON_ID='f8387852-af8b-4221-a8f7-998fc1b24294'
SOURCE_PATH='icon_set/work/todo-references/band saw_f8387852-af8b-4221-a8f7-998fc1b24294.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='band-saw'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('band', 'saw')
    ink_extremes=keyshape.bounds_for(Profile.SOLO48)
    def build(self):
        self.add_polyline('frame-left',(10,34),(10,12))
        self.add_arc('frame-tl',(10,12),(16,6),radius_x=6)
        self.add_line('frame-top',(16,6),(34,6))
        self.add_arc('frame-tr',(34,6),(40,12),radius_x=6)
        self.add_line('frame-right',(40,12),(40,18))
        self.add_contour('frame','frame-left-1','frame-tl','frame-top','frame-tr','frame-right')
        self.contours=[c for c in self.contours if c.contour_id!='frame-left']
        self.add_polyline('inner',(16,34),(16,14),(32,14),(32,18))
        self.rounded('base',6,34,42,42,3,breaks={0:[(10,34),(16,34)]})
        self.relate('connect','inner','base');self.relate('connect','frame','base')
        self.add_polyline('wheel',(27,18),(33,18),(35,23),(40,22),(42,28),(38,32),(40,37),(34,40),(30,36),(25,38),(21,33),(24,29),(22,24),(27,23),closed=True)
        self.circle('hub',31,29,3)
        self.add_line('ledge',(16,26),(22,26));self.relate('connect','ledge','inner')

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
