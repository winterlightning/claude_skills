"""Hand Holding Chopsticks.

Symbol plan: Hand enters right with curved thumb over two left-facing chopsticks; extrema (4,8)-(44,40).
Construction reference: Shared human reference: minimal anatomy; Lucide hand-grab: coherent curved grasp.
Reduction: Three tiny finger divisions reduced; right-entry asymmetry retained.
Keyshape centerline extremes follow the SOLO48 contract; stroke 4, integer grid.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '722887fe-790e-4808-bdbe-f0f818127ed3'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/chopstick_722887fe-790e-4808-bdbe-f0f818127ed3.svg'
AUTHOR = 'gpt-6'


class SidewaysHandHoldingChopsticks(Solo48):
    icon_id = 'sideways-hand-holding-chopsticks'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/food"
    aliases = ()
    keywords = ('sideways', 'hand', 'holding', 'chopsticks')

    def build(self):
        self.path('thumb',(28,8),[(24,8),((18,8),(18,16),(24,16)),(32,18),((38,20),(38,26),(44,26))])
        self.path('fingers',(24,26),[((20,30),(27,36),(37,36)),(44,40)])
        self.add_line('top-stick',(4,17),(24,16))
        self.add_line('bottom-stick',(4,28),(24,26))
        self.relate('connect','thumb','top-stick')
        self.relate('connect','fingers','bottom-stick')

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
