"""A round face smartwatch with a yuan mark.

Plan: a six arc circular face, paired rear strap runs, and a centered yuan
glyph. Strap and face share four explicit attachment nodes. Lucide watch
informed the circle and band construction; the currency glyph follows source.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = "b1f2ce85-d591-4522-b2a6-64d3fc5c75f6"
SOURCE_PATH = "pictographic-primitives/combination/smart watch circle yuan sign_b1f2ce85-d591-4522-b2a6-64d3fc5c75f6.svg"
AUTHOR = "gpt-6"


class SmartWatchYuanSymbol(Solo48):
    icon_id = "smart-watch-yuan-symbol"
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/device"
    aliases = ("yuan smartwatch", "watch payment")
    keywords = ("watch", "smartwatch", "yuan", "currency", "payment")

    def build(self) -> None:
        curves = [
            ((8, 24), (8, 17), (11, 12), (16, 10)),
            ((16, 10), (20, 7), (28, 7), (32, 10)),
            ((32, 10), (37, 12), (40, 17), (40, 24)),
            ((40, 24), (40, 31), (37, 36), (32, 38)),
            ((32, 38), (28, 41), (20, 41), (16, 38)),
            ((16, 38), (11, 36), (8, 31), (8, 24)),
        ]
        for index, (start, c1, c2, end) in enumerate(curves, 1):
            self.add_bezier(f"face-{index}", start, (c1, c2, end))
        self.add_contour("face", *(f"face-{i}" for i in range(1, 7)), closed=True)
        self.add_polyline("upper-band", (16, 10), (17, 4), (31, 4), (32, 10))
        self.add_polyline("lower-band", (16, 38), (17, 44), (31, 44), (32, 38))
        self.relate("connect", "face", "upper-band")
        self.relate("connect", "face", "lower-band")
        self.add_polyline("yuan-forks", (19, 18), (24, 25), (29, 18))
        self.add_line("yuan-bar", (20, 25), (28, 25))
        self.add_line("yuan-stem", (24, 25), (24, 32))
        self.relate("connect", "yuan-forks", "yuan-bar")
        self.relate("connect", "yuan-forks", "yuan-stem")
        self.relate("connect", "yuan-bar", "yuan-stem")
