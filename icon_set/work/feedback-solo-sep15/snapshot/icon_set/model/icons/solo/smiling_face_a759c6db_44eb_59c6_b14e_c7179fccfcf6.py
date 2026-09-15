"""Smiling Face; independently reconstructed on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a759c6db-44eb-59c6-b14e-c7179fccfcf6'
SOURCE_PATH = 'pictographic-primitives/smileys/smile face_a759c6db-44eb-59c6-b14e-c7179fccfcf6.svg'
AUTHOR = 'gpt-6'


class SmilingFace(Solo48):
    icon_id = 'smiling-face'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "people/emotions"
    aliases = ()
    keywords = ('smile', 'happy', 'smiling', 'cheerful', 'face', 'emoji')

    def build(self) -> None:

        # CIRCLE: visible radius22; shared center (24,24), centerline radius20.
        axis,radius=24,20
        self.add_arc("head-top",(axis-radius,24),(axis+radius,24),radius_x=radius)
        self.add_arc("head-bottom",(axis+radius,24),(axis-radius,24),radius_x=radius)
        self.add_contour("head","head-top","head-bottom",closed=True)

        for side,x in (("left",16),("right",32)):
            self.add_line(f"eye-{side}",(x,17),(x,19))
        self.add_arc("smile",(15,27),(33,27),radius_x=11,sweep=False)
