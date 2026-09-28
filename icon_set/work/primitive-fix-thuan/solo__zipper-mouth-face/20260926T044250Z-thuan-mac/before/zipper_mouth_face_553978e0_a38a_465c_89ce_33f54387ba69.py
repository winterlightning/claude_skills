"""Zipper-Mouth Face; independently reconstructed on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '553978e0-a38a-465c-89ce-33f54387ba69'
SOURCE_PATH = 'pictographic-primitives/smileys/zipped_553978e0-a38a-465c-89ce-33f54387ba69.svg'
AUTHOR = 'gpt-6'


class ZipperMouthFace(Solo48):
    icon_id = 'zipper-mouth-face'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "smileys"
    categories = ("smileys", "primitives")
    aliases = ()
    keywords = ('zipper', 'mouth', 'silent', 'secret', 'face', 'emoji')

    def build(self) -> None:

        # CIRCLE: the slider occludes the lower-right rim.
        self.add_arc("head-top",(4,24),(36,8),radius_x=20)
        self.add_arc("head-bottom",(24,44),(4,24),radius_x=20)
        self.add_contour("head","head-bottom","head-top")
        self.add_line("eye-left",(17,17),(18,17))
        self.add_line("eye-right",(30,17),(31,17))
        self.add_polyline("zip",(16,29),(24,29),(32,29))
        for n,x in enumerate((16,24)):
            self.add_polyline(f"tooth-{n}",(x,26),(x,29),(x,32))
            for z in (1,2):
                if n==0 and z==2:continue
                for t in (1,2):self.relate("connect",f"zip-{z}",f"tooth-{n}-{t}")
        self.add_line("pull-top",(32,25),(36,25))
        self.add_arc("pull-tip",(36,25),(36,33),radius_x=4)
        self.add_line("pull-bottom",(36,33),(32,33))
        self.add_line("pull-left-bottom",(32,33),(32,29))
        self.add_line("pull-left-top",(32,29),(32,25))
        self.add_contour("pull","pull-top","pull-tip","pull-bottom","pull-left-bottom","pull-left-top",closed=True)
        for part in ("pull-left-bottom","pull-left-top"):self.relate("connect","zip-2",part)
