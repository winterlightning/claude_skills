"""Athlete swimming freestyle in ocean waves, authored on SOLO48.

Human reference: full_body_ref.png — outlined circular head, round-ended
limbs, minimal anatomy. Lucide waves-horizontal informs the repeating wave.
Plan: detached head; one bent recovery arm joined to the diagonal torso;
one continuous ocean wave. HRECT_L centerline bounds (4,8)-(44,40).
Head/body separation is horizontal: head left x=30, shoulder x=22,
therefore 8 centerline units and exactly 4 visible units. Motion is asymmetric.
Omit submerged legs, goggles and extra wave rows for native-size readability.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = None
SOURCE_PATH = "icon_set/references/human_ref/full_body_ref.png"
AUTHOR = "gpt-6"


class OceanSwimmer(Solo48):
    icon_id = "ocean-swimmer"
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "sports"
    categories = ("sports",)
    aliases = ("open-water-swimmer",)
    keywords = ("athlete", "swimming", "freestyle", "ocean", "sea", "sport", "human")

    def build(self) -> None:
        cx, cy, radius = 36, 16, 6
        gap, stroke = 4, 4
        shoulder = (cx-radius-stroke-gap, cy)
        self.add_arc("head-top", (cx-radius, cy), (cx+radius, cy), radius_x=radius)
        self.add_arc("head-bottom", (cx+radius, cy), (cx-radius, cy), radius_x=radius)
        self.add_contour("head", "head-top", "head-bottom", closed=True)
        self.add_polyline("swimming-body", (4, 16), (14, 8), shoulder, (8, 26))
        wave_ids = []
        for index in range(4):
            x = 4 + index * 10
            name = f"wave-{index}"
            crest = 40 if index % 2 == 0 else 36
            self.add_bezier(name, (x, 38),
                            ((x+2, crest), (x+3, crest), (x+5, crest)),
                            ((x+7, crest), (x+8, crest), (x+10, 38)))
            wave_ids.append(name)
        self.add_contour("ocean", *wave_ids)
