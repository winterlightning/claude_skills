# Variant of lit-pillar-candle-5f3444ae-892d-4884-834e-0ac133b299e6-sub32-v2; parent file remains unchanged.
"""Independent 32px profile of lit-pillar-candle-5f3444ae-892d-4884-834e-0ac133b299e6.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '5f3444ae-892d-4884-834e-0ac133b299e6'
SOURCE_PATH = 'pictographic-primitives/lights/candle_5f3444ae-892d-4884-834e-0ac133b299e6.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('5f3444ae-892d-4884-834e-0ac133b299e6', 'pictographic-primitives/lights/candle_5f3444ae-892d-4884-834e-0ac133b299e6.svg'),)
PROFILE_SOURCE_KEYS = ('solo/lit-pillar-candle-5f3444ae-892d-4884-834e-0ac133b299e6',)
SOLO_SOURCE_ICON_IDS = ('lit-pillar-candle-5f3444ae-892d-4884-834e-0ac133b299e6',)
REFERENCE_EXPORT_SHA256 = 'a7c0c4d42ff463a01d521cd8753d73961b3e01b37343f118311c023e902946d7'

class DrawingVariant3(Sub32):
    icon_id = 'lit-pillar-candle-5f3444ae-892d-4884-834e-0ac133b299e6-sub32-v3'
    variant_label = 'Redraw proportions and source features'
    keyshape = Keyshape.VRECT_M
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'lights'
    categories = ('lights', 'primitives')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        # Tall candle body and centered flame, with a continuous wick and a closed base.
        self.add_bezier('flame-left',(16,2),((14,5),(12,6),(12,9)))
        self.add_bezier('flame-base',(12,9),((12,13),(20,13),(20,9)))
        self.add_bezier('flame-right',(20,9),((20,6),(18,5),(16,2)))
        self.add_contour('flame','flame-left','flame-base','flame-right',closed=True)
        self.add_line('wick',(16,12),(16,18))
        self.relate('connect','wick','flame-base')
        self.add_polyline('wax',(8,18),(24,18),(24,30),(8,30),closed=True)
        self.relate('connect','wick','wax-1')
        self.relate('connect','flame','wick')
