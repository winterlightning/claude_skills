"""Partly wrapped chocolate bar. Shared rectangular grid and matching corner radii, with an asymmetric folded wrapper edge from the original. No useful exact Lucide match. Four exposed pieces and wrapper retained.
Keyshape VRECT_L: exact SOLO48 envelope; 4px stroke.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'b591714c-777b-49a0-ad5a-afc8f96f98b0'
SOURCE_PATH = 'pictographic-primitives/food/chocolate bar_b591714c-777b-49a0-ad5a-afc8f96f98b0.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='chocolate-bar'
    keyshape=Keyshape.VRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category="food"
    aliases=()
    keywords=('chocolate', 'bar')

    def build(self):
        self.path('bar',(12,24),[('L',(12,6)),('A',(14,4),2,2,True),('L',(24,4)),('L',(34,4)),('A',(36,6),2,2,True),('L',(36,14)),('L',(36,26))])
        self.add_polyline('grid',(12,14),(24,14),(36,14));self.relate('connect','grid','bar')
        self.add_polyline('divide',(24,4),(24,14),(24,30));self.relate('connect','divide','bar');self.relate('connect','divide','grid')
        self.path('wrapper',(8,24),[('L',(12,24)),('L',(16,24)),('L',(24,30)),('L',(36,26)),('L',(40,26)),('L',(40,40)),('A',(36,44),4,4,True),('L',(12,44)),('A',(8,40),4,4,True),('L',(8,24))],True)
        self.relate('connect','wrapper','bar');self.relate('connect','wrapper','divide')

    def path(self,name,start,commands,closed=False):
        members=[];here=start
        for j,(kind,end,*args) in enumerate(commands):
            eid=f'{name}-{j}'
            if kind=='L':self.add_line(eid,here,end)
            elif kind=='A':self.add_arc(eid,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
            elif kind=='C':self.add_bezier(eid,here,(args[0],args[1],end))
            members.append(eid);here=end
        self.add_contour(name,*members,closed=closed)

    def circle(self,name,x,y,r):
        self.path(name,(x-r,y),[('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True)],True)
