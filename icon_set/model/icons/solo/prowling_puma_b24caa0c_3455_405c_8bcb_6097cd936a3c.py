'Prowling puma: independent spacing revision.\n\nWiden near legs and simplify overlapping rear contour; keep low feline pose.\nNative solo family, HRECT_L keyshape. The original model is preserved.\nDirectional and natural asymmetry follows the supplied subject.\nFinal construction review: Original subject render; no exact Lucide match selected.\n'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'b24caa0c-3455-405c-8bcb-6097cd936a3c'
SOURCE_PATH = 'pictographic-primitives/animals/puma_b24caa0c-3455-405c-8bcb-6097cd936a3c.svg'
AUTHOR = 'gpt-6'

class ProwlingPuma(Solo48):
    icon_id = 'prowling-puma'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'animals'
    aliases = ('cougar', 'mountain-lion')
    keywords = ('puma', 'cougar', 'mountain lion', 'prowl', 'big cat', 'feline', 'stalk', 'wildlife')

    def build(self):
        self.add_polyline('upper',(4, 20),(4, 14),(8, 8),(14, 14),(30, 14),closed=False)
        self.add_arc('rump',(30, 14),(44, 28),radius_x=14,radius_y=14,sweep=True)
        self.add_polyline('lower',(44, 28),(44, 40),(36, 40),(36, 28),(20, 28),(14, 40),(4, 40),(12, 24),(4, 20),closed=False)
        self.contours = [c for c in self.contours if c.contour_id != 'upper']
        self.contours = [c for c in self.contours if c.contour_id != 'lower']
        self.add_contour('body','upper-1','upper-2','upper-3','upper-4','rump','lower-1','lower-2','lower-3','lower-4','lower-5','lower-6','lower-7','lower-8',closed=True)
