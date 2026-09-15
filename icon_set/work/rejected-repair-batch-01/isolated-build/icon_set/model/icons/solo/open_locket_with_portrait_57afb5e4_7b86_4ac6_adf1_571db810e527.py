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
        self.add_arc('front-top', (18, 24), (42, 24), radius_x=12, radius_y=18)
        self.add_arc('front-bottom', (42, 24), (18, 24), radius_x=12, radius_y=18)
        self.add_contour('front', 'front-top', 'front-bottom', closed=True)
        self.add_arc('back-top',(14,8),(6,24),radius_x=8,radius_y=16,sweep=False)
        self.add_arc('back-bottom',(6,24),(14,40),radius_x=8,radius_y=16,sweep=False)
        self.add_contour('back','back-top','back-bottom')
        self.add_line('hinge',(6,24),(18,24))
        self.relate('connect','hinge','back');self.relate('connect','hinge','front')
        self.add_arc('portrait-shoulders', (27,29),(33,29),radius_x=3,radius_y=2)
        self.add_dot('portrait-head', (30,17))
