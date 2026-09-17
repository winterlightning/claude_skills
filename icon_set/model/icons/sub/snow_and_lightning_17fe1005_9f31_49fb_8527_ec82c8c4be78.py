"""Snow and Lightning: An open lightning zigzag stands between scattered short upright snow marks. The bolt descends diagonally through the centre, while the small marks form loose columns on either side.

Construction: One central zigzag and a sparse paired series of snow dots; separate marks preserve clearance.
Keyshape: SQUARE; the four extrema follow the SUB32 contract.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '17fe1005-9f31-49fb-8527-ec82c8c4be78'
SOURCE_PATH = 'pictographic-primitives/state/snow thunder_17fe1005-9f31-49fb-8527-ec82c8c4be78.svg'
AUTHOR = 'gpt-6'


class SnowAndLightning(Sub32):
    icon_id = 'snow-and-lightning'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    aliases = ()
    keywords = ('snow', 'lightning', 'open', 'zigzag', 'stands', 'between', 'scattered', 'short')

    def build(self):
        self.add_polyline("bolt",(22,2),(10,16),(22,16),(10,30))
        for x in (2,30):
            for y in (8,24):self.add_dot(f"snow-{x}-{y}",(x,y))
