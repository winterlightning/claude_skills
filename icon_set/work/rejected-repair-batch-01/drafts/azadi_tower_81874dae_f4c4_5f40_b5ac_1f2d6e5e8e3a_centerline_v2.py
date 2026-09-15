"""Give the landmark smoother flared shoulders with matched vertical tangents at the crown; widen the base transition on both sides.
Independent centerline revision; original snapshot preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '81874dae-f4c4-5f40-b5ac-1f2d6e5e8e3a'
SOURCE_PATH = 'pictographic-primitives/landmarks/batch-02/azadi tower iran_81874dae-f4c4-5f40-b5ac-1f2d6e5e8e3a.svg'
AUTHOR = 'gpt-6'

class AzadiTower(Solo48):
    icon_id = 'azadi-tower-centerline-v2'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'places/landmarks'
    aliases = ()
    keywords = ('azadi', 'tower', 'iran', 'tehran', 'monument', 'arch', 'landmark', 'gate', 'architecture')

    def build(self) -> None:
        axis = 24
        self.add_line('crown', (12, 6), (36, 6))
        self.add_bezier('right-shoulder', (36, 6), ((36, 20), (38, 30), (42, 42)))
        self.add_line('right-foot', (42, 42), (32, 42))
        self.add_line('right-opening-leg', (32, 42), (30, 33))
        self.add_arc('right-pointed-arch', (30, 33), (axis, 16), radius_x=27, sweep=False)
        self.add_arc('left-pointed-arch', (axis, 16), (18, 33), radius_x=27, sweep=False)
        self.add_line('left-opening-leg', (18, 33), (16, 42))
        self.add_line('left-foot', (16, 42), (6, 42))
        self.add_bezier('left-shoulder', (6, 42), ((10, 30), (12, 20), (12, 6)))
        self.add_contour('monument', 'crown', 'right-shoulder', 'right-foot', 'right-opening-leg', 'right-pointed-arch', 'left-pointed-arch', 'left-opening-leg', 'left-foot', 'left-shoulder', closed=True)
        self.add_arc('lower-arch-left', (18, 33), (axis, 27), radius_x=10)
        self.add_arc('lower-arch-right', (axis, 27), (30, 33), radius_x=10)
        self.add_contour('lower-arch', 'lower-arch-left', 'lower-arch-right')
        self.relate('connect', 'lower-arch', 'monument')
    variant_of = 'azadi-tower'
    variant_label = 'Batch 01 centerline repair'
