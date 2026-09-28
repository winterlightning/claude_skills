"""Paired Circular Refresh Arrows.
Plan: Half-turn repeat owns both clockwise curves and arrowheads. Extremes (6,6)-(42,42).
Lucide original and atomic-debug: refresh-cw.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'c58ba969-79a0-45e7-b451-634d48429c2a'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/refresh arrows_c58ba969-79a0-45e7-b451-634d48429c2a.svg'
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
    icon_id = 'paired-circular-refresh-arrows'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "interface-essential"
    categories = ("interface-essential", "state")
    aliases = ()
    keywords = ('refresh', 'arrows', 'circular', 'cycle', 'clockwise', 'synchronize', 'sub icon')
    def build(self):
        for i in range(2):
            def p(x,y):return (x,y) if i==0 else (48-x,48-y)
            n=f"cycle-{i}"
            path(self,n,p(6,22),[("C",p(6,13),p(14,6),p(24,6)),("C",p(32,6),p(38,10),p(42,16))])
            self.add_polyline(n+"-head",p(32,16),p(42,16),p(42,6));self.relate("connect",n,n+"-head")


# Reviewed source-equivalent container sub-icon references.
SOURCE_REFERENCES = [('6f318fe0-f892-436c-85ec-2fd600044785', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/sync arrow_6f318fe0-f892-436c-85ec-2fd600044785.svg')]
