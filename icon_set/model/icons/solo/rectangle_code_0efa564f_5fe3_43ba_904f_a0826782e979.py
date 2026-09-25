"""A framed QR-code pattern.
Plan: SQUARE retains the rectangular code card. Visible ink bounds: (4, 4, 44, 44).
Reduction: Three complete finder squares reduced to one closed square, two open marks and a dot; their two-by-two positions remain.
Construction: Lucide scan-qr-code: one strong finder square plus reduced secondary code marks."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '0efa564f-5fe3-43ba-904f-a0826782e979'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_32/rectangle code_0efa564f-5fe3-43ba-904f-a0826782e979.svg'
AUTHOR = 'gpt-6'
PLAN = 'A framed QR-code pattern.'
OMISSIONS = 'Three complete finder squares reduced to one closed square, two open marks and a dot; their two-by-two positions remain.'
CONSTRUCTION_REFERENCES = 'Lucide scan-qr-code: one strong finder square plus reduced secondary code marks.'
KEYSHAPE_INK_BOUNDS = (4, 4, 44, 44)

class Drawing(Solo48):
    icon_id = 'rectangle-code'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('rectangle', 'code')

    def box(self, n, x, y, w, h, r=3):
        pts = [(x + r, y), (x + w - r, y), (x + w, y + r), (x + w, y + h - r), (x + w - r, y + h), (x + r, y + h), (x, y + h - r), (x, y + r)]
        names = []
        for (j, a) in enumerate(pts):
            b = pts[(j + 1) % 8]
            name = f'{n}-{j}'
            names.append(name)
            if j % 2:
                self.add_arc(name, a, b, radius_x=r)
            else:
                self.add_line(name, a, b)
        self.add_contour(n, *names, closed=True)

    def build(self):
        self.box('frame', 6, 6, 36, 36, 4)
        self.add_polyline('finder', (15, 15), (23, 15), (23, 23), (15, 23), closed=True)
        self.add_line('top-right', (33, 15), (33, 23))
        self.add_polyline('bottom-left', (15, 32), (15, 33), (23, 33))
        self.add_dot('bottom-right', (33, 33))
