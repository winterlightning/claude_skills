"""Two outlined hands with distinct upper thumbs, cuffs and touching knuckles. One impact dot. Shared contact edge is drawn once; bilateral symmetry.
SQUARE centerline extremes (6,6)-(42,42); stroke 4 on SOLO48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '7eb37a5d-4cd8-4996-8500-94d9331cc88f'
SOURCE_PATH = 'pictographic-primitives/work/workflow teamwork fistbump_7eb37a5d-4cd8-4996-8500-94d9331cc88f.svg'
AUTHOR = 'gpt-6'

class FistBump(Solo48):
    icon_id = 'fist-bump'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/work'
    aliases = ()
    keywords = ('fist', 'bump', 'hands', 'greeting', 'teamwork', 'contact')

    def build(self) -> None:
        self.add_polyline('left-wrist-top', (6, 24), (12, 24), (12, 20), closed=False)
        self.add_arc('left-thumb', (12, 20), (20, 20), radius_x=4, radius_y=4, sweep=True, large_arc=False)
        self.add_line('left-thumb-side', (20, 20), (20, 24))
        self.add_arc('left-top-knuckle', (20, 24), (24, 28), radius_x=4, radius_y=4, sweep=True, large_arc=False)
        self.add_arc('left-lower-knuckle', (24, 36), (20, 40), radius_x=4, radius_y=4, sweep=True, large_arc=False)
        self.add_polyline('left-wrist-bottom', (20, 40), (14, 40), (10, 42), (6, 42), closed=False)
        self.relate("connect", 'left-wrist-top', 'left-thumb')
        self.relate("connect", 'left-thumb', 'left-thumb-side')
        self.relate("connect", 'left-thumb-side', 'left-top-knuckle')
        self.relate("connect", 'left-lower-knuckle', 'left-wrist-bottom')
        self.add_line('left-cuff', (6, 42), (6, 24))
        self.relate("connect", 'left-cuff', 'left-wrist-top')
        self.relate("connect", 'left-cuff', 'left-wrist-bottom')
        self.add_polyline('right-wrist-top', (42, 24), (36, 24), (36, 20), closed=False)
        self.add_arc('right-thumb', (36, 20), (28, 20), radius_x=4, radius_y=4, sweep=False, large_arc=False)
        self.add_line('right-thumb-side', (28, 20), (28, 24))
        self.add_arc('right-top-knuckle', (28, 24), (24, 28), radius_x=4, radius_y=4, sweep=False, large_arc=False)
        self.add_arc('right-lower-knuckle', (24, 36), (28, 40), radius_x=4, radius_y=4, sweep=False, large_arc=False)
        self.add_polyline('right-wrist-bottom', (28, 40), (34, 40), (38, 42), (42, 42), closed=False)
        self.relate("connect", 'right-wrist-top', 'right-thumb')
        self.relate("connect", 'right-thumb', 'right-thumb-side')
        self.relate("connect", 'right-thumb-side', 'right-top-knuckle')
        self.relate("connect", 'right-lower-knuckle', 'right-wrist-bottom')
        self.add_line('right-cuff', (42, 42), (42, 24))
        self.relate("connect", 'right-cuff', 'right-wrist-top')
        self.relate("connect", 'right-cuff', 'right-wrist-bottom')
        self.add_line('knuckle-contact', (24, 28), (24, 36))
        self.relate("connect", 'knuckle-contact', 'left-top-knuckle')
        self.relate("connect", 'knuckle-contact', 'left-lower-knuckle')
        self.relate("connect", 'knuckle-contact', 'right-top-knuckle')
        self.relate("connect", 'knuckle-contact', 'right-lower-knuckle')
        self.relate("connect", 'left-top-knuckle', 'right-top-knuckle')
        self.relate("connect", 'left-lower-knuckle', 'right-lower-knuckle')
        self.add_dot('impact', (24, 6))
