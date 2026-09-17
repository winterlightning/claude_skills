"""Tape Reels: Two round loops sit side by side and connect through a low horizontal tape segment, with short loose ends projecting downward. Generate this component alone; exclude Rounded Square Frame.

Construction: Two open circular loops join an eight-unit lower tape span and retain their short dangling ends; openings are widened to maintain clearance.
Keyshape: HRECT_S; authored to the SUB32 envelope.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'dfbf1aa7-96fc-485a-9fc2-0731779c283f'
SOURCE_PATH = 'pictographic-primitives/state/record phone_dfbf1aa7-96fc-485a-9fc2-0731779c283f.svg'
AUTHOR = 'gpt-6'


class TapeReels(Sub32):
    icon_id = 'tape-reels'
    keyshape = Keyshape.HRECT_S
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    aliases = ()
    keywords = ('tape', 'reels', 'round', 'loops', 'sit', 'side', 'connect', 'through')

    def build(self):
        self.add_arc('left-loop',(4,19),(12,15),radius_x=5,large_arc=True)
        self.add_line('left-inner',(12,15),(12,22))
        self.add_line('tape',(12,22),(20,22))
        self.add_line('right-inner',(20,22),(20,15))
        self.add_arc('right-loop',(20,15),(28,19),radius_x=5,large_arc=True)
        self.add_contour('reels','left-loop','left-inner','tape','right-inner','right-loop')
        self.add_line('left-end',(4,19),(3,22))
        self.add_line('right-end',(28,19),(29,22))
        self.relate('connect','reels','left-end')
        self.relate('connect','reels','right-end')
