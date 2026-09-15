"""Smiling Poo; independently reconstructed on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5cca3ad0-53a7-539e-b51f-59df052c4ac7'
SOURCE_PATH = 'pictographic-primitives/smileys/poo funny_5cca3ad0-53a7-539e-b51f-59df052c4ac7.svg'
AUTHOR = 'gpt-6'


class SmilingPoo(Solo48):
    icon_id = 'smiling-poo'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "people/emotions"
    aliases = ()
    keywords = ('poo', 'poop', 'smiling', 'funny', 'face', 'emoji')

    def build(self) -> None:

        # SQUARE extremes x6/42,y6/42. Rounded tiered mound with a curved tip.
        self.add_arc("tip",(24,6),(32,16),radius_x=10)
        self.add_arc("tier-right",(32,16),(40,24),radius_x=8)
        self.add_arc("tier-right-low",(40,24),(38,30),radius_x=8)
        self.add_arc("base-right-top",(38,30),(42,36),radius_x=4,radius_y=6)
        self.add_arc("base-right-bottom",(42,36),(36,42),radius_x=6)
        self.add_line("base",(36,42),(12,42))
        self.add_arc("base-left-bottom",(12,42),(6,36),radius_x=6)
        self.add_arc("base-left-top",(6,36),(10,30),radius_x=4,radius_y=6)
        self.add_arc("tier-left-low",(10,30),(8,24),radius_x=8)
        self.add_arc("tier-left",(8,24),(16,16),radius_x=8)
        self.add_arc("tip-left",(16,16),(24,6),radius_x=10,sweep=False)
        self.add_contour("outline","tip","tier-right","tier-right-low","base-right-top","base-right-bottom","base","base-left-bottom","base-left-top","tier-left-low","tier-left","tip-left",closed=True)
        self.add_dot("eye-left",(18,24))
        self.add_dot("eye-right",(30,24))
        self.add_arc("smile",(20,32),(28,32),radius_x=10,sweep=False)
