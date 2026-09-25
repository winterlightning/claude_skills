from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'c577e0e4-e7f4-48be-941f-09df216731ed'
SOURCE_PATH = 'pictographic-primitives/container/concentrics circle 1_c577e0e4-e7f4-48be-941f-09df216731ed.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    """Two concentric rings form a target. Outer centerline extremes are 4 and 44."""
    icon_id = 'concentric-target'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "container"
    aliases = ()
    keywords = ('target', 'bullseye', 'symbol')

    def build(self):
        # Plan: two concentric circles owned by one center; radii preserve a clear ring.
        cx, cy = 24, 24
        for label, radius in [('outer',20),('inner',11)]:
            left, right = (cx-radius,cy), (cx+radius,cy)
            self.add_arc(label+'-top',left,right,radius_x=radius)
            self.add_arc(label+'-bottom',right,left,radius_x=radius)
            self.add_contour(label,label+'-top',label+'-bottom',closed=True)
