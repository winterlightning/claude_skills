"""Halved Hubbard Squash.

Symbol plan: Asymmetric diagonal squash, round lower seed cavity and bent stem; extrema (6,6)-(42,42).
Construction reference: Supplied squash; Lucide bean: asymmetric swelling with one nested cavity.
Reduction: Seed specks omitted; asymmetric bent neck retained.
Keyshape centerline extremes follow the SOLO48 contract; stroke 4, integer grid.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '14949550-4ecc-4912-baee-f9ed5e37884b'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/hubbard squash slice_14949550-4ecc-4912-baee-f9ed5e37884b.svg'
AUTHOR = 'gpt-6'


class HubbardSquashHalf(Solo48):
    icon_id = 'hubbard-squash-half'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "food"
    categories = ("primitives", "food")
    aliases = ()
    keywords = ('hubbard', 'squash', 'half')

    def build(self):
        self.path('squash',(35,10),[((42,10),(42,16),(39,22)),((35,28),(37,34),(31,39)),((28,41),(25,42),(21,42)),((12,42),(6,36),(6,28)),((6,20),(10,15),(17,14)),((24,13),(26,15),(31,11)),((32,10),(34,10),(35,10))],True)
        self.loop('cavity',21,28,5)
        self.path('stem',(35,10),[((40,10),(42,9),(42,6))])
        self.relate('connect','stem','squash')

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
