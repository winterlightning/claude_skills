"""Left Pointing Hand with Raised Thumb.
Plan: One silhouette owns capsule index, three curled-finger scallops, palm and thumb. Extremes (8,4)-(40,44). Human reference full_body_ref.png informed minimal anatomical vocabulary; no head/body gap applies.
Construction reference: local Lucide hand, original and atomic-debug.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'ea54b202-0f96-50db-97dc-1884a36b2fb9'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/hand pointer left_ea54b202-0f96-50db-97dc-1884a36b2fb9.svg'
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
    icon_id = 'left-pointing-hand-with-raised-thumb'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/interface-essential"
    aliases = ()
    keywords = ('hand', 'left', 'point', 'finger', 'thumb', 'gesture')
    def build(self):
        path(self,"hand",(26,12),[("L",(12,12)),("A",4,4,False,(12,20)),("L",(24,20)),("A",4,4,False,(24,28)),("L",(26,28)),("A",4,4,False,(26,36)),("L",(28,36)),("A",4,4,False,(28,44)),("L",(32,44)),("C",(38,44),(40,38),(40,30)),("L",(40,24)),("C",(40,16),(37,11),(34,8)),("C",(32,6),(30,4),(27,4)),("A",5,5,False,(22,9)),("C",(22,10),(24,11),(26,12))],True)
