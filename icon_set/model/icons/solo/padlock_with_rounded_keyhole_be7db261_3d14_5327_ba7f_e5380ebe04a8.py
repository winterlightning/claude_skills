"""Padlock with Rounded Keyhole.
Plan: Mirrored closed shackle, rounded rectangular body, centered keyhole. Extremes (8,4)-(40,44).
Lucide original and atomic-debug construction: lock-keyhole.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'be7db261-3d14-5327-ba7f-e5380ebe04a8'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/lock_be7db261-3d14-5327-ba7f-e5380ebe04a8.svg'
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
    icon_id = 'padlock-with-rounded-keyhole'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "interface-essential"
    aliases = ()
    keywords = ('padlock', 'lock', 'keyhole', 'security', 'shackle', 'closed')
    def build(self):
        cx=24;left=8;right=48-left;top=16;bottom=44
        path(self,"body",(14,top),[("L",(34,top)),("L",(36,top)),("A",4,4,True,(right,20)),("L",(right,40)),("A",4,4,True,(36,bottom)),("L",(12,bottom)),("A",4,4,True,(left,40)),("L",(left,20)),("A",4,4,True,(12,top)),("L",(14,top))],True)
        path(self,"shackle",(14,top),[("L",(14,14)),("A",10,10,True,(34,14)),("L",(34,top))])
        self.relate("connect","body","shackle")
        path(self,"keyhole",(24,33),[("A",3,3,True,(24,27)),("A",3,3,True,(24,33))],True)
        self.add_line("slot",(24,33),(24,35));self.relate("connect","keyhole","slot")
