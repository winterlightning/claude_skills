"""Meeting headphone wireless (office), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '5b320b4e-ed89-4f2f-be89-6e9fdbbeecce'
SOURCE_PATH = 'pictographic-primitives/office/meeting headphone wireless_5b320b4e-ed89-4f2f-be89-6e9fdbbeecce.svg'
AUTHOR = 'gpt-6'

class MeetingHeadphoneWireless(Solo48):
    icon_id = 'meeting-headphone-wireless'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'office'
    categories = ('office', 'primitives')
    aliases = ()
    keywords = ('meeting', 'headphone', 'wireless', 'office')

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
        self.add_arc('signal', (14, 8), (34, 8), radius_x=10, radius_y=4)
        self.add_arc('band', (8, 29), (40, 29), radius_x=16, radius_y=12)
        for j, x in enumerate([8, 32]):
            n = f'cup-{j}'
            self._path(n, (x, 29), [('L', (x + 8, 29)), ('L', (x + 8, 36)), ('A', (x + 4, 40), 4, 4, True), ('A', (x, 36), 4, 4, True), ('L', (x, 29))], True)
            self.relate('connect', n, 'band')
        self._circle('mic', 24, 40, 4)
        self._path('boom', (36, 40), [('A', (32, 44), 4, 4, True), ('L', (24, 44))])
        self.relate('connect', 'boom', 'cup-1')
        self.relate('connect', 'boom', 'mic')
