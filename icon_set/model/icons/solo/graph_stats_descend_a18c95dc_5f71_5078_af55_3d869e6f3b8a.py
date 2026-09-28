"""Three exact diagonal graph segments; descending legs at 45 degrees and equal arrowhead arms.
Omissions: None
Construction references: ['trending-down'].
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'a18c95dc-5f71-5078-af55-3d869e6f3b8a'
SOURCE_PATH = 'pictographic-primitives/interface-essential/graph stats descend_a18c95dc-5f71-5078-af55-3d869e6f3b8a.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='graph-stats-descend'
    keyshape=Keyshape.HRECT_M
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "interface-essential"
    categories = ("interface-essential", "primitives")
    aliases=()
    keywords=('graph', 'stats', 'descend')

    def path(self, name, start, commands, closed=False):
        ids=[]; here=start
        for i,c in enumerate(commands):
            eid=f'{name}-{i}'; ids.append(eid)
            if c[0]=='L': self.add_line(eid,here,c[1])
            elif c[0]=='A': self.add_arc(eid,here,c[1],radius_x=c[2],radius_y=c[3],sweep=c[4],large_arc=c[5] if len(c)>5 else False)
            elif c[0]=='C': self.add_bezier(eid,here,(c[2],c[3],c[1]))
            here=c[1]
        self.add_contour(name,*ids,closed=closed)
    def circle(self,n,x,y,r):
        self.path(n,(x-r,y),[('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True)],True)
    def box(self,n,x,y,w,h,r):
        self.path(n,(x+r,y),[('L',(x+w-r,y)),('A',(x+w,y+r),r,r,True),('L',(x+w,y+h-r)),('A',(x+w-r,y+h),r,r,True),('L',(x+r,y+h)),('A',(x,y+h-r),r,r,True),('L',(x,y+r)),('A',(x+r,y),r,r,True)],True)

    def build(self):
        self.add_polyline('trend',(4,10),(22,28),(28,22),(44,38))
        self.add_polyline('arrow',(32,38),(44,38),(44,26))
        self.relate('connect','trend','arrow')
