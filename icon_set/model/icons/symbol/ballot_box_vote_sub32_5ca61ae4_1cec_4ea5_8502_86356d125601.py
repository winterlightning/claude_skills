"""Independent 32px profile of ballot-box-vote.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '5ca61ae4-1cec-4ea5-8502-86356d125601'
SOURCE_PATH = 'pictographic-primitives/symbol/vote_5ca61ae4-1cec-4ea5-8502-86356d125601.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('5ca61ae4-1cec-4ea5-8502-86356d125601', 'pictographic-primitives/symbol/vote_5ca61ae4-1cec-4ea5-8502-86356d125601.svg'),)
PROFILE_SOURCE_KEYS = ('solo/ballot-box-vote',)
SOLO_SOURCE_ICON_IDS = ('ballot-box-vote',)
REFERENCE_EXPORT_SHA256 = 'f4d5e87bf994f050bef45b64599843665a0fe8cd9411e480894554f21094f3ad'

class Drawing(Sub32):
    icon_id = 'ballot-box-vote-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    categories = ('symbol', 'state')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (8, 2), (24, 2))
        self.add_line('p1-r1-2', (24, 2), (19, 10))
        self.add_line('p1-r1-3', (19, 10), (13, 10))
        self.add_line('p1-r1-4', (13, 10), (8, 2))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=False)
        self.add_line('p2-r1-1', (7, 18), (25, 18))
        self.add_arc('p2-r1-2', (25, 18), (30, 22), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_line('p2-r1-3', (30, 22), (30, 25))
        self.add_arc('p2-r1-4', (30, 25), (25, 30), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_line('p2-r1-5', (25, 30), (7, 30))
        self.add_arc('p2-r1-6', (7, 30), (2, 25), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_line('p2-r1-7', (2, 25), (2, 22))
        self.add_arc('p2-r1-8', (2, 22), (7, 18), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', 'p2-r1-6', 'p2-r1-7', 'p2-r1-8', closed=False)
