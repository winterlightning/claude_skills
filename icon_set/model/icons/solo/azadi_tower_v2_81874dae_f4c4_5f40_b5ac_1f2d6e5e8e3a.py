from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '81874dae-f4c4-5f40-b5ac-1f2d6e5e8e3a'
SOURCE_PATH = 'pictographic-primitives/landmarks/batch-02/azadi tower iran_81874dae-f4c4-5f40-b5ac-1f2d6e5e8e3a.svg'
AUTHOR = 'gpt-6'

class AzadiTowerVariant2(Solo48):
    icon_id = 'azadi-tower-v2'
    variant_of = 'azadi-tower'
    variant_label = 'Exact keyshape envelope and clear spacing'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'places/landmarks'
    aliases = ()
    keywords = ('azadi', 'tower', 'iran', 'tehran', 'monument', 'arch', 'landmark', 'gate', 'architecture')

    def build(self) -> None:
        self.add_line('crown', (15, 6), (33, 6))
        self.add_line('right-neck', (33, 6), (35, 16))
        self.add_arc('right-shoulder', (35, 16), (40, 33), radius_x=34, sweep=False)
        self.add_line('right-flare', (40, 33), (42, 42))
        self.add_line('right-foot', (42, 42), (33, 42))
        self.add_line('right-opening-leg', (33, 42), (32, 33))
        self.add_arc('right-pointed-arch', (32, 33), (24, 16), radius_x=27, sweep=False)
        self.add_arc('left-pointed-arch', (24, 16), (16, 33), radius_x=27, sweep=False)
        self.add_line('left-opening-leg', (16, 33), (15, 42))
        self.add_line('left-foot', (15, 42), (6, 42))
        self.add_line('left-flare', (6, 42), (8, 33))
        self.add_arc('left-shoulder', (8, 33), (13, 16), radius_x=34, sweep=False)
        self.add_line('left-neck', (13, 16), (15, 6))
        self.add_contour('monument', 'crown', 'right-neck', 'right-shoulder', 'right-flare', 'right-foot', 'right-opening-leg', 'right-pointed-arch', 'left-pointed-arch', 'left-opening-leg', 'left-foot', 'left-flare', 'left-shoulder', 'left-neck', closed=True)
        self.add_arc('lower-arch-left', (16, 33), (24, 27), radius_x=10, sweep=True)
        self.add_arc('lower-arch-right', (24, 27), (32, 33), radius_x=10, sweep=True)
        self.add_contour('lower-arch', 'lower-arch-left', 'lower-arch-right')
        self.relate('connect', 'lower-arch', 'monument')
