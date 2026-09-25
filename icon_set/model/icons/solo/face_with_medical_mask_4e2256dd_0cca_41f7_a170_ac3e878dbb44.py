"""Face with Medical Mask; independently reconstructed on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4e2256dd-0cca-41f7-a170-ac3e878dbb44'
SOURCE_PATH = 'pictographic-primitives/smileys/sick contageous_4e2256dd-0cca-41f7-a170-ac3e878dbb44.svg'
AUTHOR = 'gpt-6'


class FaceWithMedicalMask(Solo48):
    icon_id = 'face-with-medical-mask'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "smileys"
    categories = ("smileys", "primitives")
    aliases = ()
    keywords = ('mask', 'medical', 'sick', 'ill', 'face', 'emoji')

    def build(self) -> None:

        # CIRCLE: visible radius22; shared center (24,24), centerline radius20.
        axis,radius=24,20
        self.add_arc("head-top",(axis-radius,24),(axis+radius,24),radius_x=radius)
        self.add_arc("head-bottom",(axis+radius,24),(axis-radius,24),radius_x=radius)
        self.add_contour("head","head-top","head-bottom",closed=True)

        self.add_dot("eye-left",(17,17))
        self.add_dot("eye-right",(31,17))
        self.add_polyline("mask",(18,26),(30,26),(30,34),(18,34),closed=True)
        self.add_line("strap-left",(4,24),(18,26))
        self.add_line("strap-right",(30,26),(44,24))
        for h in ("head-top","head-bottom"):
            self.relate("connect","strap-left",h)
            self.relate("connect","strap-right",h)
        for m in ("mask-1","mask-4"):self.relate("connect","strap-left",m)
        for m in ("mask-1","mask-2"):self.relate("connect","strap-right",m)
