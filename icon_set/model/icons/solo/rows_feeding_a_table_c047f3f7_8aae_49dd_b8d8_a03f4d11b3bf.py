"""Rows Feeding a Table.
Plan: Three-column table above two curved feeding routes sharing a left edge; reduce two table rows to one for clearance. Extremes(6,6)-(42,42).
Lucide original and atomic-debug: table.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'c047f3f7-8aae-49dd-b8d8-a03f4d11b3bf'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/split subset spreadsheet_c047f3f7-8aae-49dd-b8d8-a03f4d11b3bf.svg'
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
    icon_id = 'rows-feeding-a-table'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/interface-essential"
    aliases = ()
    keywords = ('table', 'rows', 'subset', 'extract', 'arrows', 'diagram')
    def build(self):
        # Table cells are one repeated width; every intersection is a shared node.
        self.add_polyline("table",(6,6),(18,6),(30,6),(42,6),(42,14),(30,14),(18,14),(6,14),closed=True)
        for i,x in enumerate([18,30]):
            self.add_line(f"column-{i}",(x,6),(x,14));self.relate("connect","table",f"column-{i}")
        self.add_polyline("edge",(6,22),(6,34),(6,42))
        path(self,"route-0",(6,34),[("L",(18,34)),("A",4,4,False,(22,30)),("L",(22,22))])
        path(self,"route-1",(6,42),[("L",(32,42)),("A",6,6,False,(38,36)),("L",(38,22))])
        for i,x in enumerate([22,38]):
            self.add_polyline(f"head-{i}",(x-4,26),(x,22),(x+4,26));self.relate("connect",f"route-{i}",f"head-{i}");self.relate("connect","edge",f"route-{i}")
