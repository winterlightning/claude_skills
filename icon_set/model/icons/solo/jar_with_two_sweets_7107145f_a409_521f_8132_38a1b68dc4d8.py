"""Glass Jar with Round Sweets.

Symbol plan: Jar owns broad lid and two round sweets on a diagonal; extrema (8,4)-(40,44).
Construction reference: Supplied jar silhouette; Lucide candy: clear circular food geometry.
Reduction: Two circular sweets retained; no reflections.
Keyshape centerline extremes follow the SOLO48 contract; stroke 4, integer grid.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7107145f-a409-521f-8132-38a1b68dc4d8'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/candy jar_7107145f-a409-521f-8132-38a1b68dc4d8.svg'
AUTHOR = 'gpt-6'


class JarWithTwoSweets(Solo48):
    icon_id = 'jar-with-two-sweets'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "food"
    categories = ("primitives", "food")
    aliases = ()
    keywords = ('jar', 'with', 'two', 'sweets')

    def build(self):
        axis = 24  # Paired x positions derive from the same symmetry axis.
        self.path('jar',(axis-10,4),[(axis+10,4),((axis+14,4),(axis+14,12),(axis+10,12)),(axis+8,12),((axis+8,18),(axis+16,18),(axis+16,24)),(axis+16,40),((axis+16,44),(axis+16,44),(axis+12,44)),(axis-12,44),((axis-16,44),(axis-16,44),(axis-16,40)),(axis-16,24),((axis-16,18),(axis-8,18),(axis-8,12)),(axis-10,12),((axis-14,12),(axis-14,4),(axis-10,4))],True)
        self.add_line('lid-seam',(axis-8,12),(axis+8,12))
        self.relate('connect','jar','lid-seam')
        self.loop('sweet-a',19,26,2)
        self.loop('sweet-b',30,33,2)

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
