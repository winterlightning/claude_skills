"""Three Arrows Down: Three straight arrows point downward, with the central arrow positioned lower than the two outer arrows. Each has a long upright shaft and an open V-shaped head.

Construction: Three equal downward arrow units; the central unit is translated lower.
Keyshape: SQUARE; the four extrema follow the SUB32 contract.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '4fe44175-fb41-4dbd-a349-bde8c4354a91'
SOURCE_PATH = 'pictographic-primitives/state/three arrows down_4fe44175-fb41-4dbd-a349-bde8c4354a91.svg'
AUTHOR = 'gpt-6'


class ThreeArrowsDownSub(Sub32):
    icon_id = 'three-arrows-down-sub'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    aliases = ()
    keywords = ('arrows', 'down', 'straight', 'point', 'downward', 'central', 'arrow', 'positioned')

    def build(self):
        for i,(x,y) in enumerate(((6,2),(16,18),(26,2))):
            self.add_line(f"shaft-{i}",(x,y),(x,y+12))
            self.add_polyline(f"head-{i}",(x-4,y+8),(x,y+12),(x+4,y+8))
            self.relate("connect",f"shaft-{i}",f"head-{i}")
