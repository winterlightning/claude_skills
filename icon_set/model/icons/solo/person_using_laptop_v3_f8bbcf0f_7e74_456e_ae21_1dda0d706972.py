"""Side view restored: circular head, seated back, visibly bent arm reaching an open sloping laptop and a continuous keyboard base.
SQUARE centerline extremes (6,6)-(42,42); stroke 4 on SOLO48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'f8bbcf0f-7e74-456e-ae21-1dda0d706972'
SOURCE_PATH = 'pictographic-primitives/work/working remotely_f8bbcf0f-7e74-456e-ae21-1dda0d706972.svg'
AUTHOR = 'gpt-6'

class PersonUsingLaptopVariant3(Solo48):
    icon_id = 'person-using-laptop-v3'
    variant_of = 'person-using-laptop-v2'
    variant_label = 'Recognizable hands, seated laptop user and crowned face'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/work'
    aliases = ()
    keywords = ('person', 'laptop', 'computer', 'remote', 'work', 'seated')

    def build(self) -> None:
        self.add_arc('head-top', (9, 11), (19, 11), radius_x=5, radius_y=5, sweep=True, large_arc=False)
        self.add_arc('head-bottom', (19, 11), (9, 11), radius_x=5, radius_y=5, sweep=True, large_arc=False)
        self.add_contour('head', 'head-top', 'head-bottom', closed=True)
        self.add_arc('shoulder', (6, 34), (14, 26), radius_x=8, radius_y=8, sweep=True, large_arc=False)
        self.add_line('back', (6, 36), (6, 34))
        self.add_arc('seat', (12, 42), (6, 36), radius_x=6, radius_y=6, sweep=True, large_arc=False)
        self.add_line('keyboard-base', (36, 42), (12, 42))
        self.add_contour('body', 'keyboard-base', 'seat', 'back', 'shoulder', closed=False)
        self.add_polyline('bent-arm', (14, 26), (14, 32), (27, 32), closed=False)
        self.relate("connect", 'bent-arm', 'body')
        self.add_polyline('screen', (24, 42), (30, 22), (42, 22), (36, 42), closed=True)
        self.relate("connect", 'screen', 'body')
        self.relate("connect", 'screen', 'bent-arm')
