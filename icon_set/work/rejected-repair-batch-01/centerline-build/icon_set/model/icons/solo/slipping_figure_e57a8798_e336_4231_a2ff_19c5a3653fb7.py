"""slipping-figure: reconstructed from the supplied transportation reference."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e57a8798-e336-4231-a2ff-19c5a3653fb7'
SOURCE_PATH = 'pictographic-primitives/transportation/slippery_e57a8798-e336-4231-a2ff-19c5a3653fb7.svg'
AUTHOR = 'gpt-6'


class SlippingFigure(Solo48):
    icon_id = 'slipping-figure'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "transportation"
    aliases = ()
    keywords = ('slippery', 'slip', 'fall', 'figure', 'warning', 'wet floor', 'caution', 'person')

    def build(self) -> None:

        # The shoulder and hip own the limb junctions; the pose deliberately leans right.
        self.add_arc('head-top',(30,10),(38,10),radius_x=4)
        self.add_arc('head-bottom',(38,10),(30,10),radius_x=4)
        self.add_contour('head','head-top','head-bottom',closed=True)
        self.add_polyline('arms',(10,10),(24,20),(34,26),(42,26))
        self.add_line('torso',(24,20),(18,32))
        self.add_line('back-leg',(18,32),(6,30))
        self.add_polyline('front-leg',(18,32),(28,38),(24,42))
        for part in ['arms-1','arms-2','back-leg','front-leg-1']: self.relate('connect','torso',part)
        self.relate('connect','back-leg','front-leg-1')
