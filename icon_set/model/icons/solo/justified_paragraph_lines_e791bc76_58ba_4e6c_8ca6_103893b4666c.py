"""Justified paragraph reduced to exactly three lines as reviewer requested. Shared y step14 and left edge4; last line shorter as original. No useful local align-justify match found.
Keyshape HRECT_M: exact SOLO48 envelope; 4px stroke.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'e791bc76-58ba-4e6c-8ca6-103893b4666c'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/paragraph justified align_e791bc76-58ba-4e6c-8ca6-103893b4666c.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='justified-paragraph-lines'
    keyshape=Keyshape.HRECT_M
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "interface-essential"
    aliases=()
    keywords=('justified', 'paragraph', 'lines')

    def build(self):
        for i,width in enumerate((40,40,28)):
            y=10+14*i;self.add_line(f'row-{i}',(4,y),(4+width,y))

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
