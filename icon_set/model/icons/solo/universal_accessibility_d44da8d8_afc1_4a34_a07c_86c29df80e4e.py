"""Universal accessibility: a frontal person with open arms within a circle.

CIRCLE owns the radius-20 envelope about (24,24). The ring owns clearance
to the figure; all paired limbs mirror on x=24 from shared spans.
Head radius 2 at (24,15), neck (24,25): 8 centerline / 4 ink gap.
Arms split at the neck; legs split at the hip, with real shared-node joins.
The supplied reference contributes the circular enclosure and open-arm pose.
human_ref/full_body_ref.png contributes the detached circular head and simple
limbs; Lucide person-standing contributes the shared shoulder/hip structure.
Replace the source's outlined body with the prescribed stick figure.
Text reuse/layout brief: exact label 'A11Y', centered below the symbol, using
glyphs letter-a-uppercase, digit-1, digit-1, letter-y-uppercase from
icon_set/typeface/glyphs.json. Lettering is separate from this SOLO48 export.
"""

from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = "d44da8d8-afc1-4a34-a07c-86c29df80e4e"
SOURCE_PATH = "pictographic-primitives/_uncategorized_01/a11y accessibility disability_d44da8d8-afc1-4a34-a07c-86c29df80e4e.svg"
AUTHOR = "gpt-6"


class UniversalAccessibility(Solo48):
    icon_id = "universal-accessibility"
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/uncategorized"
    aliases = ("A11Y", "universal access", "accessibility symbol")
    keywords = ("accessibility", "a11y", "universal", "access", "inclusive", "person")

    def build(self):
        axis = 24
        def circle(name, cy, radius):
            points = ((axis, cy-radius), (axis+radius, cy),
                      (axis, cy+radius), (axis-radius, cy), (axis, cy-radius))
            members = []
            for index, (start, end) in enumerate(zip(points, points[1:])):
                part = f"{name}-{index}"
                self.add_arc(part, start, end, radius_x=radius)
                members.append(part)
            self.add_contour(name, *members, closed=True)

        circle("ring", 24, 20)
        circle("head", 15, 2)
        shoulder, hip = (axis, 25), (axis, 33)
        self.add_line("torso", shoulder, hip)
        for name, sign in (("left", -1), ("right", 1)):
            hand = (axis+sign*10, shoulder[1])
            start, end = (hand, shoulder) if sign < 0 else (shoulder, hand)
            self.add_line(f"arm-{name}", start, end)
            self.add_line(f"leg-{name}", hip, (axis+sign*4, 35))
            self.relate("connect", "torso", f"arm-{name}")
            self.relate("connect", "torso", f"leg-{name}")
        self.add_contour("arms", "arm-left", "arm-right")
        self.relate("connect", "leg-left", "leg-right")
        self.mark_human_figure("person", head="head", torso="torso", torso_junction="start")
