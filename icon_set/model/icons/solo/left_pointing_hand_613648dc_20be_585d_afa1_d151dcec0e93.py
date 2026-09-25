"""Left Pointing Hand.
Plan: One silhouette owns capsule index, three curled-finger scallops, palm and thumb. Extremes (6,6)-(42,42). Human reference full_body_ref.png informed minimal anatomical vocabulary; no head/body gap applies.
Construction reference: local Lucide hand, original and atomic-debug.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '613648dc-20be-585d-afa1-d151dcec0e93'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/hand pointer left_613648dc-20be-585d-afa1-d151dcec0e93.svg'
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
    icon_id = 'left-pointing-hand'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "interface-essential"
    aliases = ()
    keywords = ('hand', 'left', 'point', 'finger', 'cursor', 'gesture')
    def build(self):
        path(self,"hand",(26,10),[("L",(10,10)),("A",4,4,False,(10,18)),("L",(22,18)),("A",4,4,False,(22,26)),("L",(24,26)),("A",4,4,False,(24,34)),("L",(26,34)),("A",4,4,False,(26,42)),("L",(32,42)),("C",(38,42),(42,36),(42,28)),("L",(42,24)),("C",(42,16),(35,6),(30,6)),("C",(27,6),(26,7),(26,10))],True)
