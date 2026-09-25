"""Megaphone.
Plan: Tapered diagonal horn, rear edge and hanging loop at shared nodes. Extremes (6,6)-(42,42).
Construction reference: local Lucide megaphone, original and atomic-debug.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '265b5a65-5aa8-4bdf-bbf6-682e357fd957'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/megaphone_265b5a65-5aa8-4bdf-bbf6-682e357fd957.svg'
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
    icon_id = 'megaphone-reference-265b5a65-5aa8-4bdf-bbf6-682e357fd957'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "interface-essential"
    aliases = ()
    keywords = ('megaphone', 'announcement', 'horn', 'handle', 'speaker', 'broadcast')
    def build(self):
        self.add_polyline("horn",(6,26),(30,6),(42,26),(30,28),(18,30),(10,32),closed=True)
        path(self,"handle",(18,30),[("C",(18,38),(20,42),(24,42)),("C",(28,42),(30,38),(30,28))])
        self.relate("connect","horn","handle")
