"""Location Pin above Baseline.
Plan: Symmetric teardrop with circular opening and detached baseline. Extremes (8,4)-(40,44).
Construction reference: local Lucide map-pin, original and atomic-debug.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'f442e678-6fbd-570e-923f-8eae8fd127e0'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/pin_f442e678-6fbd-570e-923f-8eae8fd127e0.svg'
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
    icon_id = 'location-pin-above-baseline'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/interface-essential"
    aliases = ()
    keywords = ('pin', 'map', 'location', 'marker', 'place', 'navigation')
    def build(self):
        path(self,"pin",(8,20),[("A",16,16,True,(40,20)),("C",(40,26),(30,32),(24,36)),("C",(18,32),(8,26),(8,20))],True)
        circle(self,"opening",24,19,4)
        self.add_line("baseline",(14,44),(34,44))
