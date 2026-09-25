"""Front-facing round whale with eyes, side flippers, bowed mouth and paired throat pleats.

SQUARE centerline extremes (6,6)-(42,42), mirrored around x=24.
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
    category = 'animals'
    aliases = ()
    keywords = ('whale', 'round', 'spout', 'sea', 'ocean', 'marine', 'cute', 'mammal')

    def build(self) -> None:
        # Symbol plan: preserve the subject, contour topology and curve types.
        # Rebalance whole parts on the SOLO48 integer grid; keep real shared contacts.
        self.add_arc('back-left', (6, 30), (24, 14), radius_x=18, radius_y=16, large_arc=False, sweep=True)
        self.add_arc('back-right', (24, 14), (42, 30), radius_x=18, radius_y=16, large_arc=False, sweep=True)
        self.add_bezier('belly-right', (42, 30), *(((40.83233961, 37.25119915), (36.6776644, 42), (32, 42)),))
        self.add_line('base-right', (32, 42), (28, 42))
        self.add_line('base-middle', (28, 42), (20, 42))
        self.add_line('base-left', (20, 42), (16, 42))
        self.add_bezier('belly-left', (16, 42), *(((11.3223356, 42), (7.16766039, 37.25119915), (6, 30)),))
        self.add_arc('mouth-left', (6, 30), (16, 34), radius_x=10, radius_y=4, large_arc=False, sweep=False)
        self.add_line('mouth-center', (16, 34), (32, 34))
        self.add_arc('mouth-right', (32, 34), (42, 30), radius_x=10, radius_y=4, large_arc=False, sweep=False)
        self.add_bezier('flipper-left', (6, 30), *(((6, 32.47520861), (6, 35.52479139), (6, 38)),))
        self.add_bezier('flipper-right', (42, 30), *(((42, 32.47520861), (42, 35.52479139), (42, 38)),))
        self.add_line('eye-left', (17, 25), (17, 25))
        self.add_line('eye-right', (31, 25), (31, 25))
        self.add_bezier('pleat-left', (16, 34), *(((16.59087761, 39.04103628), (18.2216513, 42), (20, 42)),))
        self.add_bezier('pleat-right', (32, 34), *(((31.40912239, 39.04103628), (29.7783487, 42), (28, 42)),))
        self.add_line('spout-stem', (24, 14), (24, 10))
        self.add_bezier('spout-left', (24, 10), *(((22.39737339, 7.16125546), (19.2325716, 6), (16, 6)),))
        self.add_bezier('spout-right', (24, 10), *(((25.60262661, 7.16125546), (28.7674284, 6), (32, 6)),))
        self.add_contour('body', *('back-left', 'back-right', 'belly-right', 'base-right', 'base-middle', 'base-left', 'belly-left'), closed=True)
        self.add_contour('mouth', *('mouth-left', 'mouth-center', 'mouth-right'), closed=False)
        self.relate('connect', *('mouth', 'body'))
        self.relate('connect', *('flipper-left', 'body'))
        self.relate('connect', *('flipper-right', 'body'))
        self.relate('connect', *('flipper-left', 'mouth'))
        self.relate('connect', *('flipper-right', 'mouth'))
        self.relate('connect', *('pleat-left', 'mouth'))
        self.relate('connect', *('pleat-left', 'body'))
        self.relate('connect', *('pleat-right', 'mouth'))
        self.relate('connect', *('pleat-right', 'body'))
        self.relate('connect', *('spout-stem', 'body'))
        self.relate('connect', *('spout-left', 'spout-stem'))
        self.relate('connect', *('spout-right', 'spout-stem'))
        self.relate('connect', *('spout-left', 'spout-right'))
