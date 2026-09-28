"""Person Vomiting into Bowl.
Plan: A forward-bent kneeling figure reaches to a bowl on the left. Head center (14,12), r=4; neck (26,12), exact horizontal 8 centerline / 4 ink gap. Extrema (4,8)-(44,40).
Reference: human_ref/full_body_ref.png: bent/kneeling torso, circular head and round-ended limbs.
Reduction: Outlined thick limbs reduced to coherent stick-figure strokes; no vomiting stream added.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '36050eda-0953-5f1d-b828-3b3c917e1c94'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__person-kneeling-beside-bowl/20260927T153747Z-thuan-mac-1/reference/party throw up_36050eda-0953-5f1d-b828-3b3c917e1c94.svg'
AUTHOR = "gpt-6"


class Batch26Icon(Solo48):
    icon_id = 'person-kneeling-beside-bowl'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "events"
    categories = ("primitives", "events")
    aliases = ()
    keywords = ('person', 'vomiting', 'into', 'bowl')

    def build(self):
        # Head faces a bowl while one arm reaches down and a bent knee supports the pose.
        self.add_arc('head-top', (10, 12), (18, 12), radius_x=4)
        self.add_arc('head-bottom', (18, 12), (10, 12), radius_x=4)
        self.add_contour('head', 'head-top', 'head-bottom', closed=True)
        self.add_line('torso', (26, 12), (32, 12))
        self.add_arc('back-round', (32, 12), (38, 18), radius_x=6)
        self.add_line('hip', (38, 18), (38, 28))
        self.add_polyline('leg', (38, 28), (30, 40), (44, 40))
        self.add_polyline('arm', (26, 12), (26, 30), (16, 30))
        self.add_line('rim', (4, 30), (16, 30))
        self.add_arc('bowl', (16, 30), (4, 30), radius_x=6, radius_y=10)
        for left,right in (('torso','back-round'),('back-round','hip'),('hip','leg'),('arm','torso'),('arm','rim'),('arm','bowl'),('rim','bowl')):
            self.relate('connect', left, right)
        self.mark_human_figure('person', head='head', torso='torso', torso_junction='start')
