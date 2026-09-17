"""House with Upright Chimney Stroke.
Plan: Symmetric house, upright chimney on right; extremes (6,6)-(42,42).
Construction reference: local Lucide house, original and atomic-debug.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'd0a49d2c-ca23-4f73-a310-7bd929b19be2'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/house_d0a49d2c-ca23-4f73-a310-7bd929b19be2.svg'
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
    icon_id = 'house-with-upright-chimney-stroke'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/interface-essential"
    aliases = ()
    keywords = ('house', 'home', 'chimney', 'roof', 'building', 'outline')
    def build(self):
        self.add_polyline("roof",(6,24),(10,20),(24,6),(36,18),(38,20),(42,24))
        path(self,"walls",(10,20),[("L",(10,40)),("A",2,2,False,(12,42)),("L",(36,42)),("A",2,2,False,(38,40)),("L",(38,20))])
        self.relate("connect","roof","walls")
        self.add_line("chimney",(36,6),(36,18))
        self.relate("connect","roof","chimney")
