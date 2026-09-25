"""Face with Tongue Out. Rebuilt from the supplied visual reference on SOLO48.
Lucide construction: face-angry / face-slightly-frowning circular face and sparse expression;
glasses uses paired circular lenses. Shared axis and paired geometry preserve expression.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'bda1d256-4ee1-42d0-bda9-4c116c14cc88'
SOURCE_PATH = 'pictographic-primitives/smileys/crazy tongue_bda1d256-4ee1-42d0-bda9-4c116c14cc88.svg'
AUTHOR = 'gpt-6'


class FaceWithTongueOut(Solo48):
    icon_id = 'face-with-tongue-out'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "smileys"
    aliases = ()
    keywords = ('tongue', 'playful', 'silly', 'mouth', 'face', 'emoji')

    def build(self) -> None:

        # Circle envelope: center (24,24), radius 20; extremes 4 and 44.
        axis, radius = 24, 20
        self.add_arc("head-top", (axis-radius,24), (axis+radius,24), radius_x=radius)
        self.add_arc("head-bottom", (axis+radius,24), (axis-radius,24), radius_x=radius)
        self.add_contour("head", "head-top", "head-bottom", closed=True)

        for side, x in (("left",16),("right",32)):
            self.add_dot(f"eye-{side}", (x,17))

        self.add_line("mouth-left", (14,25),(20,25))
        self.add_line("mouth-center", (20,25),(28,25))
        self.add_line("mouth-right", (28,25),(34,25))
        self.add_contour("mouth", "mouth-left","mouth-center","mouth-right")
        self.add_line("tongue-left", (20,25),(20,31))
        self.add_arc("tongue-tip", (20,31),(28,31),radius_x=4,sweep=False)
        self.add_line("tongue-right", (28,31),(28,25))
        self.add_contour("tongue", "tongue-left","tongue-tip","tongue-right")
        for mouth in ("mouth-left","mouth-center"):
            self.relate("connect",mouth,"tongue-left")
        for mouth in ("mouth-center","mouth-right"):
            self.relate("connect",mouth,"tongue-right")
