"""Nine Button Grid.
Plan: Nine repeated round buttons with 15-unit row/column steps; reduced corner detail for clear empty interiors. Extremes (6,6)-(42,42).
Construction reference: local Lucide grid-3x3, original and atomic-debug.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '2135b350-e1aa-5e8d-abcb-c4bcf0f5be5f'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/dial pad_2135b350-e1aa-5e8d-abcb-c4bcf0f5be5f.svg'
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
    icon_id = 'nine-button-grid'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "interface-essential"
    aliases = ()
    keywords = ('grid', 'keypad', 'nine', 'buttons', 'menu', 'dial')
    def build(self):
        for row in range(3):
            for col in range(3):circle(self,f"button-{row}-{col}",9+15*col,9+15*row,3)
