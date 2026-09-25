"""Right Triangle beside Upright Lines.
Plan: Two equal uprights at8-unit spacing and a hollow right triangle. Extremes(6,6)-(42,42).
Lucide original and atomic-debug: columns-3.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'b596e3ba-3ceb-5728-98b4-7e47abf52870'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/increase quote level_b596e3ba-3ceb-5728-98b4-7e47abf52870.svg'
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
    icon_id = 'right-triangle-beside-upright-lines'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "interface-essential"
    aliases = ()
    keywords = ('indent', 'right', 'triangle', 'arrow', 'lines', 'format')
    def build(self):
        for i in range(2):self.add_line(f"upright-{i}",(6+8*i,6),(6+8*i,42))
        self.add_polyline("triangle",(24,12),(42,24),(24,36),closed=True)
