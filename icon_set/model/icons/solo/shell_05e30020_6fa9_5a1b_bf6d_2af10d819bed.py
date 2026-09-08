from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '05e30020-6fa9-5a1b-bf6d-2af10d819bed'
SOURCE_PATH = 'pictographic-primitives/animals/shell_05e30020-6fa9-5a1b-bf6d-2af10d819bed.svg'
AUTHOR = 'gpt-6'


class ScallopShell(Solo48):
    icon_id = 'scallop-shell'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "animals/marine"
    aliases = ()
    keywords = ('shell', 'scallop', 'seashell', 'beach', 'ocean', 'ribs', 'marine', 'fan')

    def build(self) -> None:
        self.add_arc('crown', (16, 11), (32, 11), radius_x=8, radius_y=9, sweep=True, large_arc=False)
        self.add_arc('right-lobe', (32, 11), (42, 19), radius_x=10, radius_y=8, sweep=True, large_arc=False)
        self.add_arc('right-edge', (42, 19), (46, 27), radius_x=4, radius_y=8, sweep=True, large_arc=False)
        self.add_line('right-slope', (46, 27), (28, 42))
        self.add_arc('hinge', (28, 42), (20, 42), radius_x=4, radius_y=4, sweep=True, large_arc=False)
        self.add_line('left-slope', (20, 42), (2, 27))
        self.add_arc('left-edge', (2, 27), (6, 19), radius_x=4, radius_y=8, sweep=True, large_arc=False)
        self.add_arc('left-lobe', (6, 19), (16, 11), radius_x=10, radius_y=8, sweep=True, large_arc=False)
        self.add_contour('fan', 'crown', 'right-lobe', 'right-edge', 'right-slope', 'hinge', 'left-slope', 'left-edge', 'left-lobe', closed=True)
        self.add_line('rib-left', (16, 11), (19, 30))
        self.add_line('rib-right', (32, 11), (29, 30))
        self.relate("connect", 'rib-left', 'fan')
        self.relate("connect", 'rib-right', 'fan')
