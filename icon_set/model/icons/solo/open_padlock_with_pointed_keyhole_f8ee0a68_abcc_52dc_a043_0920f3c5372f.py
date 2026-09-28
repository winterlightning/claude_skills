"""Open Padlock with Pointed Keyhole.
Plan: Symmetric rounded body, left-attached open arch and centered keyhole. Extremes (8,4)-(40,44).
Lucide original and atomic-debug construction: lock-keyhole-open.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'f8ee0a68-abcc-52dc-a043-0920f3c5372f'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/lock unlock_f8ee0a68-abcc-52dc-a043-0920f3c5372f.svg'
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
    icon_id = 'open-padlock-with-pointed-keyhole'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "interface-essential"
    categories = ("interface-essential", "primitives")
    aliases = ()
    keywords = ('padlock', 'unlock', 'open', 'keyhole', 'security', 'shackle')
    def build(self):
        cx=24;left=8;right=48-left;top=16;bottom=44
        path(self,"body",(14,top),[("L",(34,top)),("L",(36,top)),("A",4,4,True,(right,20)),("L",(right,40)),("A",4,4,True,(36,bottom)),("L",(12,bottom)),("A",4,4,True,(left,40)),("L",(left,20)),("A",4,4,True,(12,top)),("L",(14,top))],True)
        path(self,"shackle",(14,top),[("L",(14,14)),("A",10,10,True,(24,4)),("C",(27,4),(30,5),(32,7))])
        self.relate("connect","body","shackle")
        path(self,"keyhole",(19,30),[("A",5,5,True,(29,30)),("C",(29,32),(26,34),(24,35)),("C",(22,34),(19,32),(19,30))],True)
