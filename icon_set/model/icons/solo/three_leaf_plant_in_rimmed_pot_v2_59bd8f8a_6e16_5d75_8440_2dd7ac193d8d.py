# Variant of three-leaf-plant-in-rimmed-pot; parent file remains unchanged.
'Three leaf plant in rimmed pot: independent spacing revision.\n\nThree broad pointed leaves without cramped seams; eight-unit rim and pot depth.\nNative solo family, VRECT_XL keyshape. The original model is preserved.\nDirectional and natural asymmetry follows the supplied subject.\nFinal construction review: sprout: broad leaf silhouettes around a central stem. Local Lucide originals and atomic-debug renders were inspected.\n'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '59bd8f8a-6e16-5d75-8440-2dd7ac193d8d'
SOURCE_PATH = 'pictographic-primitives/decoration/batch-03/indoor plant_59bd8f8a-6e16-5d75-8440-2dd7ac193d8d.svg'
AUTHOR = 'gpt-6'

class ThreeLeafPlantInRimmedPotVariant2(Solo48):
    icon_id = 'three-leaf-plant-in-rimmed-pot-v2'
    variant_of = 'three-leaf-plant-in-rimmed-pot'
    variant_label = 'Roomier spacing — remaining review'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'nature/plants'
    aliases = ()
    keywords = ('plant', 'decoration', 'foliage', 'indoor')

    def build(self):
        self.add_polyline('foliage',(16, 28),(8, 20),(8, 8),(18, 14),(24, 4),(30, 14),(40, 8),(40, 20),(32, 28),closed=False)
        self.add_polyline('rim',(12, 28),(16, 28),(32, 28),(36, 28),(36, 36),(32, 36),(16, 36),(12, 36),closed=True)
        self.add_polyline('pot',(16, 36),(18, 44),(30, 44),(32, 36),closed=False)
        self.relate('connect','foliage','rim')
        self.relate('connect','rim','pot')
