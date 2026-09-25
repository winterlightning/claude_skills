'Standing hyena: independent spacing revision.\n\nEight-unit legs and deeper muzzle retain the high-shouldered profile; remove tiny tail loop.\nNative solo family, HRECT_L keyshape. The original model is preserved.\nDirectional and natural asymmetry follows the supplied subject.\nFinal construction review: Original subject render; no exact Lucide match selected.\n'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '24a9c868-e028-5cb9-abe7-46d997efd4de'
SOURCE_PATH = 'pictographic-primitives/animals/hyena_24a9c868-e028-5cb9-abe7-46d997efd4de.svg'
AUTHOR = 'gpt-6'

class StandingHyena(Solo48):
    icon_id = 'standing-hyena'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'animals'
    aliases = ()
    keywords = ('hyena', 'standing', 'body', 'profile', 'animal', 'wildlife', 'africa', 'scavenger')

    def build(self):
        self.add_arc('rump',(4, 28),(14, 18),radius_x=10,radius_y=10,sweep=True)
        self.add_polyline('back-head',(14, 18),(30, 14),(34, 8),(38, 16),(44, 20),(44, 28),(36, 26),(32, 32),closed=False)
        self.add_polyline('foreleg',(32, 32),(32, 40),(24, 40),(24, 30),closed=False)
        self.add_line('belly',(24, 30),(12, 30))
        self.add_polyline('hindleg',(12, 30),(12, 40),(4, 40),(4, 28),closed=False)
        self.contours = [c for c in self.contours if c.contour_id != 'back-head']
        self.contours = [c for c in self.contours if c.contour_id != 'foreleg']
        self.contours = [c for c in self.contours if c.contour_id != 'hindleg']
        self.add_contour('body','rump','back-head-1','back-head-2','back-head-3','back-head-4','back-head-5','back-head-6','back-head-7','foreleg-1','foreleg-2','foreleg-3','belly','hindleg-1','hindleg-2','hindleg-3',closed=True)
