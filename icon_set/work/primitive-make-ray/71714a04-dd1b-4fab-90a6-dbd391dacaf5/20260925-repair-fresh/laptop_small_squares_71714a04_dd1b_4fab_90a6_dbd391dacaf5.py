"""laptop small squares: fresh SOLO48 repair.
Plan: Shared screen hinges and base; two identical 8-unit outlined squares.
Keyshape: SQUARE. A taller laptop was tried to make room for two vertically stacked boxes.
Omissions: No defining feature removed. This attempt remains blocked.
Construction reference: No useful additional Lucide match inspected; supplied laptop reference governs construction.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '71714a04-dd1b-4fab-90a6-dbd391dacaf5'
SOURCE_PATH = 'pictographic-primitives/other/laptop small squares_71714a04-dd1b-4fab-90a6-dbd391dacaf5.svg'
AUTHOR = 'gpt-6'
PARENT_SOURCE = 'icon_set/model/icons/solo/laptop_small_squares_71714a04_dd1b_4fab_90a6_dbd391dacaf5.py'

class Drawing(Solo48):
    icon_id = 'laptop-small-squares'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('laptop small squares',)

    def laptop(self):
        self.add_line('screen-left', (10, 34), (10, 10))
        self.add_arc('screen-tl', (10, 10), (14, 6), radius_x=4)
        self.add_line('screen-top', (14, 6), (34, 6))
        self.add_arc('screen-tr', (34, 6), (38, 10), radius_x=4)
        self.add_line('screen-right', (38, 10), (38, 34))
        self.add_line('hinge', (38, 34), (10, 34))
        self.add_contour('screen', 'screen-left', 'screen-tl', 'screen-top', 'screen-tr', 'screen-right', 'hinge', closed=True)
        self.add_polyline('base', (10, 34), (6, 42), (42, 42), (38, 34))
        self.relate('connect', 'screen', 'base')

    def build(self):
        self.laptop()
        tile = 8
        for i, y in enumerate((14, 26)):
            self.add_polyline('tile-' + str(i), (18, y), (18 + tile, y), (18 + tile, y + tile), (18, y + tile), closed=True)
