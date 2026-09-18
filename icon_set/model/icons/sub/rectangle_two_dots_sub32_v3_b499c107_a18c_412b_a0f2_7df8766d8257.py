# Variant of rectangle-two-dots-sub32-v2; parent file remains unchanged.
"""Independent 32px profile of rectangle-two-dots.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = 'b499c107-a18c-412b-a0f2-7df8766d8257'
SOURCE_PATH = 'pictographic-primitives/state/rectangle two dots_b499c107-a18c-412b-a0f2-7df8766d8257.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('b499c107-a18c-412b-a0f2-7df8766d8257', 'pictographic-primitives/state/rectangle two dots_b499c107-a18c-412b-a0f2-7df8766d8257.svg'),)
PROFILE_SOURCE_KEYS = ('solo/rectangle-two-dots',)
SOLO_SOURCE_ICON_IDS = ('rectangle-two-dots',)
REFERENCE_EXPORT_SHA256 = '2c7636d3ef9d193664f845cbb32204d9b75605a28e17bd34ee7683e4c74bdb0b'

class DrawingVariant3(Sub32):
    icon_id = 'rectangle-two-dots-sub32-v3'
    variant_of = 'rectangle-two-dots-sub32-v2'
    variant_label = 'Redraw proportions and source features'
    keyshape = Keyshape.VRECT_M
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'state'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        # Tall rounded panel with two evenly spaced dots and balanced internal margins.
        self.add_line('top',(12,2),(20,2))
        self.add_arc('tr',(20,2),(24,6),radius_x=4,radius_y=4,sweep=True)
        self.add_line('right',(24,6),(24,26))
        self.add_arc('br',(24,26),(20,30),radius_x=4,radius_y=4,sweep=True)
        self.add_line('base',(20,30),(12,30))
        self.add_arc('bl',(12,30),(8,26),radius_x=4,radius_y=4,sweep=True)
        self.add_line('left',(8,26),(8,6))
        self.add_arc('tl',(8,6),(12,2),radius_x=4,radius_y=4,sweep=True)
        self.add_contour('frame','top','tr','right','br','base','bl','left','tl',closed=True)
        for y in [11,21]:self.add_dot('dot-'+str(y),(16,y))
