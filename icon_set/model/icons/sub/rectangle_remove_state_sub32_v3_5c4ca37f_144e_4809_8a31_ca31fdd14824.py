# Variant of rectangle-remove-state-sub32-v2; parent file remains unchanged.
"""Independent 32px profile of rectangle-remove-state.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '5c4ca37f-144e-4809-8a31-ca31fdd14824'
SOURCE_PATH = 'pictographic-primitives/state/rectangle remove_5c4ca37f-144e-4809-8a31-ca31fdd14824.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('5c4ca37f-144e-4809-8a31-ca31fdd14824', 'pictographic-primitives/state/rectangle remove_5c4ca37f-144e-4809-8a31-ca31fdd14824.svg'),)
PROFILE_SOURCE_KEYS = ('solo/rectangle-remove-state',)
SOLO_SOURCE_ICON_IDS = ('rectangle-remove-state',)
REFERENCE_EXPORT_SHA256 = '03be80878aacbac0addaceb08ddf4b9f23023dd16de4aa2ddceb5bf462c5feb4'

class DrawingVariant3(Sub32):
    icon_id = 'rectangle-remove-state-sub32-v3'
    variant_of = 'rectangle-remove-state-sub32-v2'
    variant_label = 'Redraw proportions and source features'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'state'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        # Restore the source’s crossed remove mark within a wide rounded rectangle.
        self.add_line('top',(5,6),(27,6))
        self.add_arc('tr',(27,6),(30,9),radius_x=3,radius_y=3,sweep=True)
        self.add_line('right',(30,9),(30,23))
        self.add_arc('br',(30,23),(27,26),radius_x=3,radius_y=3,sweep=True)
        self.add_line('base',(27,26),(5,26))
        self.add_arc('bl',(5,26),(2,23),radius_x=3,radius_y=3,sweep=True)
        self.add_line('left',(2,23),(2,9))
        self.add_arc('tl',(2,9),(5,6),radius_x=3,radius_y=3,sweep=True)
        self.add_contour('frame','top','tr','right','br','base','bl','left','tl',closed=True)
        self.add_line('cross-a',(13,13),(19,19));self.add_line('cross-b',(19,13),(13,19));self.relate('connect','cross-a','cross-b')
