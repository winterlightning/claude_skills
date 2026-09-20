# Variant of feather-sub32-v2; parent file remains unchanged.
"""Independent 32px profile of feather.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '8ab28f10-44ce-40c6-b0df-2578356c15de'
SOURCE_PATH = 'pictographic-primitives/symbol/feather_8ab28f10-44ce-40c6-b0df-2578356c15de.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('8ab28f10-44ce-40c6-b0df-2578356c15de', 'pictographic-primitives/symbol/feather_8ab28f10-44ce-40c6-b0df-2578356c15de.svg'),)
PROFILE_SOURCE_KEYS = ('solo/feather',)
SOLO_SOURCE_ICON_IDS = ('feather',)
REFERENCE_EXPORT_SHA256 = '306d142b45ce3c96f1e95efb9fa40788b4c3337c6868db586959fae3d43ad148'

class DrawingVariant3(Sub32):
    icon_id = 'feather-sub32-v3'
    variant_of = 'feather-sub32-v2'
    variant_label = 'Redraw proportions and source features'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        # Diagonal vane has a consistent width about the quill; one barb crosses its trailing half.
        self.add_line('left',(6,26),(6,14))
        self.add_line('leading',(6,14),(16,4))
        self.add_bezier('tip-leading',(16,4),((18,2),(20,2),(24,2)))
        self.add_arc('tip',(24,2),(30,8),radius_x=6,radius_y=6,sweep=True)
        self.add_bezier('tip-trailing',(30,8),((30,12),(30,14),(28,16)))
        self.add_line('trailing',(28,16),(18,26))
        self.add_line('base',(18,26),(6,26))
        self.add_contour('vane','left','leading','tip-leading','tip','tip-trailing','trailing','base',closed=True)
        self.add_line('quill',(2,30),(22,10));self.relate('connect','quill','vane')
        self.add_line('barb',(16,16),(28,16));self.relate('connect','barb','quill');self.relate('connect','barb','vane')
