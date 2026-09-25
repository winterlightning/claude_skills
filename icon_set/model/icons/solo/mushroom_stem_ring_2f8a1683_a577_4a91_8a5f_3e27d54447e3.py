"""Mushroom with Ring on Stem.
Symbol plan: Semicircular cap, rounded stalk and cross-stem collar; axis24. Bounds (6,6)-(42,42).
Construction reference: Supplied mushroom; no useful direct Lucide mushroom match.
Reduction: Stem collar simplified to a single cross stroke.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2f8a1683-a577-4a91-8a5f-3e27d54447e3'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/mushroom poisonous_2f8a1683-a577-4a91-8a5f-3e27d54447e3.svg'
AUTHOR = 'gpt-6'

class MushroomStemRing(Solo48):
    icon_id = 'mushroom-stem-ring'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    aliases = ()
    keywords = ('mushroom', 'stem', 'ring')

    def build(self):
        axis=24
        self.add_arc('cap',(6,24),(42,24),radius_x=18)
        self.add_polyline('gills',(6,24),(18,24),(30,24),(42,24));self.relate('connect','gills','cap')
        self.path('stem',(18,24),[(18,33),(18,36),((18,40),(20,42),(axis,42)),((28,42),(30,40),(30,36)),(30,33),(30,24)]);self.relate('connect','stem','gills')
        self.add_polyline('collar',(12,33),(18,33),(30,33),(36,33));self.relate('connect','collar','stem')

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
