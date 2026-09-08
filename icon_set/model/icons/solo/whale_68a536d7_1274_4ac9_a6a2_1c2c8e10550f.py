"""Front-facing round whale with eyes, side flippers, bowed mouth and paired throat pleats.

SQUARE centerline extremes (2,2)-(46,46), mirrored around x=24.
The supplied whale informs the broad head, forked spout and curved belly bands.
Eyes and side flippers address the user’s recognizability feedback.
No useful local Lucide whale match; smooth elliptical quarters carry the body.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '68a536d7-1274-4ac9-a6a2-1c2c8e10550f'
SOURCE_PATH = 'pictographic-primitives/animals/whale_68a536d7-1274-4ac9-a6a2-1c2c8e10550f.svg'
AUTHOR = 'gpt-6'


class RoundWhale(Solo48):
    icon_id = 'round-whale'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'nature/animals'
    aliases = ()
    keywords = ('whale', 'round', 'spout', 'sea', 'ocean', 'marine', 'cute', 'mammal')

    def build(self) -> None:
        self.add_arc('back-left', (6,30), (24,14), radius_x=18, radius_y=16)
        self.add_arc('back-right', (24,14), (42,30), radius_x=18, radius_y=16)
        self.add_arc('belly-right', (42,30), (32,46), radius_x=10, radius_y=16)
        self.add_line('base-right', (32,46), (28,46))
        self.add_line('base-middle', (28,46), (20,46))
        self.add_line('base-left', (20,46), (16,46))
        self.add_arc('belly-left', (16,46), (6,30), radius_x=10, radius_y=16)
        self.add_contour('body', 'back-left', 'back-right', 'belly-right', 'base-right', 'base-middle', 'base-left', 'belly-left', closed=True)
        self.add_arc('mouth-left', (6,30), (16,34), radius_x=10, radius_y=4, sweep=False)
        self.add_line('mouth-center', (16,34), (32,34))
        self.add_arc('mouth-right', (32,34), (42,30), radius_x=10, radius_y=4, sweep=False)
        self.add_contour('mouth', 'mouth-left', 'mouth-center', 'mouth-right')
        self.relate('connect', 'mouth', 'body')
        self.add_arc('flipper-left', (6,30), (2,38), radius_x=4, radius_y=8, sweep=False)
        self.add_arc('flipper-right', (42,30), (46,38), radius_x=4, radius_y=8)
        self.relate('connect', 'flipper-left', 'body')
        self.relate('connect', 'flipper-right', 'body')
        self.relate('connect', 'flipper-left', 'mouth')
        self.relate('connect', 'flipper-right', 'mouth')
        self.add_dot('eye-left', (16,24))
        self.add_dot('eye-right', (32,24))
        self.add_arc('pleat-left', (16,34), (20,46), radius_x=4, radius_y=12, sweep=False)
        self.add_arc('pleat-right', (32,34), (28,46), radius_x=4, radius_y=12)
        for pleat in ('pleat-left', 'pleat-right'):
            self.relate('connect', pleat, 'mouth')
            self.relate('connect', pleat, 'body')
        self.add_line('spout-stem', (24,14), (24,10))
        self.relate('connect', 'spout-stem', 'body')
        self.add_arc('spout-left', (24,10), (16,2), radius_x=8, sweep=False)
        self.add_arc('spout-right', (24,10), (32,2), radius_x=8)
        self.relate('connect', 'spout-left', 'spout-stem')
        self.relate('connect', 'spout-right', 'spout-stem')
        self.relate('connect', 'spout-left', 'spout-right')
