"""An empty horizontal battery with a projecting positive terminal.
Symbol plan: battery: rounded body and right terminal.
Reduction: None.
Keyshape: HRECT_M; exact bounds are obtained from the model.
"""
from ._base import Solo48
from ...keyshapes import Keyshape
from icon_set.model.profiles import Profile
SOURCE_ICON_ID='ba844de8-52e9-42c8-a701-c100623e1e4e'
SOURCE_PATH='icon_set/work/todo-references/battery 1_ba844de8-52e9-42c8-a701-c100623e1e4e.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='battery-1-solo'
    keyshape=Keyshape.HRECT_M
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'primitives-generate'
    aliases=()
    keywords=('battery', '1')
    ink_extremes=keyshape.bounds_for(Profile.SOLO48)
    def build(self):
        self.rounded('body',4,10,36,38,4,breaks={2:[(36,18),(36,30)]})
        self.add_line('terminal-top',(36,18),(41,18))
        self.add_arc('terminal-tr',(41,18),(44,21),radius_x=3)
        self.add_line('terminal-right',(44,21),(44,27))
        self.add_arc('terminal-br',(44,27),(41,30),radius_x=3)
        self.add_line('terminal-bottom',(41,30),(36,30))
        self.add_contour('terminal','terminal-top','terminal-tr','terminal-right','terminal-br','terminal-bottom')
        self.relate('connect','terminal','body')

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
