"""Grilled Kebab Skewer.

Symbol plan: Three rounded diamond chunks on shared rising diagonal, exposed skewer ends; extrema (6,6)-(42,42).
Construction reference: Supplied skewer; Lucide candy: rounded diagonal chunks.
Reduction: Irregular edges regularized; intentional diagonal retained.
Keyshape centerline extremes follow the SOLO48 contract; stroke 4, integer grid.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '42a901b5-3866-59fe-8410-99813ff37c88'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/barbecue stick_42a901b5-3866-59fe-8410-99813ff37c88.svg'
AUTHOR = 'gpt-6'


class ThreePieceKebabSkewer(Solo48):
    icon_id = 'three-piece-kebab-skewer'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "food"
    categories = ("primitives", "food")
    aliases = ()
    keywords = ('three', 'piece', 'kebab', 'skewer')

    def build(self):
        for i,(x,y) in enumerate(((12,36),(24,24),(36,12))):
            self.path(f'food-{i}',(x+3,y-3),[(x+5,y-1),((x+6,y),(x+6,y),(x+5,y+1)),(x+1,y+5),((x,y+6),(x,y+6),(x-1,y+5)),(x-3,y+3),(x-5,y+1),((x-6,y),(x-6,y),(x-5,y-1)),(x-1,y-5),((x,y-6),(x,y-6),(x+1,y-5)),(x+3,y-3)],True)
        self.add_line('tip',(39,9),(42,6))
        self.add_line('handle',(6,42),(9,39))
        self.add_line('shaft-a',(15,33),(21,27))
        self.add_line('shaft-b',(27,21),(33,15))
        for shaft,parts in [('tip',['food-2']),('handle',['food-0']),('shaft-a',['food-0','food-1']),('shaft-b',['food-1','food-2'])]:
            for part in parts:self.relate('connect',shaft,part)

    def loop(self, name, x, y, rx, ry=None):
        ry = rx if ry is None else ry
        self.add_arc(name+'-top', (x-rx,y), (x+rx,y), radius_x=rx, radius_y=ry)
        self.add_arc(name+'-bottom', (x+rx,y), (x-rx,y), radius_x=rx, radius_y=ry)
        self.add_contour(name, name+'-top', name+'-bottom', closed=True)

    def path(self, name, start, commands, closed=False):
        ids=[]
        point=start
        for i,command in enumerate(commands):
            key=f'{name}-{i}'
            if len(command)==2:
                self.add_line(key, point, command)
                point=command
            else:
                c1,c2,end=command
                self.add_bezier(key, point, (c1,c2,end))
                point=end
            ids.append(key)
        self.add_contour(name, *ids, closed=closed)
