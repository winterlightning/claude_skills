"""Hazard Warning Triangle, re-authored from its reference on SOLO48."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '4a83aac2-4605-5a65-a8e1-970a1c0682c0'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__hazard-warning-triangle/20260926T172218Z-thuan-mac-1/reference/hazard warning flasher_4a83aac2-4605-5a65-a8e1-970a1c0682c0.svg'
AUTHOR = "gpt-6"

class HazardWarningTriangle(Solo48):
    icon_id = 'hazard-warning-triangle'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "transportation"
    categories = ("transportation", "primitives")
    aliases = ()
    keywords = ('hazard', 'warning triangle', 'emergency', 'hazard lights', 'flasher', 'dashboard', 'car', 'alert')

    def build(self) -> None:
        # Current contract centerline extremes: (6,6)-(42,42).
        self.add_polyline('outer',(24,6),(42,42),(6,42),closed=True)
        self.add_line('alert-stem',(24,29),(24,34))
