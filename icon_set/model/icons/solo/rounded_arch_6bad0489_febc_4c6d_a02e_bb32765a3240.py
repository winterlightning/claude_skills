"""An open arch with equal vertical legs and tangent semicircular crown.
Square envelope 6..42; reflection about x=24. No useful Lucide arch match.
Reference supplies the broad crown and open level endpoints, no animal parts.
"""
from ._base import Solo48
from ...keyshapes import Keyshape
SOURCE_ICON_ID = '6bad0489-febc-4c6d-a02e-bb32765a3240'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_39/walrus_6bad0489-febc-4c6d-a02e-bb32765a3240.svg'
AUTHOR = "gpt-6-astra"
class RoundedArch(Solo48):
    icon_id = "rounded-arch"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ["Rounded Arch", "Set Intersection Symbol"]
    keywords = ["arch", "curve", "shape", "inverted", "u", "symbol"]
    def build(self):
        self.add_line("left-leg", (6,42),(6,24))
        self.add_arc("crown", (6,24),(42,24),radius_x=18,sweep=True)
        self.add_line("right-leg",(42,24),(42,42))
        self.add_contour("arch","left-leg","crown","right-leg")
