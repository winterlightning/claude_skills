"""A man balances on one leg while kicking a soccer ball to the right.

Plan: two circular loops (head and ball), and an articulated body with shared
shoulder/hip nodes. Intentionally asymmetric limbs describe the kicking action.
SQUARE centerline extremes: left 6, top 6, right 42, bottom 42.
Human reference: icon_set/references/human_ref/full_body_ref.png, lower-left
figure's outlined head and single-stroke anatomy. Head radius 3; shoulder y=20
is exactly 8 below head bottom y=12, giving 4 units of painted clearance.
Lucide person-standing original and atomic-debug inform shared limb junctions.
Omit clothing, facial features and ball panels to preserve native-size clarity.
"""

from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = None
SOURCE_PATH = None
AUTHOR = "gpt-6"


class ManPlayingFootball(Solo48):
    icon_id = "man-playing-football"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "sports"
    categories = ("sports",)
    aliases = ("man-playing-soccer", "soccer-player-kicking")
    keywords = ("man", "football", "soccer", "sports", "player", "kick", "ball")

    def build(self) -> None:
        head_x, head_y, head_radius = 20, 9, 3
        shoulder = (head_x, head_y + head_radius + 8)
        hip = (16, 29)
        for name, cx, cy, radius in (
            ("head", head_x, head_y, head_radius),
            ("ball", 39, 39, 3),
        ):
            left, right = (cx - radius, cy), (cx + radius, cy)
            self.add_arc(name + "-top", left, right, radius_x=radius)
            self.add_arc(name + "-bottom", right, left, radius_x=radius)
            self.add_contour(name, name + "-top", name + "-bottom", closed=True)

        branches = (
            ("back-arm", ((6, 24), (10, 20), shoulder)),
            ("front-arm", (shoulder, (30, 24))),
            ("torso", (shoulder, hip)),
            ("standing-leg", (hip, (10, 42))),
            ("kicking-leg", (hip, (22, 37), (28, 37))),
        )
        segments = []
        for name, points in branches:
            self.add_polyline(name, *points)
            for index, (start, end) in enumerate(zip(points, points[1:]), 1):
                segments.append((f"{name}-{index}", start, end))
        for index, (name, start, end) in enumerate(segments):
            for other, a, b in segments[index + 1:]:
                if start in (a, b) or end in (a, b):
                    self.relate("connect", name, other)
