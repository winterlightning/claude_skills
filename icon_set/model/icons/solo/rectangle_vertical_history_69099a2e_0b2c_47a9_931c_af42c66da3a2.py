"""A history clock mark inside a panel.
Plan: SQUARE widens the source portrait panel to make room around the return arc. Visible ink bounds: (4, 4, 44, 44).
Reduction: Hour hand omitted; one radial clock hand retained and joined to the arc at an explicit endpoint. Arrowhead shortened.
Construction: No local Lucide history original was available; quarter-circle construction and the supplied reference guide the mark."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '69099a2e-0b2c-47a9-931c-af42c66da3a2'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_32/rectangle vertical history_69099a2e-0b2c-47a9-931c-af42c66da3a2.svg'
AUTHOR = 'gpt-6'
PLAN = 'A history clock mark inside a panel.'
OMISSIONS = 'Hour hand omitted; one radial clock hand retained and joined to the arc at an explicit endpoint. Arrowhead shortened.'
CONSTRUCTION_REFERENCES = 'No local Lucide history original was available; quarter-circle construction and the supplied reference guide the mark.'
KEYSHAPE_INK_BOUNDS = (4, 4, 44, 44)

class Drawing(Solo48):
    icon_id = 'rectangle-vertical-history'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/general'
    aliases = ()
    keywords = ('rectangle', 'vertical', 'history')

    def box(self, name, x, y, w, h, r=3):
        pts = [(x + r, y), (x + w - r, y), (x + w, y + r), (x + w, y + h - r), (x + w - r, y + h), (x + r, y + h), (x, y + h - r), (x, y + r)]
        members = []
        for (i, a) in enumerate(pts):
            b = pts[(i + 1) % 8]
            part = f'{name}-{i}'
            members.append(part)
            if i % 2:
                self.add_arc(part, a, b, radius_x=r)
            else:
                self.add_line(part, a, b)
        self.add_contour(name, *members, closed=True)

    def build(self):
        self.box('panel', 6, 6, 36, 36, 4)
        pts = [(24, 33), (15, 24), (24, 15), (33, 24)]
        for (j, (a, b)) in enumerate(zip(pts, pts[1:])):
            self.add_arc(f'history-{j}', a, b, radius_x=9)
        self.add_contour('history', *(f'history-{j}' for j in range(3)))
        self.add_polyline('arrow', (32, 22), (33, 24), (33, 21))
        self.relate('connect', 'history', 'arrow')
        self.add_line('clock-hand', (24, 15), (24, 24))
        self.relate('connect', 'history', 'clock-hand')
