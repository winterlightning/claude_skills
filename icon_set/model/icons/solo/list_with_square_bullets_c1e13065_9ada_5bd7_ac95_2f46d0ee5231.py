"""List with Square Bullets.
Plan: Three square bullets of side 8; shared row step 16 and aligned line starts. Extremes (8,4)-(40,44).
Construction reference: local Lucide list, original and atomic-debug.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'c1e13065-9ada-5bd7-ac95-2f46d0ee5231'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/list bullets_c1e13065-9ada-5bd7-ac95-2f46d0ee5231.svg'
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
    icon_id = 'list-with-square-bullets'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/interface-essential"
    aliases = ()
    keywords = ('list', 'bullets', 'squares', 'checklist', 'lines', 'interface')
    def build(self):
        for i in range(3):
            y=4+16*i
            self.add_polyline("bullet-"+str(i),(8,y),(16,y),(16,y+8),(8,y+8),closed=True)
            self.add_line("line-"+str(i),(24,y+4),(40,y+4))
