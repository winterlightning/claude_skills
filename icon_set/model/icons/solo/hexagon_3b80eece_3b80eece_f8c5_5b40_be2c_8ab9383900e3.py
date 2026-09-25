"""Upright hexagon. Lucide hexagon informs shared symmetry axes and equal corner treatment. Six true straight edges replace fragmented fitting nodes. Both x24 and y24 symmetry; no omissions.
Keyshape VRECT_L: exact SOLO48 envelope; 4px stroke.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '3b80eece-f8c5-5b40-be2c-8ab9383900e3'
SOURCE_PATH = 'pictographic-primitives/design/hexagon_3b80eece-f8c5-5b40-be2c-8ab9383900e3.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='hexagon-3b80eece'
    keyshape=Keyshape.VRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category="design"
    aliases=()
    keywords=('hexagon', '3b80eece')

    def build(self):
        self.add_polyline('hexagon',(24,4),(40,14),(40,34),(24,44),(8,34),(8,14),closed=True)

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
