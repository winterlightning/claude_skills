"""Strategy split (arrows), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'c8a64710-b7eb-5217-beec-39744ce7d77c'
SOURCE_PATH = 'pictographic-primitives/arrows/strategy split_c8a64710-b7eb-5217-beec-39744ce7d77c.svg'
AUTHOR = 'gpt-6'

class StrategySplit(Solo48):
    icon_id = 'strategy-split'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    categories = ('arrows', 'primitives')
    aliases = ()
    keywords = ('strategy', 'split', 'arrows')

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
        self.add_polyline('up', (17, 18), (24, 6), (31, 18), closed=True)
        self.add_polyline('left', (6, 21), (18, 23), (9, 34), closed=True)
        self.add_polyline('right', (42, 21), (30, 23), (39, 34), closed=True)
        self.add_polyline('stem', (24, 42), (24, 38), (24, 18))
        self.relate('connect', 'stem', 'up')
        for n, p, sweep in [('left', (14, 28), False), ('right', (34, 28), True)]:
            self.add_arc(n + '-branch', (24, 38), p, radius_x=10, radius_y=10, sweep=sweep)
            self.relate('connect', 'stem', n + '-branch')
            self.relate('connect', n, n + '-branch')
