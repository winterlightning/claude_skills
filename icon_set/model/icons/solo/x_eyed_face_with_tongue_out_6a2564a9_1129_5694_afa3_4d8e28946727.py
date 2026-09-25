"""X-Eyed Face with Tongue Out; independently reconstructed on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6a2564a9-1129-5694-afa3-4d8e28946727'
SOURCE_PATH = 'pictographic-primitives/smileys/tongue_6a2564a9-1129-5694-afa3-4d8e28946727.svg'
AUTHOR = 'gpt-6'


class XEyedFaceWithTongueOut(Solo48):
    icon_id = 'x-eyed-face-with-tongue-out'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "smileys"
    categories = ("smileys", "primitives")
    aliases = ()
    keywords = ('tongue', 'x eyes', 'silly', 'zany', 'face', 'emoji')

    def build(self) -> None:

        # CIRCLE: visible radius22; shared center (24,24), centerline radius20.
        axis,radius=24,20
        self.add_arc("head-top",(axis-radius,24),(axis+radius,24),radius_x=radius)
        self.add_arc("head-bottom",(axis+radius,24),(axis-radius,24),radius_x=radius)
        self.add_contour("head","head-top","head-bottom",closed=True)

        for side,x in (("left",17),("right",31)):
            self.add_polyline(f"eye-{side}-a",(x-2,17),(x,19),(x+2,21))
            self.add_polyline(f"eye-{side}-b",(x-2,21),(x,19),(x+2,17))
            for a in (1,2):
                for b in (1,2):self.relate("connect",f"eye-{side}-a-{a}",f"eye-{side}-b-{b}")
        self.add_line("smile-left",(14,30),(20,30))
        self.add_line("tongue-left",(20,30),(20,31))
        self.add_arc("tongue-tip",(20,31),(28,31),radius_x=4,sweep=False)
        self.add_line("tongue-right",(28,31),(28,30))
        self.add_line("smile-right",(28,30),(34,30))
        self.add_contour("mouth","smile-left","tongue-left","tongue-tip","tongue-right","smile-right")
