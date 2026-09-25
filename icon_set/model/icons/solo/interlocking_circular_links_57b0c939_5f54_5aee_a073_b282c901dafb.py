"""Interlocking Circular Links.
Plan: Two interrupted rounded rings on a lower-left to upper-right diagonal. Extremes (6,6)-(42,42).
Construction reference: local Lucide link, original and atomic-debug.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '57b0c939-5f54-5aee-a073-b282c901dafb'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/hyperlink circle_57b0c939-5f54-5aee-a073-b282c901dafb.svg'
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

class Drawing(Solo48):
    icon_id = 'interlocking-circular-links'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "interface-essential"
    categories = ("interface-essential", "primitives")
    aliases = ()
    keywords = ('links', 'chain', 'circles', 'join', 'connection', 'hyperlink')
    def build(self):
        path(self,"lower",(28,20),[("C",(24,18),(21,18),(18,18)),("A",12,12,False,(6,30)),("A",12,12,False,(18,42)),("C",(22,42),(24,40),(26,38))])
        path(self,"upper",(22,10),[("C",(24,8),(26,6),(30,6)),("A",12,12,True,(42,18)),("A",12,12,True,(30,30)),("C",(27,30),(24,30),(20,28))])
