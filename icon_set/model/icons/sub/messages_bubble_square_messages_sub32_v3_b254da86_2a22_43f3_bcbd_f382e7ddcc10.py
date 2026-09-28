# Variant of messages-bubble-square-messages-sub32-v2; parent file remains unchanged.
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

class DrawingVariant3(Sub32):
    icon_id = 'messages-bubble-square-messages-sub32-v3'
    variant_of = 'messages-bubble-square-messages-sub32-v2'
    variant_label = 'Redraw proportions and source features'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'messages'
    categories = ('messages', 'state', 'other', 'primitives-generate')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        # Rounded speech bubble with a deliberate tail and uniform corner radii.
        self.add_line('top',(6,6),(26,6))
        self.add_arc('tr',(26,6),(30,10),radius_x=4,radius_y=4,sweep=True)
        self.add_line('right',(30,10),(30,19))
        self.add_arc('br',(30,19),(26,23),radius_x=4,radius_y=4,sweep=True)
        self.add_line('base',(26,23),(15,23))
        self.add_line('tail-in',(15,23),(10,26))
        self.add_line('tail-out',(10,26),(10,23))
        self.add_line('left-base',(10,23),(6,23))
        self.add_arc('bl',(6,23),(2,19),radius_x=4,radius_y=4,sweep=True)
        self.add_line('left',(2,19),(2,10))
        self.add_arc('tl',(2,10),(6,6),radius_x=4,radius_y=4,sweep=True)
        self.add_contour('bubble','top','tr','right','br','base','tail-in','tail-out','left-base','bl','left','tl',closed=True)
