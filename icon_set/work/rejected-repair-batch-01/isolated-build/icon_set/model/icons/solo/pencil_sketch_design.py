"""Pencil sketch (design), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '7867b811-86a3-5125-8824-2c83f4113979'
SOURCE_PATH = 'pictographic-primitives/design/pencil sketch_7867b811-86a3-5125-8824-2c83f4113979.svg'
AUTHOR = 'gpt-6'

class PencilSketchDesign(Solo48):
    icon_id = 'pencil-sketch-design'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    aliases = ()
    keywords = ('pencil', 'sketch', 'design')

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
        self.add_line('sym-e0', (35, 21), (27, 13))
        self.add_line('sym-e1', (27, 13), (33, 7))
        self.add_arc('sym-e2', (33, 7), (35, 6), radius_x=3)
        self.add_arc('sym-e5', (35, 6), (39, 9), radius_x=10)
        self.add_arc('sym-e6', (39, 9), (42, 13), radius_x=10)
        self.add_arc('sym-e9', (42, 13), (41, 15), radius_x=3)
        self.add_line('sym-e10', (41, 15), (35, 21))
        self.add_line('sym-e11', (35, 21), (17, 39))
        self.add_line('sym-e12', (17, 39), (13, 35))
        self.add_line('sym-e13', (13, 35), (9, 31))
        self.add_line('sym-e14', (9, 31), (27, 13))
        self.add_line('sym-e15', (17, 39), (6, 42))
        self.add_line('sym-e16', (6, 42), (9, 31))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e5', 'sym-e6', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14')
        self.add_contour('sym-c1', 'sym-e15', 'sym-e16')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
