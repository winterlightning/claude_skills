"""Hot Steaming Soup Dumpling.
Symbol plan: Plump dumpling with three gathered lobes, two connected folds, three steam wisps. Bounds (6,6)-(42,42).
Construction reference: Supplied dumpling; Lucide soup for steam.
Reduction: Three fine crease marks reduced to two folds.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4bca0b06-22ca-493e-aaea-4f5e30cb09d6'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/xaio long bao soup duimpling_4bca0b06-22ca-493e-aaea-4f5e30cb09d6.svg'
AUTHOR = 'gpt-6'

class HotSteamingSoupDumpling(Solo48):
    icon_id = 'hot-steaming-soup-dumpling'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    aliases = ()
    keywords = ('hot', 'steaming', 'soup', 'dumpling')

    def build(self):
        axis = 24  # Mirror pairs derive from a shared vertical axis.
        self.path('dumpling',(axis-18,34),[((axis-18,30),(axis-12,28),(axis-10,26)),((axis-14,20),(axis-4,20),(axis-4,26)),((axis-4,20),(axis+4,20),(axis+4,26)),((axis+4,20),(axis+14,20),(axis+10,26)),((axis+12,28),(axis+18,30),(axis+18,34)),((axis+18,42),(axis+12,42),(axis+0,42)),((axis-12,42),(axis-18,42),(axis-18,34))],True)
        self.add_line('fold-l',(axis-4,26),(axis-6,33));self.add_line('fold-r',(axis+4,26),(axis+6,33))
        self.relate('connect','fold-l','dumpling');self.relate('connect','fold-r','dumpling')
        for i,x in enumerate((axis-12,24,36)):self.steam(x,6,13,f'steam-{i}')

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
