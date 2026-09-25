"""Nine to Five Clock Arrow.
Plan: Open clockwise arc owns the lower-right arrowhead; short joined clock hands. Extremes (6,6)-(42,42).
Construction reference: local Lucide clock, original and atomic-debug.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'd8a1922d-b402-4d9d-95d0-705bdf3e919b'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/time nine to five 3_d8a1922d-b402-4d9d-95d0-705bdf3e919b.svg'
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

def box(icon,name,x,y,w,h,r=2):
    path(icon,name,(x+r,y),[("L",(x+w-r,y)),("A",r,r,True,(x+w,y+r)),("L",(x+w,y+h-r)),("A",r,r,True,(x+w-r,y+h)),("L",(x+r,y+h)),("A",r,r,True,(x,y+h-r)),("L",(x,y+r)),("A",r,r,True,(x+r,y))],True)

class Drawing(Solo48):
    icon_id = 'nine-to-five-clock-arrow'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "interface-essential"
    aliases = ()
    keywords = ('clock', 'time', 'arrow', 'hours', 'cycle', 'work')
    def build(self):
        path(self,"rim",(6,24),[("A",18,18,True,(42,24)),("C",(42,33),(40,39),(34,42))])
        self.add_polyline("arrowhead",(34,32),(34,42),(42,42))
        self.relate("connect","rim","arrowhead")
        self.add_polyline("hands",(16,24),(24,24),(27,28))
