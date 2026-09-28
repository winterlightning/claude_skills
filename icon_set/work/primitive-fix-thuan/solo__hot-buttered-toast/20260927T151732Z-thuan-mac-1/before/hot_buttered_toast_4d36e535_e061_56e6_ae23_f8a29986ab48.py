"""Hot Buttered Toast.
Symbol plan: Mirror-symmetric bread with domed crown, shoulders, square butter, paired steam. Bounds (8,4)-(40,44).
Construction reference: Supplied toast; Lucide sandwich for distinct simple bread and filling contours.
Reduction: No crumbs or duplicate crust border.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4d36e535-e061-56e6-ae23-f8a29986ab48'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/breakfast bread toast_4d36e535-e061-56e6-ae23-f8a29986ab48.svg'
AUTHOR = 'gpt-6'

class HotButteredToast(Solo48):
    icon_id = 'hot-buttered-toast'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    categories = ('primitives', 'food')
    aliases = ()
    keywords = ('hot', 'buttered', 'toast')

    def build(self):
        axis = 24  # Mirror pairs derive from a shared vertical axis.
        self.path('toast',(axis+0,18),[((axis-10,18),(axis-16,20),(axis-16,24)),((axis-16,26),(axis-14,27),(axis-14,28)),(axis-14,40),((axis-14,44),(axis-14,44),(axis-10,44)),(axis+10,44),((axis+14,44),(axis+14,44),(axis+14,40)),(axis+14,28),((axis+14,27),(axis+16,26),(axis+16,24)),((axis+16,20),(axis+10,18),(axis+0,18))],True)
        self.add_polyline('butter',(axis-4,27),(axis+4,27),(axis+4,35),(axis-4,35),closed=True)
        for i,x in enumerate((axis-7,31)):self.steam(x,4,10,f'steam-{i}')

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
