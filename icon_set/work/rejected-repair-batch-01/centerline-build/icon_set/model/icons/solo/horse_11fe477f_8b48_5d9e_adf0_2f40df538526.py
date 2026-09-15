'Horse: independent spacing revision.\n\nWiden both legs and muzzle; remove the overlapping secondary tail outline.\nNative solo family, SQUARE keyshape. The original model is preserved.\nDirectional and natural asymmetry follows the supplied subject.\nFinal construction review: Original subject render; no exact Lucide match selected.\n'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '11fe477f-8b48-5d9e-adf0-2f40df538526'
SOURCE_PATH = 'pictographic-primitives/animals/symbol cavalry_11fe477f-8b48-5d9e-adf0-2f40df538526.svg'
AUTHOR = 'gpt-6'

class Horse(Solo48):
    icon_id = 'horse'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'animals'
    aliases = ()
    keywords = ('horse', 'pony', 'stallion', 'equine', 'cavalry', 'animal', 'riding', 'profile')

    def build(self):
        self.add_polyline('head',(30, 14),(34, 6),(42, 18),(42, 28),(34, 24),(34, 32),closed=False)
        self.add_arc('chest',(34, 32),(32, 34),radius_x=2,radius_y=2,sweep=True)
        self.add_polyline('front-leg',(32, 34),(32, 42),(24, 42),(24, 32),closed=False)
        self.add_line('belly',(24, 32),(14, 32))
        self.add_polyline('rear-leg',(14, 32),(14, 42),(6, 42),(6, 30),closed=False)
        self.add_arc('rump',(6, 30),(16, 20),radius_x=10,radius_y=10,sweep=True)
        self.add_line('back',(16, 20),(24, 20))
        self.add_arc('neck',(24, 20),(30, 14),radius_x=6,radius_y=6,sweep=False)
        self.contours = [c for c in self.contours if c.contour_id != 'head']
        self.contours = [c for c in self.contours if c.contour_id != 'front-leg']
        self.contours = [c for c in self.contours if c.contour_id != 'rear-leg']
        self.add_contour('body','head-1','head-2','head-3','head-4','head-5','chest','front-leg-1','front-leg-2','front-leg-3','belly','rear-leg-1','rear-leg-2','rear-leg-3','rump','back','neck',closed=False)
