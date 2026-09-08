from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a56ae08a-d50a-56ef-a0b7-9f3c918fa436'
SOURCE_PATH = 'pictographic-primitives/animals/sleep helper_a56ae08a-d50a-56ef-a0b7-9f3c918fa436.svg'
AUTHOR = 'gpt-6'


class SheepJumpingFence(Solo48):
    icon_id = 'sheep-jumping-fence'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "nature/animals"
    aliases = ()
    keywords = ('sheep', 'fence', 'jump', 'sleep', 'counting', 'insomnia', 'bedtime', 'rest')

    def build(self) -> None:
        # Airborne fleece above a two-post fence; extremes (2,2)-(46,46).
        self.add_arc('wool-top', (16, 8), (28, 8), radius_x=6, radius_y=6, sweep=True)
        self.add_arc('wool-shoulder', (28, 8), (40, 14), radius_x=8, radius_y=8, sweep=True)
        self.add_arc('wool-rump', (40, 14), (34, 26), radius_x=8, radius_y=8, sweep=True)
        self.add_arc('wool-base', (34, 26), (22, 26), radius_x=6, radius_y=5, sweep=True)
        self.add_arc('wool-left', (22, 26), (14, 20), radius_x=7, radius_y=7, sweep=True)
        self.add_line('wool-neck', (14, 20), (16, 8))
        self.add_contour('fleece', 'wool-top', 'wool-shoulder', 'wool-rump', 'wool-base', 'wool-left', 'wool-neck', closed=True)
        self.add_line('head-top', (16, 8), (8, 8))
        self.add_arc('muzzle', (8, 8), (8, 20), radius_x=6, radius_y=6, sweep=False)
        self.add_line('jaw', (8, 20), (14, 20))
        self.add_contour('head', 'head-top', 'muzzle', 'jaw', closed=False)
        self.add_line('front-hoof', (14, 20), (8, 27))
        self.add_line('rear-hoof', (34, 26), (40, 31))
        self.add_line('post-l', (18, 36), (18, 46))
        self.add_line('post-r', (32, 38), (32, 46))
        self.add_line('rail', (18, 38), (32, 41))
        self.add_line('ground-l', (2, 46), (18, 46))
        self.add_line('ground-mid', (18, 46), (32, 46))
        self.add_line('ground-r', (32, 46), (46, 46))
        self.relate("connect", 'fleece', 'head')
        self.relate("connect", 'fleece', 'front-hoof')
        self.relate("connect", 'fleece', 'rear-hoof')
        self.relate("connect", 'head', 'front-hoof')
        self.relate("connect", 'post-l', 'ground-l')
        self.relate("connect", 'post-l', 'ground-mid')
        self.relate("connect", 'post-r', 'ground-mid')
        self.relate("connect", 'post-r', 'ground-r')
        self.relate("connect", 'ground-l', 'ground-mid')
        self.relate("connect", 'ground-mid', 'ground-r')
