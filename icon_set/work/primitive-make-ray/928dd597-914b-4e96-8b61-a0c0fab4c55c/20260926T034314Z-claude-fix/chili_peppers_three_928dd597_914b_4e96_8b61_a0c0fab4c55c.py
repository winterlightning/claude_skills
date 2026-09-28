"""Three chili peppers stacked horizontally, each pointing left with a curled stem at its right end.

Symbol plan: one pod definition used three times (rows at y 4, 20, 37). A pod is one
closed outline of exactly two cubics between the pointed tip (left) and the head point
(right), both on the same row line: the top edge and the fuller belly. Their controls sit
at equal heights, so each edge's extreme lands exactly on an integer (pod 7 thick), and
both edges arrive vertical at the head point, which rounds the head. The stem leaves the
head point and curls up to the right. Pods are 9-10 apart.
Lucide construction: 'chili' has no local match; 'carrot'/'leaf'-style tapered pod.
Keyshape VRECT_L: centerline x 8..40 (tips, stem ends), y 4..44 (top pod, bottom belly).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "928dd597-914b-4e96-8b61-a0c0fab4c55c"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__chili-peppers-three/20260926T034135Z-thuan-mac/reference/three chilies_928dd597-914b-4e96-8b61-a0c0fab4c55c.svg"
AUTHOR = "claude-opus-5-5"


class ChiliPeppersThree(Solo48):
    icon_id = "chili-peppers-three"
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "food/vegetable"
    aliases = ("three chilies", "chilies", "hot peppers")
    keywords = ("chili", "pepper", "spicy", "hot", "heat level", "food", "vegetable", "spice")

    def build(self) -> None:
        up, down = 4, 16 / 3  # control offsets: 0.75*4 = 3 above, 0.75*16/3 = 4 below the row line
        for i, t in enumerate((4, 20, 37), start=1):
            row = t + 3
            tip, head = (8, row), (34, row)
            self.add_bezier(f"pod{i}-top", tip, ((22, row - up), (35, row - up), head))
            self.add_bezier(f"pod{i}-belly", head, ((35, row + down), (24, row + down), tip))
            self.add_contour(f"pod{i}", f"pod{i}-top", f"pod{i}-belly", closed=True)
            self.add_bezier(f"stem{i}", head, ((37, row - 1), (38, t + 1), (40, t)))
            self.relate("connect", f"pod{i}", f"stem{i}")
