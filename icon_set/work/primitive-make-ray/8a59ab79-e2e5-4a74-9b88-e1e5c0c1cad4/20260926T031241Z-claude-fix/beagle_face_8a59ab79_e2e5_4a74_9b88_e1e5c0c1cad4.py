"""A beagle face: wide domed skull, long drooping ears, jowl lobes and nose.

Symbol plan: mirrored about x=24. The skull is a half-ellipse (rx 20, ry 14) centred
(24,22) from ear top to ear top. Each ear falls from the skull end, rounds at its tip and
rises to the jowl junction J, where the straight inner ear edge meets it. From J a jowl
lobe leaves at a wide angle from the ear, dips to its low point L and rises to the central
notch N. The nose is a short round-capped bar on the axis.
Lucide construction: 'dog' - long ears as open lobes hanging from a round skull.
Keyshape HRECT_L: centerline x 4..44 (ear outer edges), y 8..40 (skull top, jowl lows).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "8a59ab79-e2e5-4a74-9b88-e1e5c0c1cad4"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__beagle-face/20260926T030905Z-thuan-mac/reference/beagle_8a59ab79-e2e5-4a74-9b88-e1e5c0c1cad4.svg"
AUTHOR = "claude-opus-5-5"


class BeagleFace(Solo48):
    icon_id = "beagle-face"
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "pets"
    aliases = ("beagle", "hound-face")
    keywords = ("dog", "beagle", "hound", "face", "breed", "pet", "floppy-ears", "puppy")

    def build(self) -> None:
        m = lambda p: (48 - p[0], p[1])
        E, J, TIP = (4, 22), (14, 30), (8, 36)
        TOP, L, N = (14, 20), (20, 40), (24, 37)
        self.add_arc("skull", E, m(E), radius_x=20, radius_y=14, sweep=True)
        for side, f in (("left", lambda p: p), ("right", m)):
            self.add_bezier(f"ear-{side}", f(E),
                            (f((4, 29)), f((5, 36)), f(TIP)),
                            (f((10, 36)), f((12, 33)), f(J)))
            self.add_line(f"ear-edge-{side}", f(TOP), f(J))
            self.add_bezier(f"jowl-{side}", f(J),
                            (f((16.5, 32.5)), f((16.5, 40)), f(L)),
                            (f((22, 40)), f((23.5, 38.5)), N))
            self.relate("connect", "skull", f"ear-{side}")
            self.relate("connect", f"ear-{side}", f"ear-edge-{side}")
            self.relate("connect", f"ear-{side}", f"jowl-{side}")
            self.relate("connect", f"ear-edge-{side}", f"jowl-{side}")
        self.relate("connect", "jowl-left", "jowl-right")
        self.add_line("nose", (23, 27), (25, 27))
