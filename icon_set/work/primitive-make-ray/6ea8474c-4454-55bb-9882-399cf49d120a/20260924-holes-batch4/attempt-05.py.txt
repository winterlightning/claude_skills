"""lesbian lgbt festival fair exhibition: repaired SOLO48 composition.
Plan: Mirrored lobes above a centered heart point.
Keyshape: SQUARE balances three repeated flags over the heart.
Reduction: No components omitted. Bunting flags deepened; heart shortened vertically.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '6ea8474c-4454-55bb-9882-399cf49d120a'
SOURCE_PATH = 'pictographic-primitives/romance/lesbian lgbt festival fair exhibition_6ea8474c-4454-55bb-9882-399cf49d120a.svg'
AUTHOR = "gpt-6"
CONSTRUCTION_REFERENCES = 'heart'

class Drawing(Solo48):
    icon_id = 'lesbian-lgbt-festival-fair-exhibition'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('lesbian lgbt festival fair exhibition',)

    def build(self):
        for (i, x) in enumerate((6, 18, 30)):
            self.add_polyline('flag-' + str(i), (x, 6), (x + 12, 6), (x + 6, 17), closed=True)
        for i in range(2):
            self.relate('connect', 'flag-' + str(i), 'flag-' + str(i + 1))
        self.add_arc('heart-left', (24, 32), (8, 32), radius_x=8, radius_y=6, sweep=False)
        self.add_line('heart-side-left', (8, 32), (24, 42))
        self.add_line('heart-side-right', (24, 42), (40, 32))
        self.add_arc('heart-right', (40, 32), (24, 32), radius_x=8, radius_y=6, sweep=False)
        self.add_contour('heart', 'heart-left', 'heart-side-left', 'heart-side-right', 'heart-right', closed=True)
