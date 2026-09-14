# Variant of gaming-keyboard-with-cable; parent file remains unchanged.
'Gaming keyboard with cable: independent spacing revision.\n\nOne roomy row of keys; remove crowded spacebar and steps; retain looped cable.\nNative solo family, SQUARE keyshape. The original model is preserved.\nDirectional and natural asymmetry follows the supplied subject.\nFinal construction review: Original subject render; no exact Lucide match selected.\n'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'a5a55431-2991-499a-9492-ddc2bc86cb9e'
SOURCE_PATH = 'pictographic-primitives/computers/batch-05/keyboard gaming_a5a55431-2991-499a-9492-ddc2bc86cb9e.svg'
AUTHOR = 'gpt-6'

class GamingKeyboardWithCableVariant2(Solo48):
    icon_id = 'gaming-keyboard-with-cable-v2'
    variant_of = 'gaming-keyboard-with-cable'
    variant_label = 'Roomier spacing — remaining review'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/device'
    aliases = ()
    keywords = ('keyboard', 'gaming', 'cable', 'typing', 'input', 'peripheral', 'computer', 'wired')

    def build(self):
        self.add_polyline('case',(6, 24),(24, 24),(42, 24),(42, 42),(6, 42),closed=True)
        self.add_dot('key-left',(16, 33))
        self.add_dot('key-middle',(24, 33))
        self.add_dot('key-right',(32, 33))
        self.add_line('cable-rise',(24, 24),(24, 18))
        self.add_arc('cable-bend',(24, 18),(28, 14),radius_x=4,radius_y=4,sweep=True)
        self.add_line('cable-run',(28, 14),(32, 14))
        self.add_arc('cable-loop',(32, 14),(32, 6),radius_x=4,radius_y=4,sweep=False)
        self.add_line('cable-tip',(32, 6),(20, 6))
        self.add_contour('cable','cable-rise','cable-bend','cable-run','cable-loop','cable-tip',closed=False)
        self.relate('connect','case','cable')
