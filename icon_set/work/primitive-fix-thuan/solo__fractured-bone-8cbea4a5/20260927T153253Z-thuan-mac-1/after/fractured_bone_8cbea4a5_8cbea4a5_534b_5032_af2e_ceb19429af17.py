"""Fractured bone lying on the diagonal (specialty: broken bone).

Symbol plan: the bone axis is x+y=48 (bottom-left to top-right). The shaft
edges are x+y=42 and x+y=54 (8.5 apart). Each end is a two-lobe knob of r4
semicircles centred on the shaft edge lines, (38,16) and (32,10), joined by
a concave r2 notch about (38,10) and eased into the shaft by short cubics
(Lucide `bone` construction). The fracture is a stair-step (horizontal and
vertical steps, which read as a jagged crack across the diagonal shaft); the
lower half is the half-turn of the upper half, so the two breaks are parallel
translations 8.9 apart.
Revision: the rejected drawing had two squat knobs with no shaft, so it read as
two blobs; the reference is a long bone snapped in the middle.
Omitted: the reference's small crack tick beside the break (no room at 8 MIC).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "8cbea4a5-534b-5032-af2e-ceb19429af17"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__fractured-bone-8cbea4a5/20260927T153253Z-thuan-mac-1/reference/specialty broken bone_8cbea4a5-534b-5032-af2e-ceb19429af17.svg"
AUTHOR = "claude-opus-5-5"


class FracturedBone(Solo48):
    icon_id = "fractured-bone-8cbea4a5"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "medical"
    categories = ("primitives", "medical")
    aliases = ("broken bone", "fracture")
    keywords = ("bone", "broken", "fracture", "orthopedic", "injury", "x-ray")

    def build(self) -> None:
        for half in (0, 1):
            def p(x, y, h=half):
                return (x, y) if h == 0 else (48 - x, 48 - y)
            n = f"half-{half}"
            self.add_line(f"{n}-break-1", p(26, 16), p(26, 20))
            self.add_line(f"{n}-break-2", p(26, 20), p(30, 20))
            self.add_line(f"{n}-break-3", p(30, 20), p(30, 24))
            self.add_line(f"{n}-edge-a", p(30, 24), p(35, 19))
            self.add_bezier(f"{n}-ease-a", p(35, 19), (p(35.7, 19.7), p(36.5, 20), p(38, 20)))
            self.add_arc(f"{n}-lobe-a", p(38, 20), p(38, 12), radius_x=4, sweep=False)
            self.add_arc(f"{n}-notch", p(38, 12), p(36, 10), radius_x=2, sweep=True)
            self.add_arc(f"{n}-lobe-b", p(36, 10), p(28, 10), radius_x=4, sweep=False)
            self.add_bezier(f"{n}-ease-b", p(28, 10), (p(28, 11.5), p(28.3, 12.3), p(29, 13)))
            self.add_line(f"{n}-edge-b", p(29, 13), p(26, 16))
            self.add_contour(n, *(f"{n}-{k}" for k in (
                "break-1", "break-2", "break-3", "edge-a", "ease-a",
                "lobe-a", "notch", "lobe-b", "ease-b", "edge-b")), closed=True)
