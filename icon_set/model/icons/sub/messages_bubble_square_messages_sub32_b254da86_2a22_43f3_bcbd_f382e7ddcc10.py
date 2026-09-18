"""Independent 32px profile of messages-bubble-square-messages.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'b254da86-2a22-43f3-bcbd-f382e7ddcc10'
SOURCE_PATH = 'pictographic-primitives/messages/messages bubble square_b254da86-2a22-43f3-bcbd-f382e7ddcc10.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('b254da86-2a22-43f3-bcbd-f382e7ddcc10', 'pictographic-primitives/messages/messages bubble square_b254da86-2a22-43f3-bcbd-f382e7ddcc10.svg'),)
PROFILE_SOURCE_KEYS = ('solo/messages-bubble-square-messages',)
SOLO_SOURCE_ICON_IDS = ('messages-bubble-square-messages',)
REFERENCE_EXPORT_SHA256 = '619ee934de1dd5db9b17853baea4c093357dad48f5ba978a9e481ac77d5c4a08'

class Drawing(Sub32):
    icon_id = 'messages-bubble-square-messages-sub32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'messages'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (10, 22), (2, 22))
        self.add_line('p1-r1-2', (2, 22), (2, 5))
        self.add_line('p1-r1-3', (2, 5), (30, 5))
        self.add_line('p1-r1-4', (30, 5), (30, 22))
        self.add_line('p1-r1-5', (30, 22), (16, 22))
        self.add_line('p1-r1-6', (16, 22), (15, 23))
        self.add_line('p1-r1-7', (15, 23), (10, 27))
        self.add_line('p1-r1-8', (10, 27), (10, 22))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', closed=False)
