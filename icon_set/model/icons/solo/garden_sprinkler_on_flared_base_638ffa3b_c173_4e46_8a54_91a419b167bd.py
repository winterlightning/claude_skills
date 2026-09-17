"""Water Garden Sprinkler.
Plan: Rounded sprinkler head over a stem and triangular foot; symmetric spray fan. Extrema (6,6)-(42,42).
Reference: Supplied original; no useful exact local Lucide match. Sparse outline and shared attachment principles.
Reduction: Five small spray strokes reduced to three clear jets; head and flared foot retained.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '638ffa3b-c173-4e46-8a54-91a419b167bd'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/farming/spirinkler_638ffa3b-c173-4e46-8a54-91a419b167bd.svg'
AUTHOR = 'gpt-6'

class Batch29Icon(Solo48):
    icon_id = 'garden-sprinkler-on-flared-base'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/agriculture"
    aliases = ()
    keywords = ('water', 'garden', 'sprinkler')

    def build(self):

        self.add_arc('head-top',(18,22),(30,22),radius_x=6)
        self.add_line('head-low-1',(30, 22),(24, 30))
        self.add_line('head-low-2',(24, 30),(18, 22))
        self.add_contour('head','head-top','head-low-1','head-low-2',closed=True)
        self.add_line('stem',(24,30),(24,34));self.relate('connect','head','stem')
        self.add_polyline('base',(24,34),(16,42),(32,42),(24,34));self.relate('connect','stem','base')
        self.add_line('jet',(24,6),(24,8))
        self.add_line('spray-left',(6,10),(12,14))
        self.add_line('spray-right',(42,10),(36,14))
