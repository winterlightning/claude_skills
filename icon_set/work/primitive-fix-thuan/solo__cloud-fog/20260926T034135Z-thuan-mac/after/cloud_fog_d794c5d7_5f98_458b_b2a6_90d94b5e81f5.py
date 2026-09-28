"""Fog: a cloud outline, open at the bottom, over two drifting mist lines.

Symbol plan: the cloud is one open bezier run from its left foot to its right foot:
a small left bump, a big central bump (top y=8) and a right bump, meeting at integer
cusps; its feet sit 9 above the first mist line. Mist: a long line from the left edge,
then a lower line broken into a longer and a shorter dash (8 apart), offset to the right,
as in the reference.
Lucide construction: 'cloud-fog' - open cloud over horizontal mist lines.
Keyshape HRECT_L: centerline x 4..44 (mist line ends), y 8..40 (cloud top, lower mist).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "d794c5d7-5f98-458b-b2a6-90d94b5e81f5"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__cloud-fog/20260926T034135Z-thuan-mac/reference/cloud mist_d794c5d7-5f98-458b-b2a6-90d94b5e81f5.svg"
AUTHOR = "claude-opus-5-5"


class CloudFog(Solo48):
    icon_id = "cloud-fog"
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "nature/weather"
    aliases = ("cloud mist", "fog", "mist", "haze")
    keywords = ("fog", "mist", "haze", "cloud", "weather", "foggy", "forecast")

    def build(self) -> None:
        foot = 23
        self.add_bezier(
            "cloud", (6, foot),
            ((6, 18), (9, 15), (13, 15)),       # left bump
            ((13, 11), (17, 8), (23, 8)),       # big bump, rising
            ((29, 8), (33, 11), (33, 15)),      # big bump, falling
            ((39, 15), (42, 18), (42, foot)),   # right bump
        )
        self.add_line("mist-1", (4, 32), (30, 32))
        self.add_line("mist-2a", (14, 40), (28, 40))
        self.add_line("mist-2b", (36, 40), (44, 40))
