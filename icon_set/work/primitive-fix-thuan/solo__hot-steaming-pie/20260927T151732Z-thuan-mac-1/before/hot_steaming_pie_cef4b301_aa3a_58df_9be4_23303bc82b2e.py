"""Hot Steaming Pie.
Symbol plan: Domed pie crust with broad scallops, tapered dish, three steam curls. Bounds (6,6)-(42,42).
Construction reference: Supplied pie; Lucide soup for steam series.
Reduction: Vent cuts omitted to protect dome clearance; scalloped crust retained.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'cef4b301-aa3a-58df-9be4-23303bc82b2e'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/pie_cef4b301-aa3a-58df-9be4-23303bc82b2e.svg'
AUTHOR = 'gpt-6'

class HotSteamingPie(Solo48):
    icon_id = 'hot-steaming-pie'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    categories = ('primitives', 'food')
    aliases = ()
    keywords = ('hot', 'steaming', 'pie')

    def build(self):
        axis = 24  # Mirror pairs derive from a shared vertical axis.
        self.path('crust',(axis-18,30),[((axis-18,23),(axis-10,20),(axis+0,20)),((axis+10,20),(axis+18,23),(axis+18,30)),((axis+18,34),(axis+15,34),(axis+12,32)),((axis+8,30),(axis+4,34),(axis+0,32)),((axis-4,30),(axis-8,34),(axis-12,32)),((axis-16,34),(axis-18,34),(axis-18,30))],True)
        self.add_polyline('dish',(axis-12,32),(axis-8,42),(axis+8,42),(axis+12,32))
        self.relate('connect','crust','dish')
        for i,x in enumerate((axis-12,24,36)):self.steam(x,6,11,f'steam-{i}')

    def path(self, name, start, commands, closed=False):
        members=[]
        for j,c in enumerate(commands):
            tag=f'{name}-{j}'
            if len(c)==2:self.add_line(tag,start,c);start=c
            else:self.add_bezier(tag,start,c);start=c[2]
            members.append(tag)
        self.add_contour(name,*members,closed=closed)

    def loop(self,name,x,y,rx,ry=None):
        ry=rx if ry is None else ry
        self.add_arc(name+'-r',(x,y-ry),(x,y+ry),radius_x=rx,radius_y=ry)
        self.add_arc(name+'-l',(x,y+ry),(x,y-ry),radius_x=rx,radius_y=ry)
        self.add_contour(name,name+'-r',name+'-l',closed=True)

    def steam(self,x,top,bottom,name):
        mid=(top+bottom)//2
        self.add_bezier(name,(x+1,top),((x-2,top+2),(x-2,mid),(x,mid)),((x+2,mid),(x+2,bottom-2),(x-1,bottom)))
