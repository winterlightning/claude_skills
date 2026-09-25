"""Staffordshire bull terrier (pets), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'df4a92a8-7c60-5ef2-a1d3-1b6549f97e0b'
SOURCE_PATH = 'pictographic-primitives/pets/staffordshire bull terrier_df4a92a8-7c60-5ef2-a1d3-1b6549f97e0b.svg'
AUTHOR = 'gpt-6'

class StaffordshireBullTerrier(Solo48):
    icon_id = 'staffordshire-bull-terrier'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'pets'
    categories = ('pets', 'primitives')
    aliases = ()
    keywords = ('staffordshire', 'bull', 'terrier', 'pets')

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
        self.add_line('e0', (29, 27), (19, 27))
        self.add_line('e1', (24, 34), (24, 37))
        self.add_line('e2', (34, 27), (34, 36))
        self.add_line('e3', (15, 36), (14, 27))
        self.add_line('e4', (13, 21), (14, 17))
        self.add_line('e5', (19, 11), (29, 11))
        self.add_line('e6', (29, 11), (31, 10))
        self.add_line('e7', (31, 10), (34, 17))
        self.add_line('e8', (4, 19), (5, 15))
        self.add_line('e9', (44, 19), (43, 15))
        self.add_arc('e10', (19, 27), (29, 27), radius_x=5, radius_y=7, sweep=False)
        self.add_line('e11', (34, 17), (34, 27))
        self.add_arc('e12-1', (34, 36), (29, 40), radius_x=6)
        self.add_arc('e12-2', (29, 40), (24, 37), radius_x=6)
        self.add_arc('e13-1', (24, 37), (20, 40), radius_x=5)
        self.add_arc('e13-2', (20, 40), (15, 36), radius_x=6)
        self.add_arc('e14', (14, 27), (13, 21), radius_x=14)
        self.add_line('e15-1', (14, 17), (17, 10))
        self.add_line('e15-2', (17, 10), (19, 11))
        self.add_arc('e16', (14, 17), (4, 19), radius_x=13)
        self.add_arc('e17-1', (5, 15), (12, 8), radius_x=7)
        self.add_arc('e17-2', (12, 8), (17, 10), radius_x=8)
        self.add_arc('e18', (34, 17), (44, 19), radius_x=14, sweep=False)
        self.add_arc('e19-1', (43, 15), (36, 8), radius_x=7, sweep=False)
        self.add_line('e19-2', (36, 8), (31, 10))
        self.add_contour('c0', 'e0', 'e10', closed=True)
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e11', 'e2', 'e12-1', 'e12-2')
        self.add_contour('c3', 'e13-1', 'e13-2', 'e3', 'e14', 'e4')
        self.add_contour('c4', 'e15-1', 'e15-2', 'e5', 'e6', 'e7')
        self.add_contour('c5', 'e16', 'e8', 'e17-1', 'e17-2')
        self.add_contour('c6', 'e18', 'e9', 'e19-1', 'e19-2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c3', 'c5')
        self.relate('connect', 'c4', 'c5')
        self.relate('connect', 'c1', 'c0')
        self.relate('connect', 'c5', 'c4')
