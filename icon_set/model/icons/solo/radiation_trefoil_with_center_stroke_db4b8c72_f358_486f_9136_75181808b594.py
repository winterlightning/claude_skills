"""Radiation Trefoil with Center Stroke.
Plan: Three annular sectors, mirrored upper pair, radii20 and10, shared center(24,24). Radial extreme20.
Lucide original and atomic-debug: radiation.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'db4b8c72-f358-486f-9136-75181808b594'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/radioactive_db4b8c72-f358-486f-9136-75181808b594.svg'
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
    icon_id = 'radiation-trefoil-with-center-stroke'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "interface-essential"
    aliases = ()
    keywords = ('radiation', 'trefoil', 'hazard', 'nuclear', 'warning', 'sectors')
    def build(self):
        for i in range(2):
            def p(x,y):return (x,y) if i==0 else (48-x,y)
            path(self,f"upper-sector-{i}",p(4,24),[("A",20,20,i==0,p(12,8)),("L",p(18,16)),("A",10,10,i!=0,p(14,24)),("L",p(4,24))],True)
        path(self,"lower-sector",(36,40),[("A",20,20,True,(12,40)),("L",(18,32)),("A",10,10,False,(30,32)),("L",(36,40))],True)
        self.add_line("center-stroke",(24,23),(24,25))
