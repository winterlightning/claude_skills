"""Propeller plane; authored directly on SOLO48."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'c880fc07-1ef2-4a42-8a1c-f54f78a7842b'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__propeller-plane/20260927T153803Z-thuan-mac-1/reference/propeller_c880fc07-1ef2-4a42-8a1c-f54f78a7842b.svg'
AUTHOR = 'gpt-6'

class PropellerPlane(Solo48):
    icon_id = 'propeller-plane'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'transportation'
    categories = ('transportation', 'primitives')
    aliases = ()
    keywords = ('propeller plane', 'airplane', 'aircraft', 'plane', 'aviation', 'flight', 'light aircraft', 'propeller')

    def build(self) -> None:
        # Three broad propeller blades radiate from one elliptical hub.
        self.add_polyline('blades',(24,20),(10,6),(6,6),(6,12),
                          (18,24),(6,36),(6,42),(12,42),
                          (26,30),(42,14),(42,6),(38,6),closed=True)
        self.add_arc('hub-top',(18,24),(30,24),radius_x=6,radius_y=4,sweep=True)
        self.add_arc('hub-bottom',(30,24),(18,24),radius_x=6,radius_y=4,sweep=True)
        self.add_contour('hub','hub-top','hub-bottom',closed=True)
        self.relate('connect','blades','hub')
