"""Rolling Edit Arrows.
Plan: Two repeated double arrows share a split center upright. Extremes(6,6)-(42,42).
Lucide original and atomic-debug: move-horizontal.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '0a3ced66-db45-5ef5-a64e-09400825a99c'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/rolling edit tool_0a3ced66-db45-5ef5-a64e-09400825a99c.svg'
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
    icon_id = 'rolling-edit-arrows'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "interface-essential"
    categories = ("interface-essential", "primitives")
    aliases = ()
    keywords = ('edit', 'rolling', 'arrows', 'double', 'horizontal', 'divider')
    def build(self):
        ys=[6,14,34,42]
        for i in range(3):self.add_line(f"upright-{i}",(24,ys[i]),(24,ys[i+1]))
        for i in range(2):self.relate("connect",f"upright-{i}",f"upright-{i+1}")
        for row,y in enumerate([14,34]):
            self.add_polyline(f"shaft-{row}",(6,y),(24,y),(42,y))
            for j in [row,row+1]:self.relate("connect",f"shaft-{row}",f"upright-{j}")
            for side,x in enumerate([6,42]):
                back=x+(6 if side==0 else -6);n=f"head-{row}-{side}"
                self.add_polyline(n,(back,y-6),(x,y),(back,y+6));self.relate("connect",n,f"shaft-{row}")
