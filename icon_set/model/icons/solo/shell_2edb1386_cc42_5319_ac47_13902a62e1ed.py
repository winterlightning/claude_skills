from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2edb1386-cc42-5319-ac47-13902a62e1ed'
SOURCE_PATH = 'pictographic-primitives/animals/shell_2edb1386-cc42-5319-ac47-13902a62e1ed.svg'
AUTHOR = 'gpt-6'


class SpiralShell(Solo48):
    icon_id = 'spiral-shell'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "animals/marine"
    aliases = ()
    keywords = ('shell', 'spiral', 'snail', 'nautilus', 'sea', 'beach', 'coil', 'marine')

    def build(self) -> None:
        self.add_arc('outer-lower', (46, 24), (2, 24), radius_x=22, radius_y=22, sweep=True, large_arc=False)
        self.add_arc('outer-upper', (2, 24), (38, 24), radius_x=18, radius_y=22, sweep=True, large_arc=False)
        self.add_arc('middle-lower', (38, 24), (12, 24), radius_x=13, radius_y=13, sweep=True, large_arc=False)
        self.add_arc('middle-upper', (12, 24), (28, 24), radius_x=8, radius_y=8, sweep=True, large_arc=False)
        self.add_arc('inner', (28, 24), (22, 24), radius_x=3, radius_y=3, sweep=True, large_arc=False)
        self.add_contour('whorl', 'outer-lower', 'outer-upper', 'middle-lower', 'middle-upper', 'inner', closed=False)
