# Variant of seal-balancing-ball; parent file remains unchanged.
'Seal balancing ball: independent spacing revision.\n\nRebalanced geometry for eight-unit straight spacing and clear curved openings.\nNative solo family, SQUARE keyshape. The original model is preserved.\nDirectional and natural asymmetry follows the supplied subject.\nFinal construction review: Original subject render; no exact Lucide match selected.\n'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '51d0c88f-615f-440d-bdfa-7172f9404ea7'
SOURCE_PATH = 'pictographic-primitives/animals/seal ball_51d0c88f-615f-440d-bdfa-7172f9404ea7.svg'
AUTHOR = 'gpt-6'

class SealBalancingBallVariant2(Solo48):
    icon_id = 'seal-balancing-ball-v2'
    variant_of = 'seal-balancing-ball'
    variant_label = 'Roomier spacing — remaining review'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'animals/marine'
    aliases = ()
    keywords = ('seal', 'ball', 'balance', 'circus', 'sea lion', 'trick', 'show', 'marine')

    def build(self):
        self.add_arc('ball-right',(12, 6),(12, 18),radius_x=6,radius_y=6,sweep=True)
        self.add_arc('ball-left',(12, 18),(12, 6),radius_x=6,radius_y=6,sweep=True)
        self.add_contour('ball','ball-right','ball-left',closed=True)
        self.add_arc('chest',(12, 18),(22, 28),radius_x=10,radius_y=10,sweep=True)
        self.add_polyline('back',(22, 28),(22, 30),(34, 34),(42, 28),(42, 42),(12, 42),closed=False)
        self.add_arc('rump',(12, 42),(6, 36),radius_x=6,radius_y=6,sweep=True)
        self.add_line('left',(6, 36),(6, 28))
        self.add_arc('head',(6, 28),(12, 18),radius_x=6,radius_y=10,sweep=True)
        self.contours = [c for c in self.contours if c.contour_id != 'back']
        self.add_contour('body','chest','back-1','back-2','back-3','back-4','back-5','rump','left','head',closed=True)
        self.relate('connect','ball','body')
