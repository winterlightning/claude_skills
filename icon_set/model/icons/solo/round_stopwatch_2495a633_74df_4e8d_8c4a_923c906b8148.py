"""Round Stopwatch.
Plan: Circular face radius15 at(24,29), exact diagonal attachment, top plunger and two joined hands. Radial extreme20 at(24,44).
Lucide original and atomic-debug: timer.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '2495a633-74df-4e8d-8c4a-923c906b8148'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/time stopwatch_2495a633-74df-4e8d-8c4a-923c906b8148.svg'
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
    icon_id = 'round-stopwatch'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "interface-essential"
    categories = ("interface-essential", "primitives")
    aliases = ()
    keywords = ('stopwatch', 'timer', 'clock', 'time', 'button', 'round')
    def build(self):
        path(self,"face",(24,14),[("A",15,15,True,(36,20)),("A",15,15,True,(39,29)),("A",15,15,True,(24,44)),("A",15,15,True,(9,29)),("A",15,15,True,(24,14))],True)
        self.add_line("plunger",(24,6),(24,14));self.add_polyline("top",(18,6),(24,6),(30,6));self.relate("connect","face","plunger");self.relate("connect","top","plunger")
        self.add_line("side",(36,20),(40,17));self.add_polyline("side-cap",(38,15),(40,17),(42,19));self.relate("connect","face","side");self.relate("connect","side","side-cap")
        self.add_polyline("hands",(24,23),(24,29),(28,33))
