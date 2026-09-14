# Variant of gem-with-jewellers-pliers; parent file remains unchanged.
'Gem with jewellers pliers: independent spacing revision.\n\nDeepen upper facet; remove tiny joint ring and post.\nNative solo family, VRECT_L keyshape. The original model is preserved.\nDirectional and natural asymmetry follows the supplied subject.\nFinal construction review: Original subject render; no exact Lucide match selected.\n'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'd972d9b1-2bc7-4822-b298-6de6a612c2ea'
SOURCE_PATH = 'pictographic-primitives/accessories/batch-06/jewelry maker_d972d9b1-2bc7-4822-b298-6de6a612c2ea.svg'
AUTHOR = 'gpt-6'

class GemWithJewellersPliersVariant2(Solo48):
    icon_id = 'gem-with-jewellers-pliers-v2'
    variant_of = 'gem-with-jewellers-pliers'
    variant_label = 'Roomier spacing — remaining review'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/accessories'
    aliases = ()
    keywords = ('gem', 'with', 'jewellers', 'pliers')

    def build(self):
        self.add_polyline('gem',(8, 12),(14, 4),(34, 4),(40, 12),(24, 22),closed=True)
        self.add_line('facet',(8, 12),(40, 12))
        self.relate('connect','gem','facet')
        self.add_polyline('left',(11, 44),(15, 31),(24, 39),closed=False)
        self.add_polyline('right',(37, 44),(33, 31),(24, 39),closed=False)
        self.relate('connect','left','right')
