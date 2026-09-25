"""Opposing Vertical Triangles.
Plan: Vertical pair from one reflected triangle definition. Extremes (8,4)-(40,44).
Lucide original and atomic-debug construction: chevrons-left-right.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '194c7896-d2b7-5216-9507-6c3057e3f666'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/scroll vertical_194c7896-d2b7-5216-9507-6c3057e3f666.svg'
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
    icon_id = 'opposing-vertical-triangles'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "interface-essential"
    aliases = ()
    keywords = ('arrows', 'up', 'down', 'vertical', 'scroll', 'triangles')
    def build(self):
        for i,s in enumerate([-1,1]):
            self.add_polyline(f"triangle-{i}",(8,24+s*5),(24,24+s*20),(40,24+s*5),closed=True)
