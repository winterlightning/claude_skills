"""Justified Paragraph Lines.
Plan: Five line series with shared left edge and 8-unit row step. Extremes (4,8)-(44,40).
Construction reference: local Lucide list, original and atomic-debug.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'e791bc76-58ba-4e6c-8ca6-103893b4666c'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/paragraph justified align_e791bc76-58ba-4e6c-8ca6-103893b4666c.svg'
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
    icon_id = 'justified-paragraph-lines'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/interface-essential"
    aliases = ()
    keywords = ('paragraph', 'justify', 'lines', 'text', 'alignment', 'format')
    def build(self):
        lengths=(40,40,40,40,28)
        for i,length in enumerate(lengths):
            y=8+8*i
            self.add_line("line-"+str(i),(4,y),(4+length,y))
