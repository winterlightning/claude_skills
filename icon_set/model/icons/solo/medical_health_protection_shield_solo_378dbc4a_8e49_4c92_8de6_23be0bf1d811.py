"""Medical Health Protection Shield. Authored directly on SOLO48 for later user-requested sub reuse.
Construction: local Lucide circle-check, triangle-alert, search, shield-plus,
smartphone and hand references inform coherent contours and shared joins.
Mirrored pointed shield and central medical cross.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._payments_batch01 import circle, rounded_rect
SOURCE_ICON_ID = '378dbc4a-8e49-4c92-8de6-23be0bf1d811'
SOURCE_PATH = 'pictographic-primitives/other/shield with plus_378dbc4a-8e49-4c92-8de6-23be0bf1d811.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'medical-health-protection-shield-solo'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    tags = ('sub icon',)
    keywords = ('sub icon', 'medical health protection shield')
    def build(self):
        # Plan: Mirrored pointed shield and central medical cross.
        self.add_bezier('shield',(24,4),((19,7),(14,9),(8,10)),((8,26),(8,35),(24,44)),((40,35),(40,26),(40,10)),((34,9),(29,7),(24,4)))
        self.add_contour('outline','shield',closed=True)
        self.add_polyline('cross-h',(17,23),(24,23),(31,23))
        self.add_polyline('cross-v',(24,16),(24,23),(24,30))
        self.relate('connect','cross-h','cross-v')
