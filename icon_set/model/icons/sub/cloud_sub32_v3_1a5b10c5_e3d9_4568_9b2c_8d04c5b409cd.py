# Variant of cloud-sub32-v2; parent file remains unchanged.
"""Independent 32px profile of cloud.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '1a5b10c5-e3d9-4568-9b2c-8d04c5b409cd'
SOURCE_PATH = 'pictographic-primitives/internet/cloud_1a5b10c5-e3d9-4568-9b2c-8d04c5b409cd.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('1a5b10c5-e3d9-4568-9b2c-8d04c5b409cd', 'pictographic-primitives/internet/cloud_1a5b10c5-e3d9-4568-9b2c-8d04c5b409cd.svg'),)
PROFILE_SOURCE_KEYS = ('solo/cloud',)
SOLO_SOURCE_ICON_IDS = ('cloud',)
REFERENCE_EXPORT_SHA256 = '92d6f7aa5f112153455bbef090004fb08fac8d48ea6f7685b095906911cde5f6'

class DrawingVariant3(Sub32):
    icon_id = 'cloud-sub32-v3'
    variant_of = 'cloud-sub32-v2'
    variant_label = 'Redraw proportions and source features'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'internet'
    categories = ('internet', 'other', 'primitives-generate')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        # Low cloud silhouette: broad base, central rounded dome and compact shoulders.
        self.add_arc('top',(8,14),(24,14),radius_x=8,radius_y=8,sweep=True)
        self.add_bezier('shoulder-right',(24,14),((28,14),(30,16),(30,20)))
        self.add_bezier('lower-right',(30,20),((30,24),(28,26),(24,26)))
        self.add_line('base',(24,26),(8,26))
        self.add_bezier('lower-left',(8,26),((4,26),(2,24),(2,20)))
        self.add_bezier('shoulder-left',(2,20),((2,16),(4,14),(8,14)))
        self.add_contour('cloud','top','shoulder-right','lower-right','base','lower-left','shoulder-left',closed=True)
