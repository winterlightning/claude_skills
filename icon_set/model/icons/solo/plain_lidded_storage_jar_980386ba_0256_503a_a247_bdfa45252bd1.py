"""Glass Storage Jar.

Symbol plan: Symmetric straight-sided jar with shoulder curves and broad lid; extrema (8,4)-(40,44).
Construction reference: Supplied jar; no useful exact Lucide match.
Reduction: No interior marks.
Keyshape centerline extremes follow the SOLO48 contract; stroke 4, integer grid.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '980386ba-0256-503a-a247-bdfa45252bd1'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/candy jar_980386ba-0256-503a-a247-bdfa45252bd1.svg'
AUTHOR = 'gpt-6'


class PlainLiddedStorageJar(Solo48):
    icon_id = 'plain-lidded-storage-jar'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "food"
    categories = ("primitives", "food")
    aliases = ()
    keywords = ('plain', 'lidded', 'storage', 'jar')

    def build(self):
        axis = 24  # Paired x positions derive from the same symmetry axis.
        self.path('jar',(axis-10,4),[(axis+10,4),((axis+14,4),(axis+14,12),(axis+10,12)),(axis+8,12),((axis+8,18),(axis+16,18),(axis+16,24)),(axis+16,40),((axis+16,44),(axis+16,44),(axis+12,44)),(axis-12,44),((axis-16,44),(axis-16,44),(axis-16,40)),(axis-16,24),((axis-16,18),(axis-8,18),(axis-8,12)),(axis-10,12),((axis-14,12),(axis-14,4),(axis-10,4))],True)
        self.add_line('lid-seam',(axis-8,12),(axis+8,12))
        self.relate('connect','jar','lid-seam')

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
