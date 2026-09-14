'Skunk: independent spacing revision.\n\nRebalanced geometry for eight-unit straight spacing and clear curved openings.\nNative solo family, HRECT_XL keyshape. The original model is preserved.\nDirectional and natural asymmetry follows the supplied subject.\nFinal construction review: Original subject render; no exact Lucide match selected.\n'
# Variant of skunk; parent file remains unchanged.
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'c747f16a-3172-497d-9495-75b5f73d5aba'
SOURCE_PATH = 'pictographic-primitives/animals/skunk_c747f16a-3172-497d-9495-75b5f73d5aba.svg'
AUTHOR = 'gpt-6'

class SkunkVariant2(Solo48):
    icon_id = 'skunk-v2'
    variant_of = 'skunk'
    variant_label = 'Roomier spacing — remaining review'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'nature/animals'
    aliases = ()
    keywords = ('skunk', 'tail', 'bushy', 'stripe', 'animal', 'wildlife', 'spray', 'nocturnal')

    def build(self):
        self.add_arc('tail-top',(4, 18),(24, 18),radius_x=10,radius_y=10,sweep=True)
        self.add_arc('tail-turn',(24, 18),(20, 24),radius_x=10,radius_y=10,sweep=True)
        self.add_polyline('body',(20, 24),(32, 24),(36, 16),(44, 24),(44, 32),(40, 32),(40, 40),(32, 40),(32, 32),(20, 32),(20, 40),(12, 40),(12, 30),(12, 24),(4, 18),closed=False)
        self.contours = [c for c in self.contours if c.contour_id != 'body']
        self.add_contour('outline','tail-top','tail-turn','body-1','body-2','body-3','body-4','body-5','body-6','body-7','body-8','body-9','body-10','body-11','body-12','body-13','body-14',closed=True)
