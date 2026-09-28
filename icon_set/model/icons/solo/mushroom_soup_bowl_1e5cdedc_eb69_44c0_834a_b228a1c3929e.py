"""Mushroom Soup Bowl.
Symbol plan: Broad soup bowl over two mushroom ingredients; cap series shares dimensions. Bounds (6,6)-(42,42).
Construction reference: Supplied soup with two mushrooms; Lucide soup broad bowl.
Reduction: Oval rim and liquid seam omitted; two mushrooms remain below the bowl.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1e5cdedc-eb69-44c0-834a-b228a1c3929e'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/mushroom soup_1e5cdedc-eb69-44c0-834a-b228a1c3929e.svg'
AUTHOR = 'gpt-6'

class MushroomSoupBowl(Solo48):
    icon_id = 'mushroom-soup-bowl'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    categories = ('primitives', 'food')
    aliases = ()
    keywords = ('mushroom', 'soup', 'bowl')

    def build(self):
        self.add_line('rim',(6,6),(42,6))
        self.add_arc('bowl',(42,6),(6,6),radius_x=18,radius_y=16);self.relate('connect','bowl','rim')
        for j,x in enumerate((13,35)):
         self.add_arc('cap-'+str(j),(x-7,38),(x+7,38),radius_x=7)
         self.add_polyline('gill-'+str(j),(x-7,38),(x,38),(x+7,38));self.relate('connect','cap-'+str(j),'gill-'+str(j))
         self.add_line('stem-'+str(j),(x,38),(x,42));self.relate('connect','stem-'+str(j),'gill-'+str(j))

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
