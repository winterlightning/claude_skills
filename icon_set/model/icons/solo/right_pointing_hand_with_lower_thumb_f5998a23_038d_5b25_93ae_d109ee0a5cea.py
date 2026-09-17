"""Right Pointing Hand with Lower Thumb.
Plan: Shared finger widths and curled-finger series, pointing right with lower thumb. Extremes (8,4)-(40,44).
Lucide original and atomic-debug: pointer.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'f5998a23-038d-5b25-93ae-d109ee0a5cea'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/hand pointer right_f5998a23-038d-5b25-93ae-d109ee0a5cea.svg'
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
    icon_id = 'right-pointing-hand-with-lower-thumb'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/interface-essential"
    aliases = ()
    keywords = ('hand', 'right', 'point', 'finger', 'thumb', 'gesture')
    def build(self):
        # Human construction guide inspected; isolated hand has no head/body gap.
        def p(x,y):return (48-y,48-x)
        commands=[("L",p(12,12)),("A",4,4,False,p(20,12)),("L",p(20,22))]
        for j in range(3):
            x=20+8*j;y=22+2*j
            if j:commands.append(("L",p(x,y)))
            commands.append(("A",4,4,False,p(x+8,y)))
        commands += [("L",p(44,28)),("C",p(44,36),p(38,40),p(30,40)),("L",p(24,40)),("C",p(14,40),p(4,38),p(4,32)),("C",p(4,30),p(4,26),p(4,24)),("C",p(4,20),p(8,20),p(12,28))]
        path(self,"hand",p(12,28),commands,True)
        for j in range(3):
            x=20+8*j;y=22+2*j;n=f"crease-{j}"
            self.add_line(n,p(x,y),p(x,y+3));self.relate("connect","hand",n)
