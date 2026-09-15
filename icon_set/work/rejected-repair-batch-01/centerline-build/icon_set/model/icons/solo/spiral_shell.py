# Review candidate; original preserved.
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '2edb1386-cc42-5319-ac47-13902a62e1ed'
SOURCE_PATH = 'pictographic-primitives/animals/shell_2edb1386-cc42-5319-ac47-13902a62e1ed.svg'
AUTHOR = 'gpt-6'

class SpiralShell(Solo48):
    icon_id = 'spiral-shell'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'animals/marine'
    aliases = ()
    keywords = ('shell', 'spiral', 'snail', 'nautilus', 'sea', 'beach', 'coil', 'marine')

    def build(self) -> None:
        """Opening repair: Rebuilt the whorl from tangent half-ellipses with wider turn spacing and exact square bounds."""
        self.add_arc('outer-upper', (42, 24), (6, 24), radius_x=18, sweep=False)
        self.add_arc('outer-lower', (6, 24), (32, 24), radius_x=13, radius_y=18, sweep=False)
        self.add_arc('middle-upper', (32, 24), (16, 24), radius_x=8, radius_y=8, sweep=False)
        self.add_arc('inner-lower', (16, 24), (22, 24), radius_x=3, radius_y=3, sweep=False)
        self.add_contour('spiral', 'outer-upper', 'outer-lower', 'middle-upper', 'inner-lower')
