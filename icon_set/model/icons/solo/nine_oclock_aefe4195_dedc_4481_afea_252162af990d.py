"""Nine OClock.
Plan: Circular face, two attached hour ticks, and joined hands pointing up and left. Radius 20 about (24,24).
Construction reference: local Lucide clock, original and atomic-debug.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'aefe4195-dedc-4481-afea-252162af990d'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/time clock nine to twelve_aefe4195-dedc-4481-afea-252162af990d.svg'
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
    icon_id = 'nine-oclock'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "interface-essential"
    categories = ("interface-essential", "state")
    aliases = ()
    keywords = ('clock', 'nine', 'time', 'hands', 'face', 'hour')
    def build(self):
        path(self,"rim",(24,4),[("A",20,20,True,(44,24)),("A",20,20,True,(24,44)),("A",20,20,True,(4,24)),("A",20,20,True,(24,4))],True)
        self.add_line("top-tick",(24,4),(24,7))
        self.add_line("left-tick",(4,24),(7,24))
        for tick in ("top-tick","left-tick"):self.relate("connect","rim",tick)
        self.add_polyline("hands",(24,16),(24,24),(16,24))
