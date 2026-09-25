"""Raised the waves and shortened the lower tail to restore clear separation.

Keyshape SQUARE: visible bounds (4, 4, 44, 44).
Reference: No useful exact match.
"""
# Independent repair of whale-tail; parent preserved.
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '9672a672-8e60-597a-b10e-94e04111186a'
SOURCE_PATH = 'pictographic-primitives/animals/whale tail_9672a672-8e60-597a-b10e-94e04111186a.svg'
AUTHOR = 'gpt-6'

class WhaleTail(Solo48):
    icon_id = 'whale-tail'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'animals'
    aliases = ()
    keywords = ('whale', 'tail', 'fluke', 'water', 'waves', 'sea', 'dive', 'ocean')

    # Symbol plan: retain the subject and shared attachment stations;
    # fit the current keyshape by adjusting the owning cap, base or repeat.
    def build(self) -> None:
        self.add_line('stem-left', (16, 29), (18, 23))
        self.add_arc('fluke-left-bottom', (18, 23), (6, 6), radius_x=26, sweep=True)
        self.add_arc('fluke-left-top', (6, 6), (24, 14), radius_x=28, sweep=False)
        self.add_arc('fluke-right-top', (24, 14), (42, 6), radius_x=28, sweep=False)
        self.add_arc('fluke-right-bottom', (42, 6), (30, 23), radius_x=26, sweep=True)
        self.add_line('stem-right', (30, 23), (32, 29))
        self.add_contour('tail', 'stem-left', 'fluke-left-bottom', 'fluke-left-top', 'fluke-right-top', 'fluke-right-bottom', 'stem-right')
        self.add_arc('wave-left', (6, 38), (16, 38), radius_x=7, radius_y=4, sweep=False)
        self.add_arc('wave-middle', (16, 38), (32, 38), radius_x=8, radius_y=4, sweep=False)
        self.add_arc('wave-right', (32, 38), (42, 38), radius_x=7, radius_y=4, sweep=False)
        self.add_contour('water', 'wave-left', 'wave-middle', 'wave-right')
