"""Occupant with Deployed Airbag, re-authored from its reference on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '7b81e3fe-4b85-4035-b8ba-bae64863f57a'
SOURCE_PATH = 'pictographic-primitives/transportation/front airbag_7b81e3fe-4b85-4035-b8ba-bae64863f57a.svg'
AUTHOR = 'gpt-6'

class OccupantDeployedAirbag(Solo48):
    icon_id = 'occupant-deployed-airbag'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/transportation"
    aliases = ()
    keywords = ('airbag', 'front airbag', 'safety', 'occupant', 'car', 'dashboard', 'passenger', 'srs')

    def build(self) -> None:
        # Current contract centerline extremes: (6,8)-(42,40).
        self.add_arc('airbag-a',(12,8),(12,24),radius_x=8)
        self.add_arc('airbag-b',(12,24),(12,8),radius_x=8)
        self.add_contour('airbag','airbag-a','airbag-b',closed=True)
        self.add_arc('head-a',(36,8),(36,14),radius_x=3)
        self.add_arc('head-b',(36,14),(36,8),radius_x=3)
        self.add_contour('head','head-a','head-b',closed=True)
        self.add_polyline('seated-body',(42,22),(30,40),(16,34),(12,40))
