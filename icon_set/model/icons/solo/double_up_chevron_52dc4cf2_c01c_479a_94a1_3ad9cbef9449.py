"""Two matching upward chevrons. Square extremes 6..42; shared 18-unit step.
Reference: stacked equal arms; Lucide chevrons-up: two continuous angular runs.
"""
from ._base import Solo48
from ...keyshapes import Keyshape
SOURCE_ICON_ID = '52dc4cf2-c01c-479a-94a1-3ad9cbef9449'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_39/up 1_52dc4cf2-c01c-479a-94a1-3ad9cbef9449.svg'
AUTHOR = "gpt-6-astra"
class DoubleUpChevron(Solo48):
    icon_id = "double-up-chevron-reference-52dc4cf2"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "arrows"
    categories = ("arrows", "primitive", "primitives")
    aliases = ["Double Up Chevron"]
    keywords = ["chevron", "double", "up", "upward", "direction", "navigation"]
    def build(self):
        for i in range(2):
            y = 6 + i*18
            self.add_polyline(f"chevron-{i}", (6,y+18),(24,y),(42,y+18))
