from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'a56ae08a-d50a-56ef-a0b7-9f3c918fa436'
SOURCE_PATH = 'pictographic-primitives/animals/sleep helper_a56ae08a-d50a-56ef-a0b7-9f3c918fa436.svg'
AUTHOR = 'gpt-6'

class SheepJumpingFence(Solo48):
    icon_id = 'sheep-jumping-fence'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'nature/animals'
    aliases = ()
    keywords = ('sheep', 'fence', 'jump', 'sleep', 'counting', 'insomnia', 'bedtime', 'rest')

    def build(self) -> None:
        self.add_arc('wool-top', (16, 12), (28, 12), radius_x=6)
        self.add_arc('wool-shoulder', (28, 12), (40, 16), radius_x=8)
        self.add_arc('wool-rump', (40, 16), (34, 22), radius_x=6)
        self.add_arc('wool-base', (34, 22), (22, 22), radius_x=6, radius_y=3)
        self.add_arc('wool-left', (22, 22), (14, 22), radius_x=4, radius_y=3)
        self.add_line('wool-neck', (14, 22), (16, 12))
        self.add_contour('fleece', 'wool-top', 'wool-shoulder', 'wool-rump', 'wool-base', 'wool-left', 'wool-neck', closed=True)
        self.add_line('head-top', (16, 12), (12, 12))
        self.add_arc('muzzle', (12, 12), (12, 22), radius_x=6, radius_y=5, sweep=False)
        self.add_line('jaw', (12, 22), (14, 22))
        self.add_contour('head', 'head-top', 'muzzle', 'jaw')
        self.add_line('front-hoof', (14, 22), (8, 28))
        self.add_line('rear-hoof', (34, 22), (40, 28))
        self.relate('connect', 'head', 'fleece')
        self.relate('connect', 'head', 'front-hoof')
        self.relate('connect', 'fleece', 'front-hoof')
        self.relate('connect', 'fleece', 'rear-hoof')
        for name, x in (('post-left', 16), ('post-right', 32)):
            self.add_polyline(name, (x, 34), (x, 38), (x, 42))
            self.relate('connect', name, 'rail')
        self.add_polyline('rail', (6, 38), (16, 38), (32, 38), (42, 38))
