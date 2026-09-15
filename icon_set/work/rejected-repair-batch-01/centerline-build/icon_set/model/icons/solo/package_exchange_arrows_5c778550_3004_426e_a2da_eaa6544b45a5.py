"""An isometric package between two opposing exchange arrows. The long horizontal arrows become compact diagonal corner arrows to keep all three cube faces legible. Lucide network informs shared-node connections; source establishes the cube. Intentional opposite diagonals express exchange.
SOLO48 VRECT_L; authored directly against the live contract, never scaled.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID='5c778550-3004-426e-a2da-eaa6544b45a5'
SOURCE_PATH='pictographic-primitives/programing/data exchange_5c778550-3004-426e-a2da-eaa6544b45a5.svg'
AUTHOR='gpt-6'

class PackageExchangeArrows(Solo48):
    icon_id='package-exchange-arrows'
    keyshape=Keyshape.VRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects/programming"
    aliases=()
    keywords=('exchange', 'data', 'package', 'cube', 'transfer', 'swap', 'arrows', 'sync')

    def build(self) -> None:
        self.add_polyline('cube',(24,14),(34,20),(34,30),(24,36),(14,30),(14,20),closed=True)
        self.add_line('face-left',(14,20),(24,26))
        self.add_line('face-right',(34,20),(24,26))
        self.add_line('face-down',(24,26),(24,36))
        for member in ('face-left','face-right','face-down'):
            self.relate('connect','cube',member)
        for a,b in (('face-left','face-right'),('face-left','face-down'),('face-right','face-down')):
            self.relate('connect',a,b)
        self.add_polyline('out-head',(32,4),(40,4),(40,12))
        self.add_line('out-shaft',(34,10),(40,4))
        self.relate('connect','out-head','out-shaft')
        self.add_polyline('in-head',(8,36),(8,44),(16,44))
        self.add_line('in-shaft',(12,40),(8,44))
        self.relate('connect','in-head','in-shaft')
