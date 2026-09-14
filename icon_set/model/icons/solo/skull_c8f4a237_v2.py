"""Skull (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'c8f4a237-2d49-56fe-b32e-7b5ef8c9b2b1'
SOURCE_PATH = 'icons-json/interface-essential/skull_c8f4a237-2d49-56fe-b32e-7b5ef8c9b2b1.json'
AUTHOR = 'gpt-6'

class SkullC8f4a237Variant2(Solo48):
    icon_id = 'skull-c8f4a237-v2'
    variant_of = 'skull-c8f4a237'
    variant_label = 'Open counters and smoother curves'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('skull', 'interface-essential')

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
        self._path('skull', (6, 24), [('A', (42, 24), 18, 18, True), ('A', (34, 34), 8, 10, True), ('L', (34, 38)), ('A', (30, 42), 4, 4, True), ('L', (18, 42)), ('A', (14, 38), 4, 4, True), ('L', (14, 34)), ('A', (6, 24), 8, 10, True)], True)
        self.add_dot('left-eye', (16, 20))
        self.add_dot('right-eye', (32, 20))
        self._circle('nose', 24, 28, 3)
        self.add_line('tooth', (24, 40), (24, 42))
        self.relate('connect', 'tooth', 'skull')
