from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c747f16a-3172-497d-9495-75b5f73d5aba'
SOURCE_PATH = 'pictographic-primitives/animals/skunk_c747f16a-3172-497d-9495-75b5f73d5aba.svg'
AUTHOR = 'gpt-6'


class Skunk(Solo48):
    icon_id = 'skunk'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "nature/animals"
    aliases = ()
    keywords = ('skunk', 'tail', 'bushy', 'stripe', 'animal', 'wildlife', 'spray', 'nocturnal')

    def build(self) -> None:
        # Wide raised tail and low right-facing body; extremes (2,5)-(46,43).
        self.add_arc('tail-top', (2, 18), (26, 18), radius_x=12, radius_y=13, sweep=True)
        self.add_arc('tail-turn', (26, 18), (20, 29), radius_x=13, radius_y=13, sweep=True)
        self.add_line('back', (20, 29), (31, 29))
        self.add_line('face-1', (31, 29), (34, 23))
        self.add_line('face-2', (34, 23), (39, 26))
        self.add_line('face-3', (39, 26), (46, 30))
        self.add_line('face-4', (46, 30), (41, 35))
        self.add_line('face-5', (41, 35), (36, 35))
        self.add_line('foreleg-1', (36, 35), (36, 43))
        self.add_line('foreleg-2', (36, 43), (30, 43))
        self.add_line('foreleg-3', (30, 43), (30, 36))
        self.add_line('belly', (30, 36), (19, 36))
        self.add_line('hindleg-1', (19, 36), (19, 43))
        self.add_line('hindleg-2', (19, 43), (11, 43))
        self.add_line('hindleg-3', (11, 43), (11, 31))
        self.add_arc('tail-inner', (11, 31), (16, 19), radius_x=17, radius_y=17, sweep=True)
        self.add_arc('stripe-crest', (16, 19), (2, 18), radius_x=7, radius_y=8, sweep=False)
        self.add_contour('silhouette', 'tail-top', 'tail-turn', 'back', 'face-1', 'face-2', 'face-3', 'face-4', 'face-5', 'foreleg-1', 'foreleg-2', 'foreleg-3', 'belly', 'hindleg-1', 'hindleg-2', 'hindleg-3', 'tail-inner', 'stripe-crest', closed=True)
