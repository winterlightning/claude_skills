"""Seated koala in right profile. Broad ears and upright nose retained; hidden limbs omitted. Asymmetry describes the seated pose; Lucide cat informs the coherent head outline."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7aff43af-b040-54db-ae24-ae746f735733'
SOURCE_PATH = 'pictographic-primitives/animals/koala body_7aff43af-b040-54db-ae24-ae746f735733.svg'
AUTHOR = 'gpt-6'


class SittingKoala(Solo48):
    icon_id = 'sitting-koala'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "nature/animals"
    aliases = ()
    keywords = ('koala', 'sitting', 'marsupial', 'australia', 'ears', 'animal', 'bear', 'zoo')

    def build(self) -> None:
        # VRECT_XL ink bounds (3, 0)-(45, 48). One continuous outer path.
        self.add_arc('crown-a', (15, 8), (23, 2), radius_x=8, radius_y=6)
        self.add_arc('crown-b', (23, 2), (31, 8), radius_x=8, radius_y=6)
        self.add_arc('right-ear-a', (31, 8), (43, 10), radius_x=7, radius_y=8)
        self.add_arc('right-ear-b', (43, 10), (35, 20), radius_x=8, radius_y=10)
        self.add_arc('cheek', (35, 20), (29, 26), radius_x=8)
        self.add_line('foreleg-top', (29, 26), (43, 28))
        self.add_arc('arm', (43, 28), (34, 34), radius_x=9, radius_y=6)
        self.add_line('foreleg', (34, 34), (32, 40))
        self.add_line('toe', (32, 40), (37, 38))
        self.add_arc('foot', (37, 38), (32, 46), radius_x=6, radius_y=8)
        self.add_line('base', (32, 46), (20, 46))
        self.add_arc('haunch', (20, 46), (9, 37), radius_x=11, radius_y=9)
        self.add_arc('back', (9, 37), (14, 26), radius_x=15)
        self.add_line('neck', (14, 26), (13, 20))
        self.add_arc('left-ear-b', (13, 20), (5, 10), radius_x=8, radius_y=10)
        self.add_arc('left-ear-a', (5, 10), (15, 8), radius_x=6, radius_y=8)
        self.add_contour(
            'outline', 'crown-a', 'crown-b', 'right-ear-a', 'right-ear-b',
            'cheek', 'foreleg-top', 'arm', 'foreleg', 'toe', 'foot', 'base',
            'haunch', 'back', 'neck', 'left-ear-b', 'left-ear-a', closed=True,
        )
        self.add_arc('knee', (32, 40), (23, 36), radius_x=9, radius_y=5, sweep=False)
        self.relate('connect', 'knee', 'outline')
        self.add_arc('nose-right', (24, 12), (24, 20), radius_x=3, radius_y=4)
        self.add_arc('nose-left', (24, 20), (24, 12), radius_x=3, radius_y=4)
        self.add_contour('nose', 'nose-right', 'nose-left', closed=True)
