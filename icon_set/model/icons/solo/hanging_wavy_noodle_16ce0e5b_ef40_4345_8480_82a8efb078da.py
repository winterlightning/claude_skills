"""Hanging Wavy Noodles.

Symbol plan: Pair of horizontal chopsticks and three shared smooth wave strands; extrema (6,6)-(42,42).
Construction reference: Supplied noodle reference; no useful Lucide match; tangent cubic waves.
Reduction: Four strands reduced to three to preserve clear spacing.
Keyshape centerline extremes follow the SOLO48 contract; stroke 4, integer grid.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '16ce0e5b-ef40-4345-8480-82a8efb078da'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/noodles_16ce0e5b-ef40-4345-8480-82a8efb078da.svg'
AUTHOR = 'gpt-6'


class HangingWavyNoodle(Solo48):
    icon_id = 'hanging-wavy-noodle'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/food"
    aliases = ()
    keywords = ('hanging', 'wavy', 'noodle')

    def build(self):
        self.add_line('upper-stick',(6,6),(42,6))
        self.add_polyline('lower-stick',(6,14),(12,14),(24,14),(36,14),(42,14))
        for i,x in enumerate((12,24,36)):
            end=42 if i!=1 else 40
            self.path(f'noodle-{i}',(x,14),[((x-5,21),(x+5,23),(x,28)),((x-5,34),(x+5,36),(x,end))])
            self.relate('connect',f'noodle-{i}','lower-stick')

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
