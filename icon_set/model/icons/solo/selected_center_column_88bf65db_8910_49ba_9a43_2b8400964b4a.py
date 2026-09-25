"""Selected Center Column.
Plan: Three equal center cells and paired dashed neighboring boundaries; same height and repeated spacing. Extremes(6,6)-(42,42).
Lucide original and atomic-debug: columns-3.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '88bf65db-8910-49ba-9a43-2b8400964b4a'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/column selected_88bf65db-8910-49ba-9a43-2b8400964b4a.svg'
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
    icon_id = 'selected-center-column'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "interface-essential"
    categories = ("interface-essential", "primitives")
    aliases = ()
    keywords = ('column', 'selected', 'grid', 'cells', 'table', 'spreadsheet')
    def build(self):
        self.add_polyline("column",(18,6),(30,6),(30,18),(30,30),(30,42),(18,42),(18,30),(18,18),closed=True)
        for i,y in enumerate([18,30]):self.add_line(f"division-{i}",(18,y),(30,y));self.relate("connect","column",f"division-{i}")
        for side,x in enumerate([6,42]):
            for j,y in enumerate([6,22,38]):self.add_line(f"dash-{side}-{j}",(x,y),(x,y+4))
