"""Right Arrow through Divider Gap.
Plan: Right arrow through a split divider with a separate left boundary. Extremes (6,6)-(42,42).
Lucide original and atomic-debug: arrow-right.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '12fb8eb8-6d1b-570b-8a0f-7bdcb6895475'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/overflow_12fb8eb8-6d1b-570b-8a0f-7bdcb6895475.svg'
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
    icon_id = 'right-arrow-through-divider-gap'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "interface-essential"
    aliases = ()
    keywords = ('arrow', 'right', 'overflow', 'divider', 'gap', 'direction')
    def build(self):
        self.add_line("boundary",(6,6),(6,42))
        for i,(a,b) in enumerate([(6,14),(34,42)]):self.add_line(f"divider-{i}",(24,a),(24,b))
        self.add_line("shaft",(14,24),(42,24));self.add_polyline("head",(34,16),(42,24),(34,32));self.relate("connect","shaft","head")
