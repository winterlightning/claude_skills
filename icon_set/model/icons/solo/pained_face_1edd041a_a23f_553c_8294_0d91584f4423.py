"""Pained Face; independently reconstructed on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1edd041a-a23f-553c-8294-0d91584f4423'
SOURCE_PATH = 'pictographic-primitives/smileys/ouch_1edd041a-a23f-553c-8294-0d91584f4423.svg'
AUTHOR = 'gpt-6'


class PainedFace(Solo48):
    icon_id = 'pained-face'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "people/emotions"
    aliases = ()
    keywords = ('pain', 'ouch', 'hurt', 'grimace', 'face', 'emoji')

    def build(self) -> None:

        # CIRCLE: center (24,24), centerline radius20, visible radius22.
        axis,radius=24,20
        self.add_arc("head-top",(axis-radius,24),(axis+radius,24),radius_x=radius)
        self.add_arc("head-bottom",(axis+radius,24),(axis-radius,24),radius_x=radius)
        self.add_contour("head","head-top","head-bottom",closed=True)

        self.add_arc("eye-left",(15,17),(19,17),radius_x=3,sweep=False)
        self.add_polyline("eye-right-a",(27,15),(29,17),(31,19))
        self.add_polyline("eye-right-b",(27,19),(29,17),(31,15))
        for a in (1,2):
            for b in (1,2):self.relate("connect",f"eye-right-a-{a}",f"eye-right-b-{b}")

        self.add_arc("mouth-top",(17,32),(31,32),radius_x=7,radius_y=5)
        self.add_arc("mouth-bottom",(31,32),(17,32),radius_x=7,radius_y=3)
        self.add_contour("mouth","mouth-top","mouth-bottom",closed=True)
