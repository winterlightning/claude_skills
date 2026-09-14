"""Megaphone (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '7a36c569-3305-4077-ab3c-e8e178a28776'
SOURCE_PATH = 'icons-json/interface-essential/megaphone_7a36c569-3305-4077-ab3c-e8e178a28776.json'
AUTHOR = 'gpt-6'

class Megaphone7a36c569(Solo48):
    icon_id = 'megaphone-7a36c569'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('megaphone', 'interface-essential')

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
        self.add_line('e0', (42, 27), (8, 35))
        self.add_line('e1', (8, 35), (6, 33))
        self.add_line('e2', (6, 33), (31, 6))
        self.add_line('e3', (31, 6), (42, 27))
        self.add_arc('e4-1', (29, 30), (21, 42), radius_x=10)
        self.add_arc('e4-2', (21, 42), (13, 34), radius_x=10)
        self.add_contour('c0', 'e4-1', 'e4-2')
        self.add_contour('c1', 'e0', 'e1', 'e2', 'e3', closed=True)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c1')
