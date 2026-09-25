"""A tilted open bottle pouring toward a separate teardrop below/left. Preserve the angled bottle silhouette and the droplet; do not replace this with an upright capped bottle.

Plan: Diagonal pouring bottle with an open mouth and a detached droplet. Bounds (2,2)-(30,30).
Construction reference: No close Lucide subject; use simple connected contours."""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'cb098a0f-2ebc-4e1f-b567-e7306fca7ed6'
SOURCE_PATH = 'pictographic-primitives/state/bottle drop_cb098a0f-2ebc-4e1f-b567-e7306fca7ed6.svg'
SOURCE_ICON_IDS = ('cb098a0f-2ebc-4e1f-b567-e7306fca7ed6', '167045a9-1f88-4bed-ac0e-a676e4818fdc')
AUTHOR = 'gpt-6'

class TiltedBottleAndDropSub(Sub32):
    icon_id = 'tilted-bottle-and-drop-sub'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'state'
    aliases = ()
    keywords = ('tilted', 'bottle', 'and', 'drop', 'sub')

    def build(self) -> None:
        self.add_polyline('bottle',(11,15),(13,13),(13,9),(20,2),(30,12),(23,19),(19,19),(16,22))
        self.add_bezier('drop-left',(6,20),((5,22),(2,25),(2,27)),((2,29),(4,30),(6,30)))
        self.add_bezier('drop-right',(6,30),((8,30),(10,29),(10,27)),((10,25),(7,22),(6,20)))
        self.add_contour('drop','drop-left','drop-right',closed=True)
