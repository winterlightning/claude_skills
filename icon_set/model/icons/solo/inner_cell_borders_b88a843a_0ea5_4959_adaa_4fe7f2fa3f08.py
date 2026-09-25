"""Inner Cell Borders.
Plan: Four mirrored broken corners surround structural central cross. Extremes (6,6)-(42,42).
Construction reference: local Lucide list, original and atomic-debug.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'b88a843a-0ea5-4959-adaa-4fe7f2fa3f08'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/cell border center_b88a843a-0ea5-4959-adaa-4fe7f2fa3f08.svg'
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
    icon_id = 'inner-cell-borders'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "interface-essential"
    aliases = ()
    keywords = ('cells', 'borders', 'grid', 'table', 'inside', 'format')
    def build(self):
        for sx in (-1,1):
            for sy in (-1,1):
                def p(x,y):return (24+sx*x,24+sy*y)
                path(self,f"corner-{sx}-{sy}",p(18,10),[("L",p(18,12)),("A",6,6,sx*sy>0,p(12,18)),("L",p(10,18))])
        self.add_polyline("horizontal",(6,24),(24,24),(42,24))
        self.add_polyline("vertical",(24,6),(24,24),(24,42))
        self.relate("connect","horizontal","vertical")
