# Variant of grappling-wrestlers; parent file remains unchanged.
'Grappling wrestlers: independent spacing revision.\n\nEnlarge paired heads and separate inside legs to eight units.\nNative solo family, SQUARE keyshape. The original model is preserved.\nDirectional and natural asymmetry follows the supplied subject.\nFinal construction review: Original subject render; no exact Lucide match selected.\n'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '1edbcccc-38d4-50b3-97fd-c3c787148861'
SOURCE_PATH = 'pictographic-primitives/sports/wrestling fight_1edbcccc-38d4-50b3-97fd-c3c787148861.svg'
AUTHOR = 'gpt-6'

class GrapplingWrestlersVariant2(Solo48):
    icon_id = 'grappling-wrestlers-v2'
    variant_of = 'grappling-wrestlers'
    variant_label = 'Roomier spacing — remaining review'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/sports'
    aliases = ()
    keywords = ('grappling', 'wrestlers', 'sport')

    def build(self):
        self.add_arc('head-lefta',(11, 10),(19, 10),radius_x=4,radius_y=4)
        self.add_arc('head-leftb',(19, 10),(11, 10),radius_x=4,radius_y=4)
        self.add_contour('head-left','head-lefta','head-leftb',closed=True)
        self.add_arc('head-righta',(29, 10),(37, 10),radius_x=4,radius_y=4)
        self.add_arc('head-rightb',(37, 10),(29, 10),radius_x=4,radius_y=4)
        self.add_contour('head-right','head-righta','head-rightb',closed=True)
        self.add_polyline('left-body',(6, 42),(12, 32),(15, 23),closed=False)
        self.add_polyline('left-leg',(12, 32),(20, 36),(20, 42),closed=False)
        self.add_polyline('right-body',(42, 42),(36, 32),(33, 23),closed=False)
        self.add_polyline('right-leg',(36, 32),(28, 36),(28, 42),closed=False)
        self.add_polyline('arms',(15, 23),(24, 29),(33, 23),closed=False)
        self.relate('connect','left-body','left-leg')
        self.relate('connect','right-body','right-leg')
        self.relate('connect','arms','left-body')
        self.relate('connect','arms','right-body')
