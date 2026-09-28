"""Cube: A cube is shown from above with a diamond-shaped top and two upright side faces meeting at a central vertical edge. Generate this component alone; exclude Magnifying Glass Frame.

Construction: An isometric cube preserves its diamond top and two side faces around one centre edge.
Keyshape: VRECT_XL; authored to the SUB32 envelope.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '76ca25eb-ec7a-4588-b4d3-72d2792ce8ed'
SOURCE_PATH = 'pictographic-primitives/state/magnifying glass cube_76ca25eb-ec7a-4588-b4d3-72d2792ce8ed.svg'
AUTHOR = 'gpt-6'


class CubeSub(Sub32):
    icon_id = 'cube-sub'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'state'
    categories = ('state',)
    aliases = ()
    keywords = ('cube', 'shown', 'diamond', 'shaped', 'top', 'upright', 'side', 'faces')

    def build(self):
        self.add_polyline('outline',(16,2),(28,8),(28,24),(16,30),(4,24),(4,8),closed=True)
        self.add_polyline('top-divide',(4,8),(16,14),(28,8))
        self.add_line('centre',(16,14),(16,30))
        self.relate('connect','outline','top-divide')
        self.relate('connect','outline','centre')
        self.relate('connect','top-divide','centre')
