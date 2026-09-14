"""Computer chip core (electronics), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '97ad08e4-d7db-5b0b-9fcc-6d4b0b6baf52'
SOURCE_PATH = 'icons-json/electronics/computer chip core_97ad08e4-d7db-5b0b-9fcc-6d4b0b6baf52.json'
AUTHOR = 'gpt-6'

class ComputerChipCore(Solo48):
    icon_id = 'computer-chip-core'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'electronics'
    aliases = ()
    keywords = ('computer', 'chip', 'core', 'electronics')

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
        self.add_polyline('body', (11, 11), (37, 11), (37, 37), (11, 37), closed=True)
        self.add_polyline('core', (20, 20), (28, 20), (28, 28), (20, 28), closed=True)
        for j, t in enumerate([16, 24, 32]):
            for side, a, b in [('t', (t, 6), (t, 11)), ('b', (t, 37), (t, 42)), ('l', (6, t), (11, t)), ('r', (37, t), (42, t))]:
                n = f'pin-{side}-{j}'
                self.add_line(n, a, b)
                self.relate('connect', n, 'body')
