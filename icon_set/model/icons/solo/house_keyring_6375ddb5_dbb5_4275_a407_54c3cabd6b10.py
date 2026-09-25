"""House Keyring. Round-bow key with two teeth joined to a pitched-roof house fob by a curved ring. Omit the tiny fob opening and preserve the physical ring connection; deliberate side-by-side asymmetry.
Keyshape SQUARE, visible extremes (4, 4, 44, 44); centerline envelope inset by 2.
Construction: Lucide key-round: a circular bow and stepped teeth; house: a unified pitched-roof contour. Source establishes the subject and pose.
Shared circles and rounded rectangles keep repeated radii coherent."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6375ddb5-dbb5-4275-a407-54c3cabd6b10'
SOURCE_PATH = 'pictographic-primitives/real-estate/real estate deal key_6375ddb5-dbb5-4275-a407-54c3cabd6b10.svg'
AUTHOR = 'gpt-6'


class HouseKeyring(Solo48):
    icon_id = 'house-keyring'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "real-estate"
    categories = ("real-estate", "primitives")
    aliases = ()
    keywords = ('house', 'keyring')

    def build(self) -> None:
        self.add_arc('bow-ne', (14, 9), (22, 17), radius_x=8, radius_y=8, sweep=True)
        self.add_arc('bow-se', (22, 17), (14, 25), radius_x=8, radius_y=8, sweep=True)
        self.add_arc('bow-sw', (14, 25), (6, 17), radius_x=8, radius_y=8, sweep=True)
        self.add_arc('bow-nw', (6, 17), (14, 9), radius_x=8, radius_y=8, sweep=True)
        self.add_contour('key-bow', 'bow-ne', 'bow-se', 'bow-sw', 'bow-nw', closed=True)
        self.add_line('key-shaft-1', (14, 25), (14, 33))
        self.add_line('key-shaft-2', (14, 33), (14, 41))
        self.add_line('key-shaft-3', (14, 41), (14, 42))
        self.add_contour('key-shaft', 'key-shaft-1', 'key-shaft-2', 'key-shaft-3', closed=False)
        self.relate("connect", 'key-bow', 'key-shaft')
        self.add_line('tooth-0', (14, 33), (20, 33))
        self.relate("connect", 'key-shaft', 'tooth-0')
        self.add_line('tooth-1', (14, 41), (20, 41))
        self.relate("connect", 'key-shaft', 'tooth-1')
        self.add_arc('ring-left', (14, 9), (24, 6), radius_x=10, radius_y=3, sweep=True)
        self.add_arc('ring-right', (24, 6), (35, 17), radius_x=11, radius_y=11, sweep=True)
        self.add_line('ring-stem', (35, 17), (35, 23))
        self.add_contour('ring', 'ring-left', 'ring-right', 'ring-stem', closed=False)
        self.relate("connect", 'key-bow', 'ring')
        self.add_line('house-fob-1', (35, 23), (42, 30))
        self.add_line('house-fob-2', (42, 30), (42, 42))
        self.add_line('house-fob-3', (42, 42), (28, 42))
        self.add_line('house-fob-4', (28, 42), (28, 30))
        self.add_line('house-fob-5', (28, 30), (35, 23))
        self.add_contour('house-fob', 'house-fob-1', 'house-fob-2', 'house-fob-3', 'house-fob-4', 'house-fob-5', closed=True)
        self.relate("connect", 'house-fob', 'ring')
