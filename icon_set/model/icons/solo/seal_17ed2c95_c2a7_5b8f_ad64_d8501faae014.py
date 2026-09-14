"""whiskered-seal: SQUARE ink (6,6)-(42,42). Mirrored bell body and two whiskers per cheek."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '17ed2c95-c2a7-5b8f-ad64-d8501faae014'
SOURCE_PATH = 'pictographic-primitives/animals/seal_17ed2c95-c2a7-5b8f-ad64-d8501faae014.svg'
AUTHOR = 'gpt-6'


class WhiskeredSeal(Solo48):
    icon_id = 'whiskered-seal'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "animals/marine"
    aliases = ()
    keywords = ('seal', 'whiskers', 'marine', 'flippers', 'animal', 'ocean', 'sea', 'front')

    def build(self) -> None:
        self.add_arc('body-1', (24, 6), (38, 16), radius_x=14, radius_y=14, sweep=True)
        self.add_line('body-2', (38, 16), (39, 24))
        self.add_arc('body-3', (39, 24), (42, 42), radius_x=46, radius_y=46, sweep=False)
        self.add_arc('body-4', (42, 42), (35, 42), radius_x=11, radius_y=3, sweep=True)
        self.add_line('body-5', (35, 42), (32, 42))
        self.add_arc('body-6', (32, 42), (16, 42), radius_x=20, radius_y=14, sweep=True)
        self.add_line('body-7', (16, 42), (13, 42))
        self.add_arc('body-8', (13, 42), (6, 42), radius_x=11, radius_y=3, sweep=True)
        self.add_arc('body-9', (6, 42), (9, 24), radius_x=46, radius_y=46, sweep=False)
        self.add_line('body-10', (9, 24), (10, 16))
        self.add_arc('body-11', (10, 16), (24, 6), radius_x=14, radius_y=14, sweep=True)
        self.add_contour('body', 'body-1', 'body-2', 'body-3', 'body-4', 'body-5', 'body-6', 'body-7', 'body-8', 'body-9', 'body-10', 'body-11', closed=True)
        self.add_line('whisker-left-top-1', (10, 16), (6, 13))
        self.add_contour('whisker-left-top', 'whisker-left-top-1', closed=False)
        self.add_line('whisker-left-low-1', (9, 24), (6, 27))
        self.add_contour('whisker-left-low', 'whisker-left-low-1', closed=False)
        self.add_line('whisker-right-top-1', (38, 16), (42, 13))
        self.add_contour('whisker-right-top', 'whisker-right-top-1', closed=False)
        self.add_line('whisker-right-low-1', (39, 24), (42, 27))
        self.add_contour('whisker-right-low', 'whisker-right-low-1', closed=False)
        self.relate("connect", 'body', 'whisker-left-top')
        self.relate("connect", 'body', 'whisker-right-top')
        self.relate("connect", 'body', 'whisker-left-low')
        self.relate("connect", 'body', 'whisker-right-low')
