"""Ghost scare (smileys), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'd3eaffac-83bd-5771-b93b-97075edcfae5'
SOURCE_PATH = 'icons-json/smileys/ghost scare_d3eaffac-83bd-5771-b93b-97075edcfae5.json'
AUTHOR = 'gpt-6'

class GhostScareVariant2(Solo48):
    icon_id = 'ghost-scare-v2'
    variant_of = 'ghost-scare'
    variant_label = 'Open counters and smoother curves'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'smileys'
    aliases = ()
    keywords = ('ghost', 'scare', 'smileys')

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
        self._path('body', (15, 17), [('A', (33, 17), 9, 9, True), ('L', (33, 32)), ('L', (38, 40)), ('L', (31, 38)), ('L', (24, 40)), ('L', (17, 38)), ('L', (10, 40)), ('L', (15, 32)), ('L', (15, 17))], True)
        for j in range(2):

            def P(x, y):
                return (x, y) if j == 0 else (48 - x, y)
            n = f'arm-{j}'
            self._path(n, P(15, 20), [('L', P(4, 15)), ('A', P(15, 32), 11, 17, j == 1)])
            self.relate('connect', n, 'body')
