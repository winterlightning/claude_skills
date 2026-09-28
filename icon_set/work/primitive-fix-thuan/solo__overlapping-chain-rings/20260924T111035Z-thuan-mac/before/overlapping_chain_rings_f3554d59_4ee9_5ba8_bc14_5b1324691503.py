"""Overlapping Chain Rings.
Plan: Two rounded diagonal rings share exact crossing nodes and a broad central lens. Extremes (6,6)-(42,42).
Lucide original and atomic-debug construction: link.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'f3554d59-4ee9-5ba8-bc14-5b1324691503'
SOURCE_PATH = 'pictographic-primitives/interface-essential/attachment_f3554d59-4ee9-5ba8-bc14-5b1324691503.svg'
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
    icon_id = 'overlapping-chain-rings'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/interface-essential"
    tags = ('sub icon',)
    aliases = ()
    keywords = ('chain', 'rings', 'link', 'attachment', 'connection', 'diagonal')
    def build(self):
        a=(16,16);b=(32,32)
        path(self,"lower-ring",a,[("C",(24,14),(34,24),b),("L",(24,40)),("C",(22,42),(20,42),(18,42)),("C",(12,42),(6,38),(6,32)),("C",(6,28),(10,22),a)],True)
        path(self,"upper-ring",a,[("L",(24,8)),("C",(26,6),(28,6),(30,6)),("C",(36,6),(42,10),(42,16)),("C",(42,20),(38,26),b),("C",(24,34),(14,24),a)],True)
        self.relate("connect","lower-ring","upper-ring")
