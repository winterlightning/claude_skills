"""Nagras (money), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '84618b8f-5dee-4f44-9380-893ba067f0b2'
SOURCE_PATH = 'icons-json/money/nagras_84618b8f-5dee-4f44-9380-893ba067f0b2.json'
AUTHOR = 'gpt-6'

class NagrasMoney(Solo48):
    icon_id = 'nagras-money'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'money'
    aliases = ()
    keywords = ('nagras', 'money')

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
        self.add_polyline('letter', (10, 44), (10, 4), (38, 44), (38, 4))
        for j, y in enumerate([20, 28]):
            self.add_line(f'bar-{j}', (8, y), (40, y))
            self.relate('connect', 'letter', f'bar-{j}')
