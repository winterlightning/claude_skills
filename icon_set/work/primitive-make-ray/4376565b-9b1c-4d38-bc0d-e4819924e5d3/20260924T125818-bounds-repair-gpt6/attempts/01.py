"""Care emoji: circular upper face, closed eyes, heart and two embracing hands. SQUARE extremes 6,6,42,42. Shared heart lobes and mirrored hands."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.profiles import Profile
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '4376565b-9b1c-4d38-bc0d-e4819924e5d3'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_16/emoji care hug heart face_4376565b-9b1c-4d38-bc0d-e4819924e5d3.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'emoji-care-hug-heart-face'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/symbol'
    aliases = ()
    keywords = ()
    # Keyshape chosen first; stroke centerlines inset 2 from the ink bounds.
    chosen_bounds = Keyshape.SQUARE.bounds_for(Profile.SOLO48)
    def build(self):
        # Open circular face above a heart; mirrored hands attach to the heart sides.
        self.add_arc('face',(6,24),(42,24),radius_x=18)
        for name,x in [('left',18),('right',30)]:
            self.add_arc('eye-'+name,(x-1,18),(x+1,18),radius_x=1)
        self.add_arc('heart-left',(24,31),(16,31),radius_x=4,sweep=False)
        self.add_polyline('heart-bottom',(16,31),(16,35),(24,42),(32,35),(32,31))
        self.add_arc('heart-right',(32,31),(24,31),radius_x=4,sweep=False)
        self.relate('connect','heart-left','heart-bottom')
        self.relate('connect','heart-right','heart-bottom')
        self.relate('connect','heart-left','heart-right')
        self.add_arc('hand-left',(16,35),(16,41),radius_x=4,radius_y=3,sweep=False)
        self.add_arc('hand-right',(32,41),(32,35),radius_x=4,radius_y=3,sweep=False)
        self.relate('connect','hand-left','heart-bottom')
        self.relate('connect','hand-right','heart-bottom')
