"""A horizontal rating row of three five-point stars.
Symbol plan and construction: star: alternating tips and valleys from one repeated definition.
Keyshape: CIRCLE provides a radial envelope while retaining the horizontal three-star arrangement.
Omissions: None; all three equal five-point stars retained.
Review: Blocked: adjacent stars are 2 units apart and several interior bands require review. Enlarged counters, staggered positions, joined tips and rectangular envelopes were tried. Narrow diamond-like candidates were visually rejected."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='cf0d9970-8b38-5723-b109-a3be9696acdb'
SOURCE_PATH = 'pictographic-primitives/rating/rating star three_cf0d9970-8b38-5723-b109-a3be9696acdb.svg'
AUTHOR="gpt-6"

class Drawing(Solo48):
    icon_id='rating-star-three'
    keyshape=Keyshape.CIRCLE
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects/general"
    aliases=()
    keywords=('rating', 'star', 'three')
    def build(self):
        # Three equal five-point stars; retain their horizontal rating arrangement.
        for i,x in enumerate((10,24,38)):
         self.add_polyline(f'star-{i}',(x,16),(x+2,22),(x+6,24),(x+3,27),(x+4,32),(x,29),(x-4,32),(x-3,27),(x-6,24),(x-2,22),closed=True)
