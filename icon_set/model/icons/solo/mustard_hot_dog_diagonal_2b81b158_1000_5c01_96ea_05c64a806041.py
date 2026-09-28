"""Hot Dog with Mustard.
Symbol plan: Diagonal rounded hot dog with a continuous mustard wave; bounds (6,6)-(42,42).
Construction reference: Supplied diagonal hot dog; Lucide sandwich: coherent outer food silhouette.
Reduction: Secondary bun/sausage seam outlines omitted; diagonal and mustard preserved.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2b81b158-1000-5c01-96ea-05c64a806041'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/hot dog grilled_2b81b158-1000-5c01-96ea-05c64a806041.svg'
AUTHOR = 'gpt-6'

class MustardHotDogDiagonal(Solo48):
    icon_id = 'mustard-hot-dog-diagonal'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    categories = ('primitives', 'food')
    aliases = ()
    keywords = ('mustard', 'hot', 'dog', 'diagonal')

    def build(self):
        self.path('bun',(6,32),[((6,28),(8,26),(12,22)),(22,12),((26,8),(28,6),(32,6)),((38,6),(42,10),(42,16)),((42,20),(40,22),(36,26)),(26,36),((22,40),(20,42),(16,42)),((10,42),(6,38),(6,32))],True)

        self.add_bezier('mustard',(16,30),((21,31),(19,23),(24,24)),((29,25),(27,17),(32,18)))

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
