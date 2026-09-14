"""Canoe paddles (outdoors), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '88951f09-c14f-56fa-8f5d-241e2d118cb3'
SOURCE_PATH = 'icons-json/outdoors/canoe paddles_88951f09-c14f-56fa-8f5d-241e2d118cb3.json'
AUTHOR = 'gpt-6'

class CanoePaddlesOutdoorsVariant2(Solo48):
    icon_id = 'canoe-paddles-outdoors-v2'
    variant_of = 'canoe-paddles-outdoors'
    variant_label = 'Open counters and smoother curves'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'outdoors'
    aliases = ()
    keywords = ('canoe', 'paddles', 'outdoors')

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
        for j in range(2):

            def P(x, y):
                return (x, y) if j == 0 else (48 - x, 48 - y)
            n = f'blade-{j}'
            self._path(n, P(8, 10), [('A', P(20, 10), 6, 6, True), ('L', P(20, 19)), ('L', P(14, 25)), ('L', P(8, 19)), ('L', P(8, 10))], True)
            self.add_line(n + '-bar', P(8, 14), P(20, 14))
            self.add_line(n + '-shaft', P(14, 25), P(14, 44))
            self.relate('connect', n, n + '-bar')
            self.relate('connect', n, n + '-shaft')
