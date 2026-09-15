"""Yawning Face; independently reconstructed on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ca318854-5993-5260-8f07-48b539a5990a'
SOURCE_PATH = 'pictographic-primitives/smileys/yawning face sleepy_ca318854-5993-5260-8f07-48b539a5990a.svg'
AUTHOR = 'gpt-6'


class SleepyYawningFace(Solo48):
    icon_id = 'sleepy-yawning-face'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "people/emotions"
    aliases = ()
    keywords = ('yawn', 'yawning', 'tired', 'sleepy', 'face', 'emoji')

    def build(self) -> None:

        # CIRCLE: visible radius22; shared center (24,24), centerline radius20.
        axis,radius=24,20
        self.add_arc("head-top",(axis-radius,24),(axis+radius,24),radius_x=radius)
        self.add_arc("head-bottom",(axis+radius,24),(axis-radius,24),radius_x=radius)
        self.add_contour("head","head-top","head-bottom",closed=True)

        for side,x in (("left",17),("right",31)):
            self.add_arc(f"eye-{side}",(x-2,17),(x+2,17),radius_x=3,sweep=False)
        self.add_arc("mouth-top",(19,30),(29,30),radius_x=5,radius_y=5)
        for i,(a,b) in enumerate(zip(((29,30),(28,34),(20,34)),((28,34),(20,34),(19,30))),1):self.add_line(f"mouth-bottom-{i}",a,b)
        self.add_contour("mouth","mouth-top","mouth-bottom-1","mouth-bottom-2","mouth-bottom-3",closed=True)
