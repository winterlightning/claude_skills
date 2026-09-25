"""Quarter Segment Stopwatch.
Plan: Quarter dial, attached top plunger and side button, detached radial tick series. Extremes (6,6)-(42,42).
Lucide original and atomic-debug: timer.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'f8f5bbf0-cb73-424c-8e34-7396a91fae9e'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/time stopwatch quarter_f8f5bbf0-cb73-424c-8e34-7396a91fae9e.svg'
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
    icon_id = 'quarter-segment-stopwatch'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "interface-essential"
    categories = ("interface-essential", "primitives")
    aliases = ()
    keywords = ('stopwatch', 'quarter', 'timer', 'time', 'segment', 'dial')
    def build(self):
        path(self,"sector",(24,14),[("C",(29,14),(33,16),(36,20)),("C",(39,24),(40,26),(40,30)),("L",(24,30)),("L",(24,14))],True)
        self.add_line("plunger",(24,6),(24,14));self.add_polyline("plunger-cap",(18,6),(24,6),(30,6));self.relate("connect","plunger","sector");self.relate("connect","plunger","plunger-cap")
        self.add_line("button",(36,20),(40,16));self.add_polyline("button-cap",(38,14),(40,16),(42,18));self.relate("connect","button","sector");self.relate("connect","button","button-cap")
        for i,(a,b) in enumerate([((6,30),(10,30)),((12,40),(14,38)),((24,42),(24,40)),((36,42),(34,40)),((12,18),(14,20))]):self.add_line(f"tick-{i}",a,b)
