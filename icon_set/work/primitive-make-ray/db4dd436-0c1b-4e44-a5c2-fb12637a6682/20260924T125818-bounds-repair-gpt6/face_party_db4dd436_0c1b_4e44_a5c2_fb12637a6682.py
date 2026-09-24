"""Celebration face with raised eyes, party horn and star. CIRCLE exact radial extent22; integer arc centres at24,24. Deliberate expression asymmetry preserves celebratory source."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.profiles import Profile
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'db4dd436-0c1b-4e44-a5c2-fb12637a6682'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_17/face party_db4dd436-0c1b-4e44-a5c2-fb12637a6682.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'face-party'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/symbol'
    aliases = ()
    keywords = ()
    # Keyshape chosen first; stroke centerlines inset 2 from the ink bounds.
    chosen_bounds = Keyshape.CIRCLE.bounds_for(Profile.SOLO48)
    def build(self):
        # Three quarters of a radius20 circular face leave a real gap for a four-ray star.
        self.add_arc('face-top',(24,4),(44,24),radius_x=20)
        self.add_arc('face-bottom',(44,24),(4,24),radius_x=20)
        self.add_contour('face','face-top','face-bottom')
        self.add_line('star-h',(8,12),(16,12))
        self.add_line('star-v',(12,8),(12,16))
        self.relate('connect','star-h','star-v')
        self.add_arc('eye-left',(18,23),(22,23),radius_x=2)
        self.add_arc('eye-right',(30,19),(34,19),radius_x=2)
        self.add_polyline('mouth',(20,31),(20,32),(20,34))
        self.add_line('horn-stem',(20,32),(28,32))
        self.add_arc('horn-curl',(28,32),(32,28),radius_x=4,sweep=False)
        self.add_contour('horn','horn-stem','horn-curl')
        self.relate('connect','mouth','horn')
