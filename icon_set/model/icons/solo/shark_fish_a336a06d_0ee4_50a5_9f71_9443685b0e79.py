"""swimming-shark: HRECT_XL ink (6,6)-(42,42). Full torpedo body leaves room for detached gill; swept fins and fork tail."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a336a06d-0ee4-50a5-9f71-9443685b0e79'
SOURCE_PATH = 'pictographic-primitives/animals/shark fish_a336a06d-0ee4-50a5-9f71-9443685b0e79.svg'
AUTHOR = 'gpt-6'


class SwimmingShark(Solo48):
    icon_id = 'swimming-shark'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "animals/marine"
    aliases = ()
    keywords = ('shark', 'swim', 'sea', 'ocean', 'fin', 'fish', 'predator', 'marine')

    def build(self) -> None:
        self.add_arc('body-1', (6, 25), (19, 15), radius_x=30, radius_y=24, sweep=True)
        self.add_arc('body-2', (19, 15), (27, 6), radius_x=18, radius_y=18, sweep=True)
        self.add_line('body-3', (27, 6), (27, 17))
        self.add_arc('body-4', (27, 17), (38, 22), radius_x=36, radius_y=28, sweep=True)
        self.add_arc('body-5', (38, 22), (42, 13), radius_x=20, radius_y=20, sweep=True)
        self.add_arc('body-6', (42, 13), (42, 37), radius_x=32, radius_y=32, sweep=False)
        self.add_arc('body-7', (42, 37), (38, 30), radius_x=20, radius_y=20, sweep=True)
        self.add_arc('body-8', (38, 30), (26, 35), radius_x=36, radius_y=28, sweep=True)
        self.add_line('body-9', (26, 35), (26, 42))
        self.add_line('body-10', (26, 42), (19, 35))
        self.add_arc('body-11', (19, 35), (6, 25), radius_x=30, radius_y=24, sweep=True)
        self.add_contour('body', 'body-1', 'body-2', 'body-3', 'body-4', 'body-5', 'body-6', 'body-7', 'body-8', 'body-9', 'body-10', 'body-11', closed=True)
        self.add_arc('gill-1', (18, 23), (18, 28), radius_x=9, radius_y=9, sweep=True)
        self.add_contour('gill', 'gill-1', closed=False)
