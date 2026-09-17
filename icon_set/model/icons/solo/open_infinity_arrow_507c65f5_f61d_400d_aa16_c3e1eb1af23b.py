"""Open Infinity Arrow.
Plan: Open flowing figure-eight with arrow at upper-left return and a detached lower-right return. Extremes (4,8)-(44,40).
Construction reference: local Lucide infinity, original and atomic-debug.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '507c65f5-f61d-400d-aa16-c3e1eb1af23b'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/loop arrow_507c65f5-f61d-400d-aa16-c3e1eb1af23b.svg'
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
    icon_id = 'open-infinity-arrow'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/interface-essential"
    aliases = ()
    keywords = ('infinity', 'loop', 'arrow', 'repeat', 'continuous', 'cycle')
    def build(self):
        path(self,"loop",(30,32),[("C",(35,40),(44,36),(44,24)),("C",(44,14),(40,8),(34,8)),("C",(29,8),(28,19),(24,24)),("C",(20,29),(19,40),(14,40)),("C",(8,40),(4,34),(4,24)),("C",(4,14),(8,8),(14,8)),("C",(17,8),(18,12),(20,16))])
        self.add_polyline("arrowhead",(12,16),(20,16),(20,8))
        self.relate("connect","loop","arrowhead")
