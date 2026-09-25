"""Korean Rice Cake Skewer with Sauce.
Symbol plan: Three contiguous diagonal rice cakes with shared seams, protruding skewer, low-left dipping bowl. Bounds (6,6)-(42,42).
Construction reference: Supplied rice-cake skewer and natural dipping dish; Lucide soup bowl.
Reduction: Tiny rim ellipse omitted; three food bars retained.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c5b185fc-2fac-4f46-9e95-acf2bd4b9e3d'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/korean tokboki_c5b185fc-2fac-4f46-9e95-acf2bd4b9e3d.svg'
AUTHOR = 'gpt-6'

class KoreanRiceCakeSkewerSauce(Solo48):
    icon_id = 'korean-rice-cake-skewer-sauce'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    categories = ('primitives', 'food')
    aliases = ()
    keywords = ('korean', 'rice', 'cake', 'skewer', 'sauce')

    def build(self):
        self.add_polyline('cakes',(16,14),(20,10),(24,6),(30,12),(36,18),(42,24),(38,28),(34,32),(28,26),(22,20),closed=True)
        for j,(a,b) in enumerate([((22,20),(30,12)),((28,26),(36,18))]):
         self.add_line('seam-'+str(j),a,b);self.relate('connect','seam-'+str(j),'cakes')
        self.add_line('tail',(38,28),(42,32));self.relate('connect','tail','cakes')
        self.add_line('tip',(16,6),(20,10));self.relate('connect','tip','cakes')
        self.path('sauce',(6,32),[(19,32),((19,38),(16,42),(12,42)),((8,42),(6,38),(6,32))],True)

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
