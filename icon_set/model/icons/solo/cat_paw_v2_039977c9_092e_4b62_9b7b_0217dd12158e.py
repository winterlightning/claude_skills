# Variant of cat-paw; parent file remains unchanged.
'cat-paw: Rebalanced the toe lobes and palm; removed two crowded side dots. Keyshape VRECT_L; SOLO48 stroke 4. Reviewed at 48 px in both themes.'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '039977c9-092e-4b62-9b7b-0217dd12158e'
SOURCE_PATH = 'pictographic-primitives/animals/cat pawn_039977c9-092e-4b62-9b7b-0217dd12158e.svg'
AUTHOR = 'gpt-6'

class CatPawVariant2(Solo48):
    icon_id = 'cat-paw-v2'
    variant_of = 'cat-paw'
    variant_label = 'Correct width and full spacing review'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/animals'
    aliases = ()
    keywords = ('cat', 'paw', 'print', 'pad', 'toe', 'pet', 'animal', 'foot')

    def build(self) -> None:
        # Two broad toe lobes and two separated toe pads; omit crowded side dots.
        self.add_line('leg-left', (8, 44), (8, 18))
        self.add_arc('outer-toe-left', (8, 18), (14, 12), radius_x=6)
        self.add_arc('inner-toe-left', (14, 12), (24, 12), radius_x=5, radius_y=8)
        self.add_arc('inner-toe-right', (24, 12), (34, 12), radius_x=5, radius_y=8)
        self.add_arc('outer-toe-right', (34, 12), (40, 18), radius_x=6)
        self.add_line('leg-right', (40, 18), (40, 44))
        self.add_contour('outline', 'leg-left', 'outer-toe-left', 'inner-toe-left', 'inner-toe-right', 'outer-toe-right', 'leg-right')
        self.add_dot('toe-left', (18, 21))
        self.add_dot('toe-right', (30, 21))
        self.add_arc('palm-left', (17, 38), (24, 32), radius_x=7, radius_y=6)
        self.add_arc('palm-right', (24, 32), (31, 38), radius_x=7, radius_y=6)
        self.add_arc('palm-base-right', (31, 38), (24, 42), radius_x=7, radius_y=4)
        self.add_arc('palm-base-left', (24, 42), (17, 38), radius_x=7, radius_y=4)
        self.add_contour('palm', 'palm-left', 'palm-right', 'palm-base-right', 'palm-base-left', closed=True)
