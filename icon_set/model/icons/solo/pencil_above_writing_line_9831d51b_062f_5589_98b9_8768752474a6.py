"""Pencil above Writing Line.
Plan: Diagonal pencil outline, cap seam and separated writing line; omit barrel facet. Extremes (6,6)-(42,42).
Lucide original and atomic-debug: pencil-line.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '9831d51b-062f-5589-98b9-8768752474a6'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/pencil edit_9831d51b-062f-5589-98b9-8768752474a6.svg'
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
    icon_id = 'pencil-above-writing-line'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/interface-essential"
    aliases = ()
    keywords = ('pencil', 'write', 'line', 'edit', 'stationery', 'tip')
    def build(self):
        path(self,"pencil",(6,32),[("L",(10,20)),("L",(18,12)),("L",(24,6)),("C",(26,6),(28,6),(30,8)),("L",(34,12)),("C",(36,14),(36,16),(34,18)),("L",(29,23)),("L",(20,32)),("L",(6,32))],True)
        self.add_line("cap-seam",(18,12),(29,23));self.relate("connect","pencil","cap-seam")
        self.add_line("writing-line",(18,42),(42,42))
