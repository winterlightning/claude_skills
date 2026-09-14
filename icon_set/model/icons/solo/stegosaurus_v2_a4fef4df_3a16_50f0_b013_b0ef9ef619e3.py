# Variant of stegosaurus; parent file remains unchanged.
'Stegosaurus: independent spacing revision.\n\nWiden two visible legs and deepen head; preserve three large dorsal plates.\nNative solo family, HRECT_L keyshape. The original model is preserved.\nDirectional and natural asymmetry follows the supplied subject.\nFinal construction review: Original subject render; no exact Lucide match selected.\n'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'a4fef4df-3a16-50f0-b013-b0ef9ef619e3'
SOURCE_PATH = 'pictographic-primitives/animals/dinosaur stegosaurus_a4fef4df-3a16-50f0-b013-b0ef9ef619e3.svg'
AUTHOR = 'gpt-6'

class StegosaurusVariant2(Solo48):
    icon_id = 'stegosaurus-v2'
    variant_of = 'stegosaurus'
    variant_label = 'Roomier spacing — remaining review'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'animals/prehistoric'
    aliases = ()
    keywords = ('stegosaurus', 'dinosaur', 'plates', 'spikes', 'prehistoric', 'jurassic', 'reptile', 'extinct')

    def build(self):
        self.add_polyline('upper',(4, 32),(8, 26),(10, 16),(18, 22),(20, 8),(28, 20),(34, 12),(36, 24),(40, 24),closed=False)
        self.add_arc('brow',(40, 24),(44, 28),radius_x=4,radius_y=4,sweep=True)
        self.add_polyline('lower',(44, 28),(44, 32),(36, 32),(36, 40),(28, 40),(28, 32),(18, 32),(16, 40),(8, 40),(8, 32),(4, 32),closed=False)
        self.contours = [c for c in self.contours if c.contour_id != 'upper']
        self.contours = [c for c in self.contours if c.contour_id != 'lower']
        self.add_contour('body','upper-1','upper-2','upper-3','upper-4','upper-5','upper-6','upper-7','upper-8','brow','lower-1','lower-2','lower-3','lower-4','lower-5','lower-6','lower-7','lower-8','lower-9','lower-10',closed=True)
