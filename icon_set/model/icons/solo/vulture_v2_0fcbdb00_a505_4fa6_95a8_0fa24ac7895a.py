# Variant of vulture; parent file remains unchanged.
'Vulture: independent spacing revision.\n\nBroaden hooked head and wing; keep one clear supporting leg.\nNative solo family, VRECT_L keyshape. The original model is preserved.\nDirectional and natural asymmetry follows the supplied subject.\nFinal construction review: bird: simplified body, open supporting limbs. Local Lucide originals and atomic-debug renders were inspected.\n'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '0fcbdb00-a505-4fa6-95a8-0fa24ac7895a'
SOURCE_PATH = 'pictographic-primitives/animals/wild bird vulture_0fcbdb00-a505-4fa6-95a8-0fa24ac7895a.svg'
AUTHOR = 'gpt-6'

class VultureVariant2(Solo48):
    icon_id = 'vulture-v2'
    variant_of = 'vulture'
    variant_label = 'Roomier spacing — remaining review'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'animals/birds'
    aliases = ()
    keywords = ('vulture', 'scavenger', 'bird', 'neck', 'beak', 'standing', 'carrion', 'wildlife')

    def build(self):
        self.add_arc('crown',(24, 12),(40, 12),radius_x=8,radius_y=8,sweep=True)
        self.add_polyline('neck',(40, 12),(40, 20),(32, 20),(32, 24),closed=False)
        self.add_arc('throat',(32, 24),(24, 32),radius_x=8,radius_y=8,sweep=True)
        self.add_polyline('wing',(24, 32),(8, 40),(12, 24),(18, 20),(24, 24),(24, 12),closed=False)
        self.contours = [c for c in self.contours if c.contour_id != 'neck']
        self.contours = [c for c in self.contours if c.contour_id != 'wing']
        self.add_contour('body','crown','neck-1','neck-2','neck-3','throat','wing-1','wing-2','wing-3','wing-4','wing-5',closed=True)
        self.add_polyline('leg',(22, 33),(26, 44),(36, 44),closed=False)
        self.relate('connect','body','leg')
