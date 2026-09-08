from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b6b89579-fc5e-4e62-9315-3b593b0c12db'
SOURCE_PATH = 'pictographic-primitives/animals/shell sea grass_b6b89579-fc5e-4e62-9315-3b593b0c12db.svg'
AUTHOR = 'gpt-6'


class ShellWithSeagrass(Solo48):
    icon_id = 'shell-with-seagrass'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "animals/marine"
    aliases = ()
    keywords = ('shell', 'seagrass', 'seaweed', 'ocean', 'beach', 'marine', 'clam', 'underwater')

    def build(self) -> None:
        self.add_arc('shell', (2, 46), (36, 46), radius_x=17, radius_y=15, sweep=True, large_arc=False)
        self.add_line('base', (36, 46), (2, 46))
        self.add_contour('clam', 'shell', 'base', closed=True)
        self.add_arc('small-shell', (36, 35), (46, 46), radius_x=10, radius_y=11, sweep=True, large_arc=False)
        self.add_line('small-base', (46, 46), (36, 46))
        self.add_contour('small', 'small-shell', 'small-base', closed=False)
        self.relate("connect", 'small', 'clam')
        self.add_arc('left-a', (10, 7), (10, 15), radius_x=6, radius_y=6, sweep=False, large_arc=False)
        self.add_arc('left-b', (10, 15), (10, 23), radius_x=6, radius_y=6, sweep=True, large_arc=False)
        self.add_contour('left', 'left-a', 'left-b', closed=False)
        self.add_arc('middle-a', (24, 2), (24, 10), radius_x=6, radius_y=6, sweep=False, large_arc=False)
        self.add_arc('middle-b', (24, 10), (24, 18), radius_x=6, radius_y=6, sweep=True, large_arc=False)
        self.add_contour('middle', 'middle-a', 'middle-b', closed=False)
        self.add_arc('right-a', (38, 7), (38, 15), radius_x=6, radius_y=6, sweep=False, large_arc=False)
        self.add_arc('right-b', (38, 15), (38, 23), radius_x=6, radius_y=6, sweep=True, large_arc=False)
        self.add_contour('right', 'right-a', 'right-b', closed=False)
