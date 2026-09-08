"""Palm-on cat paw continuing into an open leg. Lucide paw-print informs separated pads; four toe pads become dots and the central pad uses a broad rounded contour for clearance."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '039977c9-092e-4b62-9b7b-0217dd12158e'
SOURCE_PATH = 'pictographic-primitives/animals/cat pawn_039977c9-092e-4b62-9b7b-0217dd12158e.svg'
AUTHOR = 'gpt-6'


class CatPaw(Solo48):
    icon_id = 'cat-paw'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/animals"
    aliases = ()
    keywords = ('cat', 'paw', 'print', 'pad', 'toe', 'pet', 'animal', 'foot')

    def build(self) -> None:
        # VRECT_XL centerline extremes recorded in batch-02-review.md.
        self.add_line('leg-left', (5, 46), (5, 16))
        self.add_arc('outer-toe-left', (5, 16), (12, 9), radius_x=7, radius_y=7, sweep=True)
        self.add_arc('inner-toe-left', (12, 9), (24, 9), radius_x=6, radius_y=7, sweep=True)
        self.add_arc('inner-toe-right', (24, 9), (36, 9), radius_x=6, radius_y=7, sweep=True)
        self.add_arc('outer-toe-right', (36, 9), (43, 16), radius_x=7, radius_y=7, sweep=True)
        self.add_line('leg-right', (43, 16), (43, 46))
        self.add_contour('outline', 'leg-left', 'outer-toe-left', 'inner-toe-left', 'inner-toe-right', 'outer-toe-right', 'leg-right', closed=False)
        self.add_dot('pad-outer-left', (13, 20))
        self.add_dot('pad-inner-left', (18, 13))
        self.add_dot('pad-inner-right', (30, 13))
        self.add_dot('pad-outer-right', (35, 21))
        self.add_arc('palm-left', (15, 35), (24, 26), radius_x=9, radius_y=9, sweep=True)
        self.add_arc('palm-right', (24, 26), (33, 35), radius_x=9, radius_y=9, sweep=True)
        self.add_arc('pad-base-right', (33, 35), (24, 39), radius_x=9, radius_y=4, sweep=True)
        self.add_arc('pad-base-left', (24, 39), (15, 35), radius_x=9, radius_y=4, sweep=True)
        self.add_contour('palm', 'palm-left', 'palm-right', 'pad-base-right', 'pad-base-left', closed=True)
