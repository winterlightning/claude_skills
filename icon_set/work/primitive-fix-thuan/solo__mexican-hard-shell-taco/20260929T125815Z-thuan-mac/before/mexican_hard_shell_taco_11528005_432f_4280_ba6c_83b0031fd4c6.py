"""Mexican Food Hard Shell Taco.
Symbol plan: Diagonal folded shell with three broad scallops of filling. Bounds (6,6)-(42,42).
Construction reference: Supplied taco; Lucide citrus broad curved food wedge.
Reduction: Many small filling scallops reduced to three broad lobes; diagonal fold retained.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '11528005-432f-4280-ba6c-83b0031fd4c6'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/tacos_11528005-432f-4280-ba6c-83b0031fd4c6.svg'
AUTHOR = 'gpt-6'

class MexicanHardShellTaco(Solo48):
    icon_id = 'mexican-hard-shell-taco'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    categories = ('primitives', 'food')
    aliases = ()
    keywords = ('mexican', 'hard', 'shell', 'taco')

    def build(self):
        self.path('shell',(16,42),[(42,16),((37,11),(28,14),(22,20)),((16,26),(11,36),(16,42))],True)
        self.path('filling',(16,42),[((10,42),(6,38),(6,34)),(6,27),((6,20),(7,15),(14,15)),((14,8),(19,6),(24,6)),((29,6),(31,7),(34,10)),((37,10),(40,12),(42,16))]);self.relate('connect','filling','shell')

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
