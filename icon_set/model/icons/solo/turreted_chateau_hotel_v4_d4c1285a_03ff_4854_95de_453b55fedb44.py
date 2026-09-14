# Variant of turreted-chateau-hotel-v2; parent file remains unchanged.
'Turreted chateau hotel v2: independent spacing revision.\n\nUse the reviewed château roof/arched-entry construction; remove cramped overlapping front turret and eaves.\nNative solo family, HRECT_L keyshape. The original model is preserved.\nDirectional and natural asymmetry follows the supplied subject.\nFinal construction review: Original subject render; no exact Lucide match selected.\n'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'd4c1285a-03ff-4854-95de-453b55fedb44'
SOURCE_PATH = 'pictographic-primitives/landmarks/batch-03/chateau frontenac canada_d4c1285a-03ff-4854-95de-453b55fedb44.svg'
AUTHOR = 'gpt-6'

class LandmarkVariant4(Solo48):
    icon_id = 'turreted-chateau-hotel-v4'
    variant_of = 'turreted-chateau-hotel-v2'
    variant_label = 'Roomier spacing — remaining review'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'places/landmarks'
    aliases = ()
    keywords = ('chateau', 'hotel', 'castle', 'turret', 'quebec', 'canada', 'landmark', 'architecture', 'building')

    def build(self):
        self.add_polyline('outline',(4, 40),(4, 26),(10, 16),(16, 26),(20, 16),(24, 8),(32, 8),(36, 16),(36, 26),(38, 26),(44, 32),(44, 40),(30, 40),(20, 40),closed=True)
        self.add_line('eave',(20, 16),(36, 16))
        self.add_line('door-left',(20, 40),(20, 35))
        self.add_arc('door-top',(20, 35),(30, 35),radius_x=5,radius_y=5,sweep=True)
        self.add_line('door-right',(30, 35),(30, 40))
        self.add_contour('door','door-left','door-top','door-right',closed=False)
        self.relate('connect','outline','eave')
        self.relate('connect','outline','door')
