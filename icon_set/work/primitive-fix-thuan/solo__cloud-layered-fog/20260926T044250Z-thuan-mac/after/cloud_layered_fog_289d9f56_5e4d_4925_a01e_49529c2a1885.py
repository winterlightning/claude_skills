"""Layered fog: a cloud outline, open at the bottom, over three drifting mist lines.

Symbol plan: the cloud is one open bezier run from its left foot to its right foot:
a small left bump, a big central bump (top y=6) and a right bump meeting at integer
cusps; its feet sit 9 above the first mist line. Mist: three staggered lines 8 apart -
a long one from the left edge, a middle one offset right with a short dash beyond it
(8 apart), and a lower one offset left, as in the reference.
Lucide construction: 'cloud-fog' - open cloud over horizontal mist lines.
Keyshape SQUARE: centerline x 6..42 (mist ends), y 6..42 (cloud top, lowest mist).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "289d9f56-5e4d-4925-a01e-49529c2a1885"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__cloud-layered-fog/20260926T044250Z-thuan-mac/reference/cloud mist 2_289d9f56-5e4d-4925-a01e-49529c2a1885.svg"
AUTHOR = "claude-opus-5-5"


class CloudLayeredFog(Solo48):
    icon_id = "cloud-layered-fog"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "nature/weather"
    aliases = ("cloud mist", "fog", "mist", "haze")
    keywords = ("fog", "mist", "haze", "cloud", "weather", "foggy", "forecast", "layers")

    def build(self) -> None:
        foot = 17
        self.add_bezier(
            "cloud", (9, foot),
            ((9, 13), (11, 11), (15, 11)),      # left bump
            ((15, 8), (19, 6), (24, 6)),        # big bump, rising
            ((29, 6), (33, 8), (33, 11)),       # big bump, falling
            ((37, 11), (39, 13), (39, foot)),   # right bump
        )
        self.add_line("mist-1", (6, 26), (30, 26))
        self.add_line("mist-2a", (14, 34), (32, 34))
        self.add_line("mist-2b", (40, 34), (42, 34))
        self.add_line("mist-3", (10, 42), (28, 42))
