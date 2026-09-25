"""Rounded Gear.
Plan: Six broad lobes and curved recesses from a half-turn repeat, centered round hub. Extremes(6,6)-(42,42).
Lucide original and atomic-debug: settings.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '1ccd28b1-c02a-5c2e-bb72-1fbc386d96b2'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/cog_1ccd28b1-c02a-5c2e-bb72-1fbc386d96b2.svg'
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
    icon_id = 'rounded-gear'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "interface-essential"
    aliases = ()
    keywords = ('gear', 'cog', 'settings', 'wheel', 'mechanical', 'hub')
    def build(self):
        # A half-turn repeat owns all six rounded teeth and recesses.
        commands=[]
        segments=[((28,6),(28,8),(29,12)),((31,15),(34,13),(38,12)),((40,11),(42,14),(42,16)),((42,19),(38,20),(38,24)),((38,28),(42,29),(42,32)),((42,34),(40,37),(38,36)),((34,35),(31,33),(29,36)),((28,40),(28,42),(24,42))]
        for i in range(2):
            def p(q):return q if i==0 else (48-q[0],48-q[1])
            for a,b,c in segments:commands.append(("C",p(a),p(b),p(c)))
        path(self,"gear",(24,6),commands,True)
        circle(self,"hub",24,24,4)
