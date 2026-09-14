"""Presentation (office), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '17f53de2-7f28-4023-80ae-484c48ce0e0e'
SOURCE_PATH = 'icons-json/office/presentation_17f53de2-7f28-4023-80ae-484c48ce0e0e.json'
AUTHOR = 'gpt-6'

class PresentationVariant2(Solo48):
    icon_id = 'presentation-v2'
    variant_of = 'presentation'
    variant_label = 'Open counters and smoother curves'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'office'
    aliases = ()
    keywords = ('presentation', 'office')

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
        self.add_line('rail', (4, 8), (44, 8))
        self.add_polyline('screen', (8, 8), (8, 25), (24, 25), (40, 25), (40, 8))
        self.relate('connect', 'screen', 'rail')
        self._circle('pull', 24, 35, 5)
        self.add_line('cord', (24, 25), (24, 30))
        self.relate('connect', 'cord', 'screen')
        self.relate('connect', 'cord', 'pull')
