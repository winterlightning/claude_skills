"""Peeled Mangosteen Fruit.
Symbol plan: Domed flesh over half-shell, with central fruit seam. Bounds (6,6)-(42,42).
Construction reference: Supplied mangosteen; Lucide soup half-bowl arcs.
Reduction: Three narrow flesh segments reduced to two, and doubled rim omitted.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b3274f58-7457-4539-98bc-84a72cc5ccf3'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/mangosteen peeled_b3274f58-7457-4539-98bc-84a72cc5ccf3.svg'
AUTHOR = 'gpt-6'

class PeeledMangosteenFruit(Solo48):
    icon_id = 'peeled-mangosteen-fruit'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    aliases = ()
    keywords = ('peeled', 'mangosteen', 'fruit')

    def build(self):
        axis=24
        self.add_polyline('rim',(6,24),(12,24),(axis,24),(36,24),(42,24))
        self.add_arc('shell',(42,24),(6,24),radius_x=18);self.relate('connect','shell','rim')
        self.path('flesh',(12,24),[((12,14),(16,6),(axis,6)),((32,6),(36,14),(36,24))]);self.relate('connect','flesh','rim')
        self.add_line('seam',(axis,6),(axis,24));self.relate('connect','seam','flesh');self.relate('connect','seam','rim')

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
