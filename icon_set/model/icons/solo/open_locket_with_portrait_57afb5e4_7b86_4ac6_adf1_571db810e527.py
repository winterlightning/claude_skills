'Open portrait locket: preserve its overlapping oval covers and a small round-headed bust with exact four-unit head-to-shoulder clearance.'
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
        self.add_arc('front-top', (14,24), (42,24), radius_x=14, radius_y=18)
        self.add_arc('front-bottom', (42,24), (14,24), radius_x=14, radius_y=18)
        self.add_contour('front', 'front-top', 'front-bottom', closed=True)

        self.add_bezier('back',(28,6),((14,6),(6,12),(6,24)),((6,36),(14,42),(28,42)))
        self.relate('connect','front','back')
        # Shared user reference: round head bottom21, shoulder top29 gives exact4-unit ink gap.

        self.add_arc('portrait-head-top', (25,18), (31,18), radius_x=3, radius_y=3)
        self.add_arc('portrait-head-bottom', (31,18), (25,18), radius_x=3, radius_y=3)
        self.add_contour('portrait-head', 'portrait-head-top', 'portrait-head-bottom', closed=True)

        self.add_arc('portrait-shoulders',(24,31),(32,31),radius_x=4,radius_y=2)
