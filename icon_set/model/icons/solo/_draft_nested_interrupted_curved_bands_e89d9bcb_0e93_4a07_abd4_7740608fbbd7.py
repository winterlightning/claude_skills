"""Nested interrupted curved bands, asymmetric sweep to the upper right.
HRECT_L extremes (4,8)-(44,40). Four cubic strokes own the two interrupted
curves, preserving the slanted break. Source ribbon taper is omitted in this
constant-stroke experiment. Native identity must be checked before release.

Review: valid with zero warnings; visual identity unresolved. Do not export.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'e89d9bcb-0e93-4a07-abd4-7740608fbbd7'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_13/crowdin logo_e89d9bcb-0e93-4a07-abd4-7740608fbbd7.svg'
AUTHOR = 'gpt-6-astra'
class Drawing(Solo48):
    icon_id = 'nested-interrupted-curved-bands'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ('Triple Curved Arcs Symbol',)
    keywords = ('arcs','bands','curves','symbol','nested','abstract','mark')
    def build(self):
        self.add_bezier('outer-top',(44,8),((22,8),(8,8),(4,20)))
        self.add_bezier('outer-bottom',(4,28),((4,36),(10,40),(24,40)))
        self.add_bezier('inner-top',(44,18),((34,18),(28,18),(24,24)))
        self.add_bezier('inner-bottom',(28,32),((28,34),(34,34),(40,34)))
