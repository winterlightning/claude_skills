"""Disguised Face. Rebuilt from the supplied visual reference on SOLO48.
Lucide construction: face-angry / face-slightly-frowning circular face and sparse expression;
glasses uses paired circular lenses. Shared axis and paired geometry preserve expression.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f7b41792-3c8f-403e-b9a7-c16ae8fb7788'
SOURCE_PATH = 'pictographic-primitives/smileys/disguised face old_f7b41792-3c8f-403e-b9a7-c16ae8fb7788.svg'
AUTHOR = 'gpt-6'


class DisguisedFace(Solo48):
    icon_id = 'disguised-face'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "people/emotions"
    aliases = ()
    keywords = ('disguise', 'glasses', 'moustache', 'nose', 'face', 'emoji')

    def build(self) -> None:

        # Circle envelope: center (24,24), radius 20; extremes 4 and 44.
        axis, radius = 24, 20
        self.add_arc("head-top", (axis-radius,24), (axis+radius,24), radius_x=radius)
        self.add_arc("head-bottom", (axis+radius,24), (axis-radius,24), radius_x=radius)
        self.add_contour("head", "head-top", "head-bottom", closed=True)

        # Paired small circular lenses use the contract's complete-circle exception.
        for side,x in (("left",17),("right",31)):
            self.add_arc(f"lens-{side}-top",(x-3,19),(x+3,19),radius_x=3)
            self.add_arc(f"lens-{side}-bottom",(x+3,19),(x-3,19),radius_x=3)
            self.add_contour(f"lens-{side}",f"lens-{side}-top",f"lens-{side}-bottom",closed=True)
        self.add_line("bridge",(20,19),(28,19))
        for side in ("left","right"):
            for half in ("top","bottom"):
                self.relate("connect","bridge",f"lens-{side}-{half}")
        self.add_arc("moustache-left",(16,32),(24,30),radius_x=7,sweep=False)
        self.add_arc("moustache-right",(24,30),(32,32),radius_x=7,sweep=False)
        self.add_contour("moustache","moustache-left","moustache-right")
