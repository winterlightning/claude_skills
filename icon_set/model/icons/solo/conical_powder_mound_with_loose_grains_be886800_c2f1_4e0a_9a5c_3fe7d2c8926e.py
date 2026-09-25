"""Conical cornmeal mound with two loose grains. Smooth symmetric mound about x20, straight base; grains preserve intentional asymmetry. No useful exact Lucide match. Irregular grain contours simplified to one small circle and one dot.
Keyshape HRECT_M: exact SOLO48 envelope; 4px stroke.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'be886800-c2f1-4e0a-9a5c-3fe7d2c8926e'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_13/cornmeal_be886800-c2f1-4e0a-9a5c-3fe7d2c8926e.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='conical-powder-mound-with-loose-grains'
    keyshape=Keyshape.HRECT_M
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects/reference"
    aliases=()
    keywords=('conical', 'powder', 'mound', 'with', 'loose', 'grains')

    def build(self):
        self.path('mound',(4,38),[('C',(20,16),(10,30),(16,16)),('C',(36,38),(24,16),(30,30)),('L',(4,38))],True)
        self.circle('grain',40,13,3);self.add_dot('small-grain',(44,27))

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
