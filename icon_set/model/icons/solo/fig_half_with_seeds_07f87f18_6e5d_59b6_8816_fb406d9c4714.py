"""Half Sliced Fig Fruit.

Symbol plan: Mirrored pear outline with blunt neck and three seeds; extrema (8,4)-(40,44).
Construction reference: Supplied fig; Lucide bean: continuous fruit contour.
Reduction: Dropped nested flesh boundary to preserve seed spacing.
Keyshape centerline extremes follow the SOLO48 contract; stroke 4, integer grid.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '07f87f18-6e5d-59b6-8816-fb406d9c4714'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/fig_07f87f18-6e5d-59b6-8816-fb406d9c4714.svg'
AUTHOR = 'gpt-6'


class FigHalfWithSeeds(Solo48):
    icon_id = 'fig-half-with-seeds'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "food"
    aliases = ()
    keywords = ('fig', 'half', 'with', 'seeds')

    def build(self):
        axis = 24  # Paired x positions derive from the same symmetry axis.
        self.path('fig',(axis-4,4),[(axis+4,4),((axis+4,15),(axis+16,18),(axis+16,29)),((axis+16,39),(axis+9,44),(axis+0,44)),((axis-9,44),(axis-16,39),(axis-16,29)),((axis-16,18),(axis-4,15),(axis-4,4))],True)
        for i,p in enumerate(((axis+0,23),(axis-5,32),(axis+5,32))):self.add_dot(f'seed-{i}',p)

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
