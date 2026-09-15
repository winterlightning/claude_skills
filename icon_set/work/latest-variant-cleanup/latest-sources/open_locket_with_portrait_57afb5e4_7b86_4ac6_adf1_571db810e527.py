"""Simplify the locket portrait to a dot head and one shoulder curve; retain both hinged halves. Independent feedback revision; parent preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '57afb5e4-7b86-4ac6-adf1-571db810e527'
SOURCE_PATH = 'pictographic-primitives/accessories/batch-07/locket_57afb5e4-7b86-4ac6-adf1-571db810e527.svg'
AUTHOR = 'gpt-6'

class OpenLocketWithPortrait(Solo48):
    icon_id = 'open-locket-with-portrait'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/accessories'
    aliases = ()
    keywords = ('open', 'locket', 'with', 'portrait')

    def build(self) -> None:
        """Symbol plan: Simplify the locket portrait to a dot head and one shoulder curve; retain both hinged halves. Reference: inspected current parent; no useful exact Lucide match selected."""
        self.add_arc('front-top', (14, 24), (42, 24), radius_x=14, radius_y=18)
        self.add_arc('front-bottom', (42, 24), (14, 24), radius_x=14, radius_y=18)
        self.add_contour('front', 'front-top', 'front-bottom', closed=True)
        self.add_bezier('back', (28, 6), ((14, 6), (6, 12), (6, 24)), ((6, 36), (14, 42), (28, 42)))
        self.relate('connect', 'front', 'back')
        self.add_arc('portrait-shoulders', (24, 31), (32, 31), radius_x=4, radius_y=2)
        self.add_dot('portrait-head', (28, 18))
