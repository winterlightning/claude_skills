"""Legal scale 1 (office), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'fdd3c820-b393-4768-9d70-ae254dcf010e'
SOURCE_PATH = 'pictographic-primitives/office/legal scale 1_fdd3c820-b393-4768-9d70-ae254dcf010e.svg'
AUTHOR = 'gpt-6'

class LegalScale1(Solo48):
    icon_id = 'legal-scale-1'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'office'
    aliases = ()
    keywords = ('legal', 'scale', 'office')

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
        self._circle('pivot', 24, 13, 5)
        self.add_line('post', (24, 18), (24, 40))
        self.add_line('foot', (16, 40), (32, 40))
        self.relate('connect', 'post', 'pivot')
        self.relate('connect', 'post', 'foot')
        for j, x in enumerate([10, 38]):
            n = f'pan-{j}'
            self.add_polyline(n + '-cord', (x - 6, 27), (x, 13), (x + 6, 27))
            self._path(n, (x - 6, 27), [('L', (x + 6, 27)), ('A', (x - 6, 27), 6, 7, True)], True)
            self.add_line(n + '-beam', (x, 13), (19 if j == 0 else 29, 13))
            self.relate('connect', n, n + '-cord')
            self.relate('connect', n + '-beam', n + '-cord')
            self.relate('connect', n + '-beam', 'pivot')
