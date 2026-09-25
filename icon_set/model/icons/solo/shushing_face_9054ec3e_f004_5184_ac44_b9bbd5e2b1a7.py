"""Shushing Face; independently reconstructed on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9054ec3e-f004-5184-ac44-b9bbd5e2b1a7'
SOURCE_PATH = 'pictographic-primitives/smileys/shushing face quiet silent_9054ec3e-f004-5184-ac44-b9bbd5e2b1a7.svg'
AUTHOR = 'gpt-6'


class ShushingFace(Solo48):
    icon_id = 'shushing-face'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "smileys"
    aliases = ()
    keywords = ('shushing', 'quiet', 'silent', 'finger', 'face', 'emoji')

    def build(self) -> None:

        # SQUARE (4,4)-(44,44): index finger conceals the mouth and lower head.
        self.add_arc("head",(6,24),(42,24),radius_x=18)
        for side,x in (("left",18),("right",30)):
            self.add_arc(f"eye-{side}",(x-1,17),(x+1,17),radius_x=2)
        self.add_line("finger-left",(20,34),(20,29))
        self.add_arc("fingertip",(20,29),(28,29),radius_x=4)
        self.add_line("finger-right",(28,29),(28,34))
        self.add_line("knuckles-top",(28,34),(32,34))
        self.add_arc("knuckles",(32,34),(36,38),radius_x=4)
        self.add_arc("palm-right",(36,38),(32,42),radius_x=4)
        self.add_line("palm-bottom",(32,42),(16,42))
        self.add_line("palm-left",(16,42),(16,34))
        self.add_line("thumb",(16,34),(20,34))
        self.add_contour("hand","finger-left","fingertip","finger-right","knuckles-top","knuckles","palm-right","palm-bottom","palm-left","thumb",closed=True)
