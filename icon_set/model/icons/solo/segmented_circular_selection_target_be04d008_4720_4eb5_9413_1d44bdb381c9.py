"""Segmented Circular Selection Target.
Plan: Four equal circular outer segments rotated by quarter turns around a central circle. Outer radius20, inner radius7.
Lucide original and atomic-debug: scan.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'be04d008-4720-4eb5-9413-1d44bdb381c9'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/cursor select circle_be04d008-4720-4eb5-9413-1d44bdb381c9.svg'
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
    icon_id = 'segmented-circular-selection-target'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "interface-essential"
    aliases = ()
    keywords = ('target', 'selection', 'circle', 'segmented', 'reticle', 'interface')
    def build(self):
        cx=cy=24
        for i in range(4):
            def p(x,y):
                for _ in range(i):x,y=-y,x
                return (cx+x,cy+y)
            path(self,f"segment-{i}",p(-10,-17),[("C",p(-7,-19),p(-3,-20),p(0,-20)),("C",p(3,-20),p(7,-19),p(10,-17))])
        circle(self,"center",cx,cy,7)
