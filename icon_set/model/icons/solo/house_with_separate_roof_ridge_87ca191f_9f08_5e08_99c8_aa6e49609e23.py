"""House with Separate Roof Ridge.
Plan: Two parallel roof chevrons, mirrored facade and open rounded doorway; extremes (6,6)-(42,42).
Construction reference: local Lucide house, original and atomic-debug.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '87ca191f-9f08-5e08-99c8-aa6e49609e23'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/house_87ca191f-9f08-5e08-99c8-aa6e49609e23.svg'
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
    icon_id = 'house-with-separate-roof-ridge'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "interface-essential"
    aliases = ()
    keywords = ('house', 'home', 'roof', 'door', 'building', 'entrance')
    def build(self):
        self.add_polyline("ridge",(6,18),(24,6),(42,18))
        path(self,"house",(8,30),[("L",(24,18)),("L",(40,30)),("L",(40,42)),("L",(28,42)),("L",(28,36)),("A",2,2,False,(26,34)),("L",(22,34)),("A",2,2,False,(20,36)),("L",(20,42)),("L",(8,42)),("L",(8,30))],True)
