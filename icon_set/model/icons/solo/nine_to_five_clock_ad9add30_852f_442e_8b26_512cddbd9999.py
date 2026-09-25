"""Nine to Five Clock.
Plan: Eight attached ticks on a symmetric circular face; left and down-right hands. Cardinal radius 20 about (24,24).
Construction reference: local Lucide clock, original and atomic-debug.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'ad9add30-852f-442e-8b26-512cddbd9999'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/time clock nine to five_ad9add30-852f-442e-8b26-512cddbd9999.svg'
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
    icon_id = 'nine-to-five-clock'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "interface-essential"
    categories = ("interface-essential", "primitives")
    aliases = ()
    keywords = ('clock', 'time', 'nine', 'five', 'hours', 'face')
    def build(self):
        # One quadrant owns the curve and tick geometry; rotate it four times.
        cx,cy=24,24
        def rotate(point,quarter):
            x,y=point
            for _ in range(quarter):x,y=-y,x
            return (cx+x,cy+y)
        commands=[]
        for quarter in range(4):
            for c1,c2,end in [((5,-20),(10,-18),(14,-14)),((18,-10),(20,-5),(20,0))]:
                commands.append(("C",rotate(c1,quarter),rotate(c2,quarter),rotate(end,quarter)))
        path(self,"rim",(cx,cy-20),commands,True)
        for quarter in range(4):
            for i,(start,end) in enumerate([((0,-20),(0,-17)),((14,-14),(12,-12))]):
                name="tick-"+str(quarter*2+i)
                self.add_line(name,rotate(start,quarter),rotate(end,quarter))
                self.relate("connect","rim",name)
        self.add_polyline("hands",(cx-8,cy),(cx,cy),(cx+5,cy+8))
