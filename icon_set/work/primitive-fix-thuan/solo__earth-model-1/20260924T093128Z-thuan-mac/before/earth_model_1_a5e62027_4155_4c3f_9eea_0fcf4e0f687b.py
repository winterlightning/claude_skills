"""Earth model 1 (maps), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'a5e62027-4155-4c3f-9eea-0fcf4e0f687b'
SOURCE_PATH = 'pictographic-primitives/maps/earth model 1_a5e62027-4155-4c3f-9eea-0fcf4e0f687b.svg'
AUTHOR = 'gpt-6'

class EarthModel1(Solo48):
    icon_id = 'earth-model-1'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'maps'
    aliases = ()
    keywords = ('earth', 'model', 'maps')

    def _circle(self, name, x, y, r, ry=None):
        ry = r if ry is None else ry
        self.add_arc(name + '-a', (x - r, y), (x + r, y), radius_x=r, radius_y=ry)
        self.add_arc(name + '-b', (x + r, y), (x - r, y), radius_x=r, radius_y=ry)
        self.add_contour(name, name + '-a', name + '-b', closed=True)

    def _path(self, name, start, parts, closed=False):
        ids = []
        p = start
        for j, s in enumerate(parts):
            i = f'{name}-{j}'
            q = s[1]
            if s[0] == 'L':
                self.add_line(i, p, q)
            else:
                self.add_arc(i, p, q, radius_x=s[2], radius_y=s[3], sweep=s[4])
            ids.append(i)
            p = q
        self.add_contour(name, *ids, closed=closed)

    def build(self):
        """Use a flat pedestal bar with a real central stem; remove the pinched shallow stand counter."""
        self._circle('globe', 18, 16, 10)
        self._path('meridian', (32, 4), [('A', (40, 20), 20, 20, True), ('A', (22, 34), 18, 14, True), ('A', (8, 32), 24, 24, True)])
        self.add_line('stem', (22, 34), (22, 44))
        self.add_polyline('base', (13, 44), (22, 44), (31, 44))
        self.relate('connect', 'stem', 'meridian')
        self.relate('connect', 'stem', 'base')
