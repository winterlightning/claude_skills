"""Increasing Length Bars.
Plan: Three capsules share radius 4 and 16-unit row step; widths 16,24,32. Extremes (8,4)-(40,44).
Construction reference: local Lucide list, original and atomic-debug.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'e35f33b6-4cda-5034-be8a-41f333f665a1'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/descending sort_e35f33b6-4cda-5034-be8a-41f333f665a1.svg'
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
    icon_id = 'increasing-length-bars'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "interface-essential"
    categories = ("interface-essential", "primitives")
    aliases = ()
    keywords = ('bars', 'sort', 'ascending', 'order', 'length', 'horizontal')
    def build(self):
        for i,width in enumerate((16,24,32)):
            top=4+16*i;left=8;right=left+width;r=4
            path(self,"bar-"+str(i),(left+r,top),[("L",(right-r,top)),("A",r,r,True,(right-r,top+8)),("L",(left+r,top+8)),("A",r,r,True,(left+r,top))],True)
