# Variant of leaping-rabbit; parent file remains unchanged.
'Leaping rabbit: independent spacing revision.\n\nOpen long ear and rear foot instead of tight doubled returns; retain leaping pose and dot tail.\nNative solo family, SQUARE keyshape. The original model is preserved.\nDirectional and natural asymmetry follows the supplied subject.\nFinal construction review: Original subject render; no exact Lucide match selected.\n'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '5a74fdf4-e500-5569-9d8c-fa2c1fe5ad69'
SOURCE_PATH = 'pictographic-primitives/animals/rabbit running_5a74fdf4-e500-5569-9d8c-fa2c1fe5ad69.svg'
AUTHOR = 'gpt-6'

class LeapingRabbitVariant3(Solo48):
    icon_id = 'leaping-rabbit-v3'
    variant_of = 'leaping-rabbit'
    variant_label = 'Roomier spacing — remaining review'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'nature/animals'
    aliases = ('running-rabbit',)
    keywords = ('rabbit', 'bunny', 'leap', 'run', 'hop', 'fast', 'hare', 'motion')

    def build(self):
        self.add_arc('rump',(6, 28),(16, 18),radius_x=10,radius_y=10,sweep=True)
        self.add_line('back',(16, 18),(26, 24))
        self.add_arc('shoulder',(26, 24),(32, 18),radius_x=6,radius_y=6,sweep=False)
        self.add_polyline('head',(32, 18),(42, 18),(42, 30),(34, 30),(30, 34),closed=False)
        self.contours = [c for c in self.contours if c.contour_id != 'head']
        self.add_contour('outline','rump','back','shoulder','head-1','head-2','head-3','head-4',closed=False)
        self.add_line('ear',(32, 18),(22, 6))
        self.relate('connect','ear','outline')
        self.add_arc('belly',(6, 28),(14, 36),radius_x=8,radius_y=8,sweep=False)
        self.add_polyline('foot',(14, 36),(22, 42),(36, 42),closed=False)
        self.contours = [c for c in self.contours if c.contour_id != 'foot']
        self.add_contour('lower','belly','foot-1','foot-2',closed=False)
        self.relate('connect','lower','outline')
        self.add_dot('tail',(6, 12))
