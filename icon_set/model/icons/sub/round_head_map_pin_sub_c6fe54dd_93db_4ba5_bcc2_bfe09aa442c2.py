"""A round pin head above a long straight vertical stem. This is a pin, not a teardrop location marker.

Plan: Circular pin head and a long centered stem. Bounds (8,2)-(24,30).
Construction reference: No close Lucide subject; use simple connected contours."""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'c6fe54dd-93db-4ba5-bcc2-bfe09aa442c2'
SOURCE_PATH = 'pictographic-primitives/state/pin task_c6fe54dd-93db-4ba5-bcc2-bfe09aa442c2.svg'
SOURCE_ICON_IDS = ('c6fe54dd-93db-4ba5-bcc2-bfe09aa442c2',)
AUTHOR = 'gpt-6'

class RoundHeadMapPinSub(Sub32):
    icon_id = 'round-head-map-pin-sub'
    keyshape = Keyshape.VRECT_M
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'state'
    categories = ('state',)
    aliases = ()
    keywords = ('round', 'head', 'map', 'pin', 'sub')

    def build(self) -> None:
        self.add_arc('head-a',(16,2),(16,18),radius_x=8)
        self.add_arc('head-b',(16,18),(16,2),radius_x=8)
        self.add_contour('head','head-a','head-b',closed=True)
        self.add_line('stem',(16,18),(16,30))
        self.relate('connect','head','stem')
