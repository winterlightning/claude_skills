"""Shield (protection), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'c3034182-8272-438e-bd25-32ee58c63442'
SOURCE_PATH = 'pictographic-primitives/protection/shield_c3034182-8272-438e-bd25-32ee58c63442.svg'
AUTHOR = 'gpt-6'

class ShieldC3034182(Solo48):
    icon_id = 'shield-c3034182'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'protection'
    categories = ('protection', 'primitives')
    aliases = ()
    keywords = ('shield', 'protection')

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
        self._path('shield', (24, 4), [('L', (16, 8)), ('A', (8, 10), 16, 16, True), ('L', (8, 22)), ('A', (24, 44), 24, 24, False), ('A', (40, 22), 24, 24, False), ('L', (40, 10)), ('A', (32, 8), 16, 16, True), ('L', (24, 4))], True)
