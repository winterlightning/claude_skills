"""Kidney-shaped paint palette. SQUARE extremes6,6,42,42. Lucide palette informs organic notch and separate paint wells."""
from ...keyshapes import Keyshape
from icon_set.model.profiles import Profile
from ._base import Solo48
SOURCE_ICON_ID = 'd3ea8f6b-49cc-4787-9672-77eeeeac6b7b'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_29/palate_d3ea8f6b-49cc-4787-9672-77eeeeac6b7b.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'palate'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ()
    # Keyshape chosen first; stroke centerlines inset 2 from the ink bounds.
    chosen_bounds = Keyshape.SQUARE.bounds_for(Profile.SOLO48)
    def build(self):
        # Organic kidney contour with clear lower-right notch; two separated paint-well circles.
        self.add_bezier('outline',(24,6),((34,6),(42,12),(42,22)),((42,28),(38,30),(34,30)),((30,30),(36,42),(26,42)),((14,42),(6,36),(6,25)),((6,14),(14,6),(24,6)))
        self.add_contour('palette','outline',closed=True)
        self.add_arc('well-upper-a',(22,17),(26,17),radius_x=2)
        self.add_arc('well-upper-b',(26,17),(22,17),radius_x=2)
        self.add_contour('well-upper','well-upper-a','well-upper-b',closed=True)
        self.add_arc('well-left-a',(16,29),(20,29),radius_x=2)
        self.add_arc('well-left-b',(20,29),(16,29),radius_x=2)
        self.add_contour('well-left','well-left-a','well-left-b',closed=True)
