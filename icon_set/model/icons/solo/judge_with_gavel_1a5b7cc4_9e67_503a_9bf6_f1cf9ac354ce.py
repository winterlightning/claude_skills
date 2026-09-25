"""Judge with Gavel.

Symbol plan: Asymmetric bust and held gavel; circular head radius6 bottom18, shoulders top26: exact detached ink gap4. Head axis14. Centerline extremes (6,6)-(42,42). Gavel owns its handle node.
References: original SOURCE_PATH; Lucide pencil/gavel/hat-glasses for coherent
outlines and shared attachment nodes; human_ref/user.svg for circular heads
and rounded shoulders. Omit tiny decorative face, emblem and robe marks.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1a5b7cc4-9e67-503a-9bf6-f1cf9ac354ce'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/crime/legal judge_1a5b7cc4-9e67-503a-9bf6-f1cf9ac354ce.svg'
AUTHOR = 'gpt-6'

class JudgeWithGavel(Solo48):
    icon_id = 'judge-with-gavel'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "crime"
    categories = ("crime", "primitives")
    aliases = ()
    keywords = ('judge', 'with', 'gavel')

    def build(self):
        self.add_arc('head-top',(8,12),(20,12),radius_x=6)
        self.add_arc('head-bottom',(20,12),(8,12),radius_x=6)
        self.add_contour('head','head-top','head-bottom',closed=True)
        self.add_line('body-left',(6,42),(6,34))
        self.add_arc('shoulder-left',(6,34),(14,26),radius_x=8)
        self.add_arc('shoulder-right',(14,26),(22,34),radius_x=8)
        self.add_line('body-right',(22,34),(22,42))
        self.add_contour('body','body-left','shoulder-left','shoulder-right','body-right')
        self.add_polyline('gavel',(30,10),(42,10),(42,20),(36,20),(30,20),closed=True)
        self.add_line('handle',(36,20),(30,34))
        self.relate('connect','gavel','handle')
