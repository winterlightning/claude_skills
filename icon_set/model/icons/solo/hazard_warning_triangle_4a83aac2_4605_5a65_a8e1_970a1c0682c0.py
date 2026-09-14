"""Hazard Warning Triangle, re-authored from its reference on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '4a83aac2-4605-5a65-a8e1-970a1c0682c0'
SOURCE_PATH = 'pictographic-primitives/transportation/hazard warning flasher_4a83aac2-4605-5a65-a8e1-970a1c0682c0.svg'
AUTHOR = 'gpt-6'

class HazardWarningTriangle(Solo48):
    icon_id = 'hazard-warning-triangle'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/transportation"
    aliases = ()
    keywords = ('hazard', 'warning triangle', 'emergency', 'hazard lights', 'flasher', 'dashboard', 'car', 'alert')

    def build(self) -> None:
        # Current contract centerline extremes: (6,6)-(42,42).
        self.add_polyline('outer',(24,6),(42,42),(6,42),closed=True)
