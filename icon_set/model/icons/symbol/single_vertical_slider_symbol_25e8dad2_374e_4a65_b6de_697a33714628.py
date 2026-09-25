"""A single vertical slider: a round knob at the bottom of one short upright stem. Exclude the enclosing upright rectangle and do not replace it with multiple horizontal sliders.

Plan: Circular knob and centered attached stem. Bounds (8,2)-(24,30).
Construction reference: No close Lucide subject; use simple connected contours."""
from ...keyshapes import Keyshape
from ._base import Symbol32

SOURCE_ICON_ID = '25e8dad2-374e-4a65-b6de-697a33714628'
SOURCE_PATH = 'pictographic-primitives/other/rectangle uv low_25e8dad2-374e-4a65-b6de-697a33714628.svg'
SOURCE_ICON_IDS = ('25e8dad2-374e-4a65-b6de-697a33714628',)
AUTHOR = 'gpt-6'

class SingleVerticalSliderSymbol(Symbol32):
    icon_id = 'single-vertical-slider-symbol'
    keyshape = Keyshape.VRECT_M
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives-generate'
    categories = ('other', 'primitives-generate')
    aliases = ()
    keywords = ('single', 'vertical', 'slider', 'symbol')

    def build(self) -> None:
        self.add_arc('knob-a',(16,14),(16,30),radius_x=8)
        self.add_arc('knob-b',(16,30),(16,14),radius_x=8)
        self.add_contour('knob','knob-a','knob-b',closed=True)
        self.add_line('stem',(16,2),(16,14))
        self.relate('connect','knob','stem')
