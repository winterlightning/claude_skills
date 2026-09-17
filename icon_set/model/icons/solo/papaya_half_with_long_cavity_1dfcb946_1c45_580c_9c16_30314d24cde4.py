"""Halved Tropical Papaya Fruit.

Symbol plan: Symmetric papaya and long pointed cavity; extrema (8,4)-(40,44).
Construction reference: Supplied papaya; Lucide bean: coherent nested contours.
Reduction: No seed speckles added.
Keyshape centerline extremes follow the SOLO48 contract; stroke 4, integer grid.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1dfcb946-1c45-580c-9c16-30314d24cde4'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/papaya_1dfcb946-1c45-580c-9c16-30314d24cde4.svg'
AUTHOR = 'gpt-6'


class PapayaHalfWithLongCavity(Solo48):
    icon_id = 'papaya-half-with-long-cavity'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/food"
    aliases = ()
    keywords = ('papaya', 'half', 'with', 'long', 'cavity')

    def build(self):
        axis = 24  # Paired x positions derive from the same symmetry axis.
        self.path('papaya',(axis+0,4),[((axis+9,4),(axis+7,12),(axis+12,20)),((axis+15,25),(axis+16,27),(axis+16,30)),((axis+16,38),(axis+9,41),(axis+0,44)),((axis-9,41),(axis-16,38),(axis-16,30)),((axis-16,27),(axis-15,25),(axis-12,20)),((axis-7,12),(axis-9,4),(axis+0,4))],True)
        self.path('cavity',(axis+0,15),[((axis+5,22),(axis+5,30),(axis+0,35)),((axis-5,30),(axis-5,22),(axis+0,15))],True)

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
