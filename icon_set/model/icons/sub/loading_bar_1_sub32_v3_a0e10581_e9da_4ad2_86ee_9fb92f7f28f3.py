# Variant of loading-bar-1-sub32-v2; parent file remains unchanged.
"""Independent 32px profile of loading-bar-1.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = 'a0e10581-e9da-4ad2-86ee-9fb92f7f28f3'
SOURCE_PATH = 'pictographic-primitives/interface-essential/loading bar 1_a0e10581-e9da-4ad2-86ee-9fb92f7f28f3.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('a0e10581-e9da-4ad2-86ee-9fb92f7f28f3', 'pictographic-primitives/interface-essential/loading bar 1_a0e10581-e9da-4ad2-86ee-9fb92f7f28f3.svg'),)
PROFILE_SOURCE_KEYS = ('solo/loading-bar-1',)
SOLO_SOURCE_ICON_IDS = ('loading-bar-1',)
REFERENCE_EXPORT_SHA256 = 'fcfe06951f6fb5a902e6d72293d5967d601599f5ae411ce8a35ce3fe8c4eca69'

class DrawingVariant3(Sub32):
    icon_id = 'loading-bar-1-sub32-v3'
    variant_of = 'loading-bar-1-sub32-v2'
    variant_label = 'Redraw proportions and source features'
    keyshape = Keyshape.HRECT_S
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'interface-essential'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        # True horizontal capsule with equally spaced diagonal bands; no bulging vertical oval ends.
        self.add_line('top',(8,10),(24,10))
        self.add_arc('right',(24,10),(24,22),radius_x=6,radius_y=6,sweep=True)
        self.add_line('bottom',(24,22),(8,22))
        self.add_arc('left',(8,22),(8,10),radius_x=6,radius_y=6,sweep=True)
        self.add_contour('capsule','top','right','bottom','left',closed=True)
        for i,x in enumerate([8,18]):
         uid=f'band-{i}';self.add_line(uid,(x,22),(x+6,10))
         self.relate('connect',uid,'top');self.relate('connect',uid,'bottom')
        self.relate('connect','band-0','left');self.relate('connect','band-1','right')
