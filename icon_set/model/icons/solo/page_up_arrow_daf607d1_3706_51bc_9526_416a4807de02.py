"""Page Up Arrow.
Plan: Shared vertical axis, two bars with equal spacing, connected upward head. Extremes (8,4)-(40,44).
Lucide original and atomic-debug: arrow-up.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'daf607d1-3706-51bc-9526-416a4807de02'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/keyboard page up_daf607d1-3706-51bc-9526-416a4807de02.svg'
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
    icon_id = 'page-up-arrow'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "interface-essential"
    aliases = ()
    keywords = ('page', 'up', 'arrow', 'keyboard', 'navigation', 'crossbars')
    def build(self):
        ys=[4,24,32,44]
        for i in range(3):self.add_line(f"shaft-{i}",(24,ys[i]),(24,ys[i+1]))
        for i in range(2):self.relate("connect",f"shaft-{i}",f"shaft-{i+1}")
        for i,y in enumerate([24,32]):
            self.add_polyline(f"bar-{i}",(12,y),(24,y),(36,y))
            self.relate("connect",f"bar-{i}",f"shaft-{i}");self.relate("connect",f"bar-{i}",f"shaft-{i+1}")
        self.add_polyline("head",(8,20),(24,4),(40,20));self.relate("connect","shaft-0","head")
