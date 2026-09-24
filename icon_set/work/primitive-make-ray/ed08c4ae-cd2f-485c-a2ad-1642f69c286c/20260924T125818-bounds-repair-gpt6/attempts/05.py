"""Arduino infinity with minus and plus. HRECT_M centerline extremes (4,10)-(44,38). Cubic lobes follow Lucide infinity coherent flow."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.profiles import Profile
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'ed08c4ae-cd2f-485c-a2ad-1642f69c286c'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_04/arduino plus minus_ed08c4ae-cd2f-485c-a2ad-1642f69c286c.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'arduino-plus-minus'
    keyshape = Keyshape.HRECT_M
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/symbol'
    aliases = ()
    keywords = ()
    # Keyshape chosen first; stroke centerlines inset 2 from the ink bounds.
    chosen_bounds = Keyshape.HRECT_M.bounds_for(Profile.SOLO48)
    def build(self):
        # Infinity lobes share crossing at (24,24); axial endpoints own exact bounds.
        self.add_bezier('loop',(24,24),((23,16),(17,10),(12,10)),((7,10),(4,16),(4,24)),((4,32),(7,38),(12,38)),((17,38),(23,32),(24,24)),((25,16),(31,10),(36,10)),((41,10),(44,14),(44,20)),((44,22),(44,26),(44,28)),((44,34),(41,38),(36,38)),((31,38),(25,32),(24,24)))
        self.add_contour('infinity','loop',closed=True)
        self.add_line('minus',(13,24),(15,24))
        self.add_line('plus-h',(32,24),(36,24))
        self.add_line('plus-v',(34,22),(34,26))
        self.relate('connect','plus-h','plus-v')
