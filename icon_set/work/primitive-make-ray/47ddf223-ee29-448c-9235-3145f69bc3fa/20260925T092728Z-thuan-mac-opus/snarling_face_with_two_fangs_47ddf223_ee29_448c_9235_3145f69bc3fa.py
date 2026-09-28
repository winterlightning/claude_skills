"""Snarl: an angry face - brows slanting down toward the centre with
half-moon eyes hanging beneath them, over an open mouth showing two fangs.

Symbol plan: each eye is one brow line (slope 1:2, split at the node where
the eye begins) plus a cubic half-moon from that node to the brow's inner
end; the right eye mirrors the left about x = 24. The mouth is a closed
rounded box (radius-4 corners); the fangs are two strokes from split nodes
on its top edge, 8 from the sides and 9 from the bottom. The reference's
rounded-square face outline is omitted: 8 units inside its rim leave a
20-unit square, too small for eyes with valid holes and a fanged mouth.
Keyshape SQUARE, centerline box (6,6)-(42,42).
Lucide construction: angry (slanted brows over eyes, mouth below).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "47ddf223-ee29-448c-9235-3145f69bc3fa"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__snarling-face-with-two-fangs/20260925T092530Z-thuan-mac/reference/snarl_47ddf223-ee29-448c-9235-3145f69bc3fa.svg"
AUTHOR = "claude-opus-5-5"


class SnarlingFaceWithTwoFangs(Solo48):
    icon_id = "snarling-face-with-two-fangs"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "emoji"
    aliases = ("snarl", "angry face", "growl")
    keywords = ("face", "snarl", "angry", "fangs", "growl", "emoji")

    def build(self) -> None:
        for index, side in enumerate((1, -1), 1):
            self.eye(f"eye-{index}", side)
        top, bottom, left, right, r = 28, 42, 10, 38, 4
        fangs = (18, 30)
        self.add_line("mouth-top-1", (left + r, top), (fangs[0], top))
        self.add_line("mouth-top-2", (fangs[0], top), (fangs[1], top))
        self.add_line("mouth-top-3", (fangs[1], top), (right - r, top))
        self.add_arc("mouth-2", (right - r, top), (right, top + r), radius_x=r)
        self.add_line("mouth-3", (right, top + r), (right, bottom - r))
        self.add_arc("mouth-4", (right, bottom - r), (right - r, bottom), radius_x=r)
        self.add_line("mouth-5", (right - r, bottom), (left + r, bottom))
        self.add_arc("mouth-6", (left + r, bottom), (left, bottom - r), radius_x=r)
        self.add_line("mouth-7", (left, bottom - r), (left, top + r))
        self.add_arc("mouth-8", (left, top + r), (left + r, top), radius_x=r)
        self.add_contour("mouth", "mouth-top-1", "mouth-top-2", "mouth-top-3",
                         *[f"mouth-{i}" for i in range(2, 9)], closed=True)
        for index, x in enumerate(fangs, 1):
            self.add_line(f"fang-{index}", (x, top), (x, top + 5))
            self.relate("connect", "mouth", f"fang-{index}")

    def eye(self, name, side, depth=9):
        """Brow from (6,6) to (20,13) (slope 1:2); the half-moon runs from the
        brow node (8,7) to its inner end, its controls pushed depth along
        the chord's downward normal (-1, 2) / sqrt(5)."""
        def m(x, y):
            return (x, y) if side == 1 else (48 - x, y)
        outer, start, inner = m(6, 6), m(8, 7), m(20, 13)
        nx, ny = -depth / 5 ** 0.5, 2 * depth / 5 ** 0.5
        c_inner = m(20 + nx, 13 + ny)
        c_start = m(8 + nx, 7 + ny)
        self.add_line(f"{name}-brow-1", outer, start)
        self.add_line(f"{name}-brow-2", start, inner)
        self.add_bezier(f"{name}-lid", inner, (c_inner, c_start, start))
        self.add_contour(name, f"{name}-brow-2", f"{name}-lid", closed=True)
        self.relate("connect", f"{name}-brow-1", name)
