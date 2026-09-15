"""Diamond shine (money), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '75340985-f83d-4e1e-ae44-738cb3face8c'
SOURCE_PATH = 'pictographic-primitives/money/diamond shine_75340985-f83d-4e1e-ae44-738cb3face8c.svg'
AUTHOR = 'gpt-6'

class DiamondShine(Solo48):
    icon_id = 'diamond-shine'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'money'
    aliases = ()
    keywords = ('diamond', 'shine', 'money')

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
        self.add_polyline('outline', (24, 4), (32, 14), (32, 30), (24, 44), (16, 30), (16, 14), closed=True)
        self.add_polyline('top', (16, 14), (24, 18), (32, 14))
        self.add_polyline('bottom', (16, 30), (24, 30), (32, 30))
        self.add_line('spine', (24, 18), (24, 30))
        for a, b in [('outline', 'top'), ('outline', 'bottom'), ('top', 'spine'), ('bottom', 'spine')]:
            self.relate('connect', a, b)
        for j, x in enumerate([8, 40]):
            self.add_line(f'ray-{j}', (x, 19), (x, 25))
