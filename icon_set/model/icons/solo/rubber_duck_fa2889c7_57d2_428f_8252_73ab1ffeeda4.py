'Rubber duck: independent spacing revision.\n\nEight-unit bill and broad tail/body opening, using the reviewed bath-duck construction.\nNative solo family, HRECT_L keyshape. The original model is preserved.\nDirectional and natural asymmetry follows the supplied subject.\nFinal construction review: Original subject render; no exact Lucide match selected.\n'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'fa2889c7-57d2-428f-8252-73ab1ffeeda4'
SOURCE_PATH = 'pictographic-primitives/babies/toy yellow duck_fa2889c7-57d2-428f-8252-73ab1ffeeda4.svg'
AUTHOR = 'gpt-6'

class RubberDuck(Solo48):
    icon_id = 'rubber-duck'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/baby'
    aliases = ()
    keywords = ('rubber', 'duck', 'baby', 'nursery', 'toy')

    def build(self):
        self.add_arc('head-top',(10, 18),(20, 8),radius_x=10,radius_y=10,sweep=True)
        self.add_arc('head-back',(20, 8),(30, 18),radius_x=10,radius_y=10,sweep=True)
        self.add_arc('neck',(30, 18),(26, 26),radius_x=10,radius_y=10,sweep=True)
        self.add_arc('back',(26, 26),(44, 23),radius_x=22,radius_y=12,sweep=False)
        self.add_line('tail',(44, 23),(44, 26))
        self.add_arc('body-right',(44, 26),(32, 40),radius_x=12,radius_y=14,sweep=True)
        self.add_line('belly',(32, 40),(22, 40))
        self.add_arc('body-left',(22, 40),(10, 28),radius_x=12,radius_y=12,sweep=True)
        self.add_polyline('bill',(10, 28),(13, 26),(4, 26),(4, 18),(10, 18),closed=False)
        self.contours = [c for c in self.contours if c.contour_id != 'bill']
        self.add_contour('body','head-top','head-back','neck','back','tail','body-right','belly','body-left','bill-1','bill-2','bill-3','bill-4',closed=True)
