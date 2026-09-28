"""Triton: a crowned sea-god bust - three-point crown, long flowing hair, a round beard and broad shoulders.

Symbol plan: symmetric about x=24. The crown is one closed outline: a wide band (y=18)
with three points and two valleys above it. Below the band the face is one outline: two
straight sides and a half-ellipse beard (8x7) as its lower edge, with a mouth line across
where the beard begins. The hair is two wavy strands hanging free from the band's outer
ends, 8 outside the face. A straight shoulder line runs across the bottom, 9 below the
beard and 8 below the hair ends.
The reference's hairline waves and eye are dropped (they cannot keep 8-unit clearances
inside the face at 48).
Lucide construction: 'crown' for the band and points; bust composition.
Keyshape SQUARE: centerline x 6..42 (hair, shoulders), y 6..42 (crown points, shoulders).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "e0f0a128-2cb2-4393-b949-1e303f667163"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__crowned-triton-portrait/20260926T044250Z-thuan-mac/reference/triton_e0f0a128-2cb2-4393-b949-1e303f667163.svg"
AUTHOR = "claude-opus-5-5"


def _m(p):
    return (48 - p[0], p[1])


class CrownedTritonPortrait(Solo48):
    icon_id = "crowned-triton-portrait"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "people/mythology"
    aliases = ("triton", "poseidon", "sea god", "neptune")
    keywords = ("triton", "god", "crown", "king", "beard", "mythology", "greek", "sea", "portrait")

    def build(self) -> None:
        band, mouth, fl, fr = 18, 26, 16, 32
        # crown
        top = [(10, band), (10, 6), (17, 11), (24, 6), (31, 11), (38, 6), (38, band)]
        for i in range(1, len(top)):
            self.add_line(f"crown-top-{i}", top[i - 1], top[i])
        nodes = [38, fr, fl, 10]
        band_names = []
        for i in range(len(nodes) - 1):
            n = f"band-{i}"
            self.add_line(n, (nodes[i], band), (nodes[i + 1], band))
            band_names.append(n)
        self.add_contour("crown", *[f"crown-top-{i}" for i in range(1, 7)], *band_names, closed=True)
        # face and beard
        self.add_line("face-l", (fl, band), (fl, mouth))
        self.add_arc("beard", (fl, mouth), (fr, mouth), radius_x=8, radius_y=7, sweep=False)
        self.add_line("face-r", (fr, mouth), (fr, band))
        self.add_contour("face", "face-l", "beard", "face-r")
        self.add_line("mouth", (fl, mouth), (fr, mouth))
        self.relate("connect", "crown", "face")
        self.relate("connect", "face", "mouth")
        # hair strands
        for side, f in (("l", lambda p: p), ("r", _m)):
            self.add_bezier(f"hair-{side}", f((10, band)), (f((7, 21)), f((6, 24)), f((7, 27))),
                            (f((8, 30)), f((6, 31)), f((6, 34))))
            self.relate("connect", "crown", f"hair-{side}")
        self.add_line("shoulders", (6, 42), (42, 42))
