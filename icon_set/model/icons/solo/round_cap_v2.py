"""Round cap (construction), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '30e26f6b-4595-560c-bfbe-0115d910a155'
SOURCE_PATH = 'icons-json/construction/round cap_30e26f6b-4595-560c-bfbe-0115d910a155.json'
AUTHOR = 'gpt-6'

class RoundCapVariant2(Solo48):
    icon_id = 'round-cap-v2'
    variant_of = 'round-cap'
    variant_label = 'Open counters and smoother curves'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'construction'
    aliases = ()
    keywords = ('round', 'cap', 'construction')

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
        self._path('outer', (44, 8), [('L', (20, 8)), ('A', (20, 40), 16, 16, False), ('L', (44, 40))])
        self._circle('loop', 19, 24, 5)
        self.add_line('rail', (24, 24), (44, 24))
        self.relate('connect', 'loop', 'rail')
