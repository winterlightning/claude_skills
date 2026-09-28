"""Notification Bell.
Plan: Mirrored flaring bell silhouette, gently pointed crown and detached semicircular clapper. Extremes (8,4)-(40,44).
Construction reference: local Lucide bell, original and atomic-debug.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '072a73b7-1a6e-4972-9c99-c1bf69a5e759'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/alarm bell_072a73b7-1a6e-4972-9c99-c1bf69a5e759.svg'
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
    icon_id = 'notification-bell-reference-072a73b7-1a6e-4972-9c99-c1bf69a5e759'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "interface-essential"
    categories = ("interface-essential", "primitives")
    aliases = ()
    keywords = ('bell', 'notification', 'alert', 'alarm', 'clapper', 'ring')
    def build(self):
        # Shared crown axis, wall offset and clapper radius own both halves.
        cx=24
        left,right=cx-12,cx+12
        path(self,"bell",(cx,4),[("C",(cx-6,7),(left,7),(left,16)),("C",(left,23),(cx-14,27),(cx-16,30)),("L",(cx+16,30)),("C",(cx+14,27),(right,23),(right,16)),("C",(right,7),(cx+6,7),(cx,4))],True)
        self.add_arc("clapper",(cx-6,39),(cx+6,39),radius_x=6,radius_y=5,sweep=False)
