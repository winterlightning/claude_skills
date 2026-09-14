# Variant of waterside-fortress; parent file remains unchanged.
'Waterside fortress: independent spacing revision.\n\nEight-unit flag pocket and wider entry spacing; omit tiny base ripple.\nNative solo family, VRECT_XL keyshape. The original model is preserved.\nDirectional and natural asymmetry follows the supplied subject.\nFinal construction review: Original subject render; no exact Lucide match selected.\n'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '110fec5a-d343-43f3-b5f4-126763839e1e'
SOURCE_PATH = 'pictographic-primitives/war/water fortress_110fec5a-d343-43f3-b5f4-126763839e1e.svg'
AUTHOR = 'gpt-6'

class WatersideFortressVariant3(Solo48):
    icon_id = 'waterside-fortress-v3'
    variant_of = 'waterside-fortress'
    variant_label = 'Roomier spacing — remaining review'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/war'
    aliases = ()
    keywords = ('fortress', 'water', 'flag', 'bunker', 'fortification', 'building')

    def build(self):
        self.add_polyline('fort',(8, 44),(8, 32),(20, 20),(26, 20),(32, 20),(40, 28),(40, 44),closed=False)
        self.add_polyline('flag',(26, 20),(26, 12),(26, 4),(38, 4),(34, 12),(26, 12),closed=False)
        self.add_polyline('door',(20, 44),(20, 34),(30, 34),(30, 44),closed=False)
        self.relate('connect','fort','flag')
