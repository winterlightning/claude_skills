"""A distressed infant face with crossed eyes, frown and three crown rays. Shoulders are omitted to preserve readable expression."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '828eb5e9-1438-5b90-b595-556e440421af'
SOURCE_PATH = 'pictographic-primitives/babies/colic baby_828eb5e9-1438-5b90-b595-556e440421af.svg'
AUTHOR = 'gpt-6'


class DistressedBabyFace(Solo48):
    icon_id = 'distressed-baby-face'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "people/babies"
    aliases = ()
    keywords = ('distressed', 'baby', 'face', 'infant', 'nursery')

    def build(self) -> None:
        # Centerline extremes: (2,2)-(46,46).
        self.add_arc('crown', (8, 25), (40, 25), radius_x=16, radius_y=13, sweep=True, large_arc=False)
        self.add_arc('ear-right', (40, 25), (40, 33), radius_x=6, radius_y=4, sweep=True, large_arc=False)
        self.add_arc('jaw', (40, 33), (8, 33), radius_x=16, radius_y=13, sweep=True, large_arc=False)
        self.add_arc('ear-left', (8, 33), (8, 25), radius_x=6, radius_y=4, sweep=True, large_arc=False)
        self.add_contour('face', 'crown', 'ear-right', 'jaw', 'ear-left', closed=True)
        self.add_line('eye-left-down', (15, 25), (19, 29))
        self.add_line('eye-left-up', (15, 29), (19, 25))
        self.relate("connect", 'eye-left-down', 'eye-left-up')
        self.add_line('eye-right-down', (29, 25), (33, 29))
        self.add_line('eye-right-up', (29, 29), (33, 25))
        self.relate("connect", 'eye-right-down', 'eye-right-up')
        self.add_arc('frown', (20, 38), (28, 38), radius_x=5, radius_y=3, sweep=True, large_arc=False)
        self.add_line('ray-middle', (24, 2), (24, 5))
        self.add_line('ray-left', (10, 4), (12, 7))
        self.add_line('ray-right', (38, 4), (36, 7))
