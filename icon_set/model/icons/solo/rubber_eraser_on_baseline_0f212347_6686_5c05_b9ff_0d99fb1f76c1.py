"""Rubber Eraser on Baseline.
Plan: Diagonal rounded eraser with transverse band and baseline at shared lower edge. Extremes(6,6)-(42,42).
Lucide original and atomic-debug: eraser.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '0f212347-6686-5c05-b9ff-0d99fb1f76c1'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/eraser_0f212347-6686-5c05-b9ff-0d99fb1f76c1.svg'
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
    icon_id = 'rubber-eraser-on-baseline'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "interface-essential"
    aliases = ()
    keywords = ('eraser', 'rubber', 'stationery', 'diagonal', 'baseline', 'tool')
    def build(self):
        path(self,"eraser",(16,42),[("C",(14,42),(13,41),(12,40)),("L",(8,36)),("C",(6,34),(6,32),(6,30)),("C",(6,28),(7,27),(8,26)),("L",(12,22)),("L",(26,8)),("C",(28,6),(30,6),(32,6)),("C",(34,6),(35,7),(36,8)),("L",(40,12)),("C",(42,14),(42,16),(42,18)),("C",(42,20),(41,21),(40,22)),("L",(28,34)),("L",(24,38)),("L",(20,42)),("L",(16,42))],True)
        self.add_line("band",(12,22),(28,34));self.relate("connect","eraser","band")
        self.add_line("baseline",(20,42),(42,42));self.relate("connect","eraser","baseline")
