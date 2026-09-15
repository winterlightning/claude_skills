'Standing giraffe: independent spacing revision.\n\nWiden muzzle, long neck and both visible legs; omit short overlapping tail and horn strokes.\nNative solo family, VRECT_XL keyshape. The original model is preserved.\nDirectional and natural asymmetry follows the supplied subject.\nFinal construction review: Original subject render; no exact Lucide match selected.\n'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '91e66038-39e6-4fde-9641-6dc2916522b9'
SOURCE_PATH = 'pictographic-primitives/animals/giraffe body_91e66038-39e6-4fde-9641-6dc2916522b9.svg'
AUTHOR = 'gpt-6'

class StandingGiraffe(Solo48):
    icon_id = 'standing-giraffe'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'animals'
    aliases = ()
    keywords = ('giraffe', 'standing', 'neck', 'tall', 'animal', 'safari', 'zoo', 'africa')

    def build(self):
        self.add_polyline('rear-back',(8, 44),(8, 30),(18, 30),closed=False)
        self.add_arc('shoulder',(18, 30),(22, 26),radius_x=4,radius_y=4,sweep=False)
        self.add_polyline('neck-head',(22, 26),(24, 8),(24, 4),(32, 4),(32, 8),(40, 16),(40, 26),(32, 24),(32, 44),(24, 44),(24, 38),(16, 38),(16, 44),(8, 44),closed=False)
        self.contours = [c for c in self.contours if c.contour_id != 'rear-back']
        self.contours = [c for c in self.contours if c.contour_id != 'neck-head']
        self.add_contour('body','rear-back-1','rear-back-2','shoulder','neck-head-1','neck-head-2','neck-head-3','neck-head-4','neck-head-5','neck-head-6','neck-head-7','neck-head-8','neck-head-9','neck-head-10','neck-head-11','neck-head-12','neck-head-13',closed=True)
