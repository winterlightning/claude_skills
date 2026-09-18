"""Open Catalog with Dollar Sign -- batch-002 r2 generation.

Subject: an open product catalog (book) marked with a dollar sign for prices.

Plan: symmetric pages about the spine x=24. The page outline is one closed
contour. Its tops are gull-wing arcs (radius 82) that are level at the outer
corners and dip into the spine. Its outer edges are vertical, and its bottom
edges run down to the spine foot in a V. The spine is the dollar sign's bar.
It drops from the top dip into the S and continues from the S to the V. The
S is two half-ellipse bowls (rx 4, ry 4) with level terminals, as in the
typeface symbol-dollar.
Keyshape SQUARE; centerline box (6,6)-(42,42).
Reduction: the reference puts the dollar on the right page and three text
strokes on the left page. At 48 a centred spine leaves pages 18 wide, but a
legible 8-wide S needs about 26 with 4-unit ink clearance. The dollar
therefore moves into the gutter, where the spine doubles as its bar, and the
left-page strokes are dropped. Right-page and spineless layouts were drawn
and rejected: the S either crowded its own terminals (ry 3) or lost the book
read.
Construction reference: Lucide book-open (page tops dipping into a central
spine) and dollar-sign (level terminals over half-round bowls); typeface
glyph symbol-dollar consulted for proportions only, not copied.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._batch_002_r2_shapes import path

SOURCE_ICON_ID = '24fd53e6-156c-4466-9207-a789aa1d1627'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/business/workflow coaching product catalog_24fd53e6-156c-4466-9207-a789aa1d1627.svg'
EXPORTED_REFERENCE = 'work/brief-exports/20260918-all-todo-batches-15/batches/batch-002/references/workflow coaching product catalog_24fd53e6-156c-4466-9207-a789aa1d1627.svg'
AUTHOR = 'claude-opus-5'

SPINE = 24
LEFT, TOP, RIGHT, BOTTOM = 6, 6, 42, 42
SPINE_TOP, OUTER_BOTTOM, WING_RADIUS = 8, 38, 82
DOLLAR_CY, DOLLAR_RX, DOLLAR_RY = 25, 4, 4


class OpenCatalogWithDollarSignBatch002R2(Solo48):
    icon_id = 'open-catalog-with-dollar-sign-batch-002-r2'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/business'
    aliases = ('product-catalog', 'price-catalog', 'price-list')
    keywords = ('catalog', 'book', 'open', 'dollar', 'price', 'product', 'shopping', 'money')

    def build(self) -> None:
        spine_top, spine_foot = (SPINE, SPINE_TOP), (SPINE, BOTTOM)
        path(self, 'pages', spine_top,
             ('A', (RIGHT, TOP), WING_RADIUS, WING_RADIUS, True),
             ('L', (RIGHT, OUTER_BOTTOM)), ('L', spine_foot), ('L', (LEFT, OUTER_BOTTOM)),
             ('L', (LEFT, TOP)),
             ('A', spine_top, WING_RADIUS, WING_RADIUS, True), closed=True)

        x, y, rx, ry = SPINE, DOLLAR_CY, DOLLAR_RX, DOLLAR_RY
        s_top, s_bottom = (x, y - 2 * ry), (x, y + 2 * ry)
        self.add_line('spine-upper', spine_top, s_top)
        path(self, 'dollar', (x + rx, y - 2 * ry),
             ('L', s_top),
             ('A', (x, y), rx, ry, False),
             ('A', s_bottom, rx, ry, True),
             ('L', (x - rx, y + 2 * ry)))
        self.add_line('spine-lower', s_bottom, spine_foot)
        self.relate('connect', 'pages', 'spine-upper')
        self.relate('connect', 'spine-upper', 'dollar')
        self.relate('connect', 'dollar', 'spine-lower')
        self.relate('connect', 'spine-lower', 'pages')
