"""Round Skull.
Plan: Broad rounded cranium, mirrored cheek curves, circular eye pair and four jaw/teeth strokes. Extremes(4,8)-(44,40).
Lucide original and atomic-debug: skull.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'b8db3bb2-1f4b-49d9-b96b-c7a0fabc4886'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/skull_b8db3bb2-1f4b-49d9-b96b-c7a0fabc4886.svg'
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
    icon_id = 'round-skull'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/interface-essential"
    aliases = ()
    keywords = ('skull', 'head', 'bones', 'eyes', 'anatomy', 'skeleton')
    def build(self):
        path(self,"skull",(11,36),[("L",(11,34)),("C",(6,31),(4,29),(4,24)),("C",(4,15),(13,8),(24,8)),("C",(35,8),(44,15),(44,24)),("C",(44,29),(42,31),(37,34)),("L",(37,36))])
        for i,s in enumerate([-1,1]):
            circle(self,f"eye-{i}",24+s*7,22,3)
            self.add_line(f"tooth-{i}",(24+s*4,36),(24+s*4,40))
