"""Lidded Trash Bin.
Plan: Tapered body, projecting lid, raised handle and one groove. Extremes (8,4)-(40,44).
Construction reference: local Lucide trash, original and atomic-debug.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '1d1010fc-b5fd-5797-8e32-32efcf38328d'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/bin_1d1010fc-b5fd-5797-8e32-32efcf38328d.svg'
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
    icon_id = 'lidded-trash-bin'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/interface-essential"
    aliases = ()
    keywords = ('bin', 'trash', 'lid', 'handle', 'waste', 'rubbish')
    def build(self):
        self.add_polyline("lid",(8,12),(12,12),(18,12),(30,12),(36,12),(40,12))
        path(self,"body",(12,12),[("L",(14,40)),("C",(14,42),(16,44),(18,44)),("L",(30,44)),("C",(32,44),(34,42),(34,40)),("L",(36,12))])
        self.relate("connect","body","lid")
        path(self,"handle",(18,12),[("L",(18,8)),("A",4,4,True,(22,4)),("L",(26,4)),("A",4,4,True,(30,8)),("L",(30,12))])
        self.relate("connect","handle","lid")
        self.add_line("groove",(24,22),(24,34))
