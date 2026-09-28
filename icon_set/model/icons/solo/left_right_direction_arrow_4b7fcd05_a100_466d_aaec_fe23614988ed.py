"""Left and Right Direction Arrow, re-authored from its reference on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '4b7fcd05-a100-466d-aaec-fe23614988ed'
SOURCE_PATH = 'pictographic-primitives/transportation/direction indicators_4b7fcd05-a100-466d-aaec-fe23614988ed.svg'
AUTHOR = 'gpt-6'

class LeftRightDirectionArrow(Solo48):
    icon_id = 'left-right-direction-arrow'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "transportation"
    categories = ("transportation", "primitives")
    aliases = ()
    keywords = ('direction', 'turn signal', 'indicator', 'left', 'right', 'arrow', 'junction', 'dashboard')

    def build(self) -> None:
        # Current contract centerline extremes: (6,8)-(42,40).
        self.add_polyline('outline',(4,20),(12,8),(12,14),(36,14),(36,8),(44,20),(36,32),(36,24),(28,24),(28,40),(20,40),(20,24),(12,24),(12,32),closed=True)
