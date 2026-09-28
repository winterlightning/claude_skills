"""Compact disc with reflection bands: a CD seen face-on - outer rim, hub ring, a dot
spindle hole, and two pairs of radial reflection lines.

Symbol plan: point symmetry about the centre. The rim is a radius-20 circle and the
hub a radius-10 circle about (24,24); both are split where the reflection lines
meet them, at directions (1,0) and (3,4) and their opposites, which are integer
points of both circles (hub (34,24)/(30,32), rim (44,24)/(36,40), mirrored). Each
reflection line runs radially from hub to rim; the two lines of a pair are 53
degrees apart (8.9 apart at the hub). The spindle is a single dot 10 inside the hub.
Revision (reviewer: "change the inner circle become a dot"): the spindle ring is a
dot; the reference's hub ring and reflection-line pairs replace the two stubs.
Lucide construction: 'disc' - rim, hub ring and centre dot.
Keyshape CIRCLE: radius 20.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "f5fbc057-7aee-4e09-9bf8-51ff852cd4ca"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__compact-disc-with-reflection-bands/20260926T073832Z-thuan-mac/reference/cd playing_f5fbc057-7aee-4e09-9bf8-51ff852cd4ca.svg"
AUTHOR = "claude-opus-5-5"

DIRECTIONS = ((5, 0), (3, 4), (-5, 0), (-3, -4))  # clockwise order, unit 5


class CompactDiscWithReflectionBands(Solo48):
    icon_id = "compact-disc-with-reflection-bands"
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "media/music"
    aliases = ("cd", "cd-playing", "disc")
    keywords = ("cd", "compact-disc", "disc", "music", "audio", "dvd", "media")

    def ring(self, name: str, r: int) -> list[tuple[int, int]]:
        k = r // 5
        pts = [(24 + dx * k, 24 + dy * k) for dx, dy in DIRECTIONS]
        members = []
        for i, a in enumerate(pts):
            b = pts[(i + 1) % 4]
            self.add_arc(f"{name}-{i}", a, b, radius_x=r, sweep=True)
            members.append(f"{name}-{i}")
        self.add_contour(name, *members, closed=True)
        return pts

    def build(self) -> None:
        rim = self.ring("rim", 20)
        hub = self.ring("hub", 10)
        for i, (a, b) in enumerate(zip(hub, rim)):
            self.add_line(f"reflection-{i}", a, b)
            self.relate("connect", f"reflection-{i}", "hub")
            self.relate("connect", f"reflection-{i}", "rim")
        self.add_dot("spindle", (24, 24))
