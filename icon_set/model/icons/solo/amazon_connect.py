"""Amazon connect (programing), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '00b02f02-c0d5-4245-8a8e-8f209b070186'
SOURCE_PATH = 'pictographic-primitives/programing/amazon connect_00b02f02-c0d5-4245-8a8e-8f209b070186.svg'
AUTHOR = 'gpt-6'

class AmazonConnect(Solo48):
    icon_id = 'amazon-connect'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'programing'
    aliases = ()
    keywords = ('amazon', 'connect', 'programing')

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
        for name, x, y in [('top', 24, 13), ('left', 9, 35), ('right', 39, 35)]:
            self._circle(name, x, y, 5)
        self.add_polyline('branches', (9, 30), (24, 18), (39, 30))
        for n in ['top', 'left', 'right']:
            self.relate('connect', n, 'branches')
