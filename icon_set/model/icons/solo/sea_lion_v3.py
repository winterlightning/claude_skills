# Review revision; previous candidates preserved.
"""sea-lion: HRECT_XL ink (6,6)-(42,42). Left-facing raised head, sweeping back and splayed flippers."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '7188aa8a-305f-404d-bfe3-07ee8f265206'
SOURCE_PATH = 'pictographic-primitives/animals/seal body_7188aa8a-305f-404d-bfe3-07ee8f265206.svg'
AUTHOR = 'gpt-6'

class SeaLionVariant3(Solo48):
    icon_id = 'sea-lion-v3'
    variant_of = 'sea-lion-v2'
    variant_label = 'Review revision: clear geometry and spacing'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'animals/marine'
    aliases = ()
    keywords = ('sea lion', 'seal', 'flippers', 'marine', 'animal', 'ocean', 'zoo', 'whiskers')

    def build(self) -> None:
        self.add_arc('head-back', (16, 6), (28, 16), radius_x=12, radius_y=10)
        self.add_line('neck-back', (28, 16), (28, 22))
        self.add_line('back-start', (28, 22), (30, 22))
        self.add_arc('back', (30, 22), (42, 34), radius_x=12)
        self.add_line('rear-edge', (42, 34), (42, 38))
        self.add_arc('rear-tip', (42, 38), (38, 42), radius_x=4)
        self.add_line('rear-base', (38, 42), (34, 42))
        self.add_line('rear-inner', (34, 42), (36, 34))
        self.add_line('rear-join', (36, 34), (30, 32))
        self.add_arc('belly', (30, 32), (24, 34), radius_x=12, radius_y=6)
        self.add_line('front-flipper', (24, 34), (28, 42))
        self.add_arc('front-flipper-base', (28, 42), (16, 38), radius_x=12, radius_y=4)
        self.add_line('chest-base', (16, 38), (10, 40))
        self.add_line('front-foot', (10, 40), (6, 38))
        self.add_line('chest-lower', (6, 38), (10, 30))
        self.add_arc('chest-upper', (10, 30), (8, 24), radius_x=14)
        self.add_line('jaw', (8, 24), (6, 18))
        self.add_line('mouth-lower', (6, 18), (10, 16))
        self.add_line('mouth-upper', (10, 16), (6, 14))
        self.add_arc('forehead', (6, 14), (16, 6), radius_x=10, radius_y=8)
        self.add_contour('body', 'head-back', 'neck-back', 'back-start', 'back', 'rear-edge', 'rear-tip', 'rear-base', 'rear-inner', 'rear-join', 'belly', 'front-flipper', 'front-flipper-base', 'chest-base', 'front-foot', 'chest-lower', 'chest-upper', 'jaw', 'mouth-lower', 'mouth-upper', 'forehead', closed=True)
        self.add_line('flipper-mark', (16, 30), (16, 38))
        self.relate('connect', 'flipper-mark', 'body')
        self.add_dot('eye', (19, 15))
