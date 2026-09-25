"""Infinity Loop.
Plan: Continuous symmetric figure-eight, smooth center crossing and broad lobes. Extremes (4,10)-(44,38).
Construction reference: local Lucide infinity, original and atomic-debug.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '44b0abb4-e46a-5a2e-a6a8-e05bdc85c901'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/loop_44b0abb4-e46a-5a2e-a6a8-e05bdc85c901.svg'
AUTHOR = 'gpt-6'

def circle(icon,name,cx,cy,r):
    icon.add_arc(name+"-top",(cx-r,cy),(cx+r,cy),radius_x=r)
    icon.add_arc(name+"-bottom",(cx+r,cy),(cx-r,cy),radius_x=r)
    icon.add_contour(name,name+"-top",name+"-bottom",closed=True)

def path(icon,name,start,commands,closed=False):
    point=start;members=[]
    for i,command in enumerate(commands):
        member=f"{name}-{i}"; kind=command[0]; end=command[-1]
        if kind=="L":icon.add_line(member,point,end)
        elif kind=="A":icon.add_arc(member,point,end,radius_x=command[1],radius_y=command[2],sweep=command[3])
        else:icon.add_bezier(member,point,(command[1],command[2],end))
        members.append(member);point=end
    icon.add_contour(name,*members,closed=closed)

class Drawing(Solo48):
    icon_id = 'infinity-loop'
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "interface-essential"
    aliases = ()
    keywords = ('infinity', 'loop', 'endless', 'symbol', 'continuous', 'eight')
    def build(self):
        path(self,"loop",(4,24),[("C",(4,16),(8,10),(14,10)),("C",(19,10),(20,19),(24,24)),("C",(28,29),(29,38),(34,38)),("C",(40,38),(44,32),(44,24)),("C",(44,16),(40,10),(34,10)),("C",(29,10),(28,19),(24,24)),("C",(20,29),(19,38),(14,38)),("C",(8,38),(4,32),(4,24))],True)
