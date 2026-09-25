"""SQUARE centerline6,6,42,42. Enlarged star within plate radius18. Tile shares star endpoint33,32; omit tile rows to open internal space."""
from ...keyshapes import Keyshape
from icon_set.model.profiles import Profile
from ._base import Solo48
SOURCE_ICON_ID = '8eb34e8a-c1a0-4770-a3b1-2f00e05fdaef'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_30/pesach passover 2_8eb34e8a-c1a0-4770-a3b1-2f00e05fdaef.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'pesach-passover-2'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ()
    # Keyshape chosen first; stroke centerlines inset 2 from the ink bounds.
    chosen_bounds = Keyshape.SQUARE.bounds_for(Profile.SOLO48)
    def build(self):
        self.add_arc('plate-left',(24,42),(24,6),radius_x=18)
        self.add_bezier('plate-top',(24,6),((31,6),(36,10),(39,15)))
        self.add_contour('plate','plate-left','plate-top')
        self.add_polyline('star',(24,15),(28,19),(33,21),(30,26),(33,32),(24,29),(17,31),(18,26),(15,21),(20,19),closed=True)
        self.add_polyline('tile',(33,32),(42,32),(42,42),(33,42),closed=True)
        self.relate('connect','star','tile')
