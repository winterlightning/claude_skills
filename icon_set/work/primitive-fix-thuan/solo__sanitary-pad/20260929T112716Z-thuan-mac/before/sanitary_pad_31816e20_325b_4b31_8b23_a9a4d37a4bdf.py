"""Sanitary Pad.

Plan: Diagonal capsule-like pad with a nested absorbent panel. Lucide pill informs rounded diagonal silhouette. Bounds (6,6)-(42,42). Inset loop kept; matching capsule halves share radii.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '31816e20-325b-4b31-8b23-a9a4d37a4bdf'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/health/sanitary pad_31816e20-325b-4b31-8b23-a9a4d37a4bdf.svg'
AUTHOR = 'gpt-6'


class SanitaryPad(Solo48):
    icon_id = 'sanitary-pad'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'health'
    categories = ('health', 'state')
    aliases = ()
    keywords = ('sanitary', 'pad')

    def build(self):
        self.add_line('left',(12,15),(18,9))
        self.add_arc('top-cap',(18,9),(36,33),radius_x=15)
        self.add_line('right',(36,33),(30,39))
        self.add_arc('bottom-cap',(30,39),(12,15),radius_x=15)
        self.add_contour('pad','left','top-cap','right','bottom-cap',closed=True)
        self.add_line('panel-left',(19,22),(23,18))
        self.add_arc('panel-top',(23,18),(29,26),radius_x=5)
        self.add_line('panel-right',(29,26),(25,30))
        self.add_arc('panel-bottom',(25,30),(19,22),radius_x=5)
        self.add_contour('absorbent-panel','panel-left','panel-top','panel-right','panel-bottom',closed=True)
