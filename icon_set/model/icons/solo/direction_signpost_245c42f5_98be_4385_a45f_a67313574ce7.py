"""Direction Signpost, rebuilt from the supplied reference on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '245c42f5-98be-4385-a45f-a67313574ce7'
SOURCE_PATH = 'pictographic-primitives/transportation/crossroad_245c42f5-98be-4385-a45f-a67313574ce7.svg'
AUTHOR = 'gpt-6'

class DirectionSignpost(Solo48):
    icon_id = 'direction-signpost'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'transportation'
    aliases = ()
    keywords = ('signpost', 'direction', 'crossroad', 'wayfinding', 'sign', 'road', 'junction', 'navigation')

    def build(self) -> None:
        # Height repair: exact SOLO48 keyshape extremes; original subject and stroke retained.
        self.add_polyline('upper-board', (12, 4), (34, 4), (40, 10), (34, 16), (24, 16), (12, 16), closed=True)
        self.add_polyline('lower-board', (14, 24), (24, 24), (40, 24), (40, 36), (24, 36), (14, 36), (8, 30), closed=True)
        self.add_line('post-middle', (24, 16), (24, 24))
        self.add_line('post-bottom', (24, 36), (24, 44))
        self.relate('connect', 'post-middle', 'upper-board')
        self.relate('connect', 'post-middle', 'lower-board')
        self.relate('connect', 'post-bottom', 'lower-board')
