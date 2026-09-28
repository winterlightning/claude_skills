"""Scuba Diver. Right-swimming diver with bent legs and an attached back tank; surface reduced to one line and lower waves omitted.
Keyshape HRECT_L, visible extremes (2, 6, 46, 42); centerline envelope inset by 2.
Construction: Lucide person-standing: a circular head and sparse articulated limbs. Source establishes the subject and pose.
Shared circles and rounded rectangles keep repeated radii coherent."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '559d4aad-57a7-4a2f-a69a-7e30a9faaaba'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__scuba-diver/20260927T084430Z-thuan-mac-1/reference/diving diver_559d4aad-57a7-4a2f-a69a-7e30a9faaaba.svg'
AUTHOR = "gpt-6"


class ScubaDiver(Solo48):
    icon_id = "scuba-diver"
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "recreation"
    categories = ("primitives", "recreation")
    aliases = ()
    keywords = ("scuba", "diver", "swimming", "tank")

    def build(self):
        # Reference body: long prone silhouette, back tank, isolated head.
        # Lucide waves informed one broad surface swell. The tail is intentionally directional.
        self.add_bezier('surface-swell',(4,8),((10,9),(18,9),(28,8)))
        self.add_line('surface-flat',(28,8),(44,8))
        self.add_contour('surface','surface-swell','surface-flat')
        self.add_arc('head-top',(35,21),(43,21),radius_x=4)
        self.add_arc('head-bottom',(43,21),(35,21),radius_x=4)
        self.add_contour('head','head-top','head-bottom',closed=True)
        self.add_polyline('body',(4,20),(12,20),(16,28),(26,28),(30,29),(30,32),(25,36),(18,36),(12,32),(4,24),closed=True)
        self.add_polyline('tank',(16,28),(16,18),(26,18),(26,28))
        self.relate('connect','tank','body')
        self.add_polyline('fin',(30,32),(39,40),(44,40))
        self.relate('connect','fin','body')
        self.mark_human_figure('diver',head='head',torso='body-4',torso_junction='start')
