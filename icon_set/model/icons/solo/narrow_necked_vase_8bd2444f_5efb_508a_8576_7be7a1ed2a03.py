"""Shortened the lip and moved the rounded belly base upward.

Keyshape VRECT_L: visible bounds (6, 2, 42, 46).
Reference: amphora: paired neck-to-belly flow; no handles added.
"""
# Independent repair of narrow-necked-vase; parent preserved.
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '8bd2444f-5efb-508a-8576-7be7a1ed2a03'
SOURCE_PATH = 'pictographic-primitives/culture/batch-05/vase_8bd2444f-5efb-508a-8576-7be7a1ed2a03.svg'
AUTHOR = 'gpt-6'

class NarrowNeckedVase(Solo48):
    icon_id = 'narrow-necked-vase'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'culture'
    aliases = ()
    keywords = ('vase', 'pottery', 'ceramic', 'vessel', 'decorative', 'flowers', 'antique', 'urn')

    # Symbol plan: retain the subject and shared attachment stations;
    # fit the current keyshape by adjusting the owning cap, base or repeat.
    def build(self) -> None:
        self.add_line('lip', (16, 4), (32, 4))
        self.add_line('neck-right', (32, 4), (32, 10))
        self.add_arc('flare-right', (32, 10), (36, 20), radius_x=14, sweep=False)
        self.add_arc('belly-upper-right', (36, 20), (40, 30), radius_x=20)
        self.add_arc('base-right', (40, 30), (26, 44), radius_x=14)
        self.add_line('base', (26, 44), (22, 44))
        self.add_arc('base-left', (22, 44), (8, 30), radius_x=14)
        self.add_arc('belly-upper-left', (8, 30), (12, 20), radius_x=20)
        self.add_arc('flare-left', (12, 20), (16, 10), radius_x=14, sweep=False)
        self.add_line('neck-left', (16, 10), (16, 4))
        self.add_contour('vase', 'lip', 'neck-right', 'flare-right', 'belly-upper-right', 'base-right', 'base', 'base-left', 'belly-upper-left', 'flare-left', 'neck-left', closed=True)
