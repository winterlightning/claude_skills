"""Navigation message on smartphone. VRECT_L exact centerline bounds8,4,40,44. Bubble and phone share genuine edge endpoints; the pin remains independent."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.profiles import Profile
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '9d04d41b-14a1-476d-b164-23e91f0672af'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_28/navigation smartphone message_9d04d41b-14a1-476d-b164-23e91f0672af.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'navigation-smartphone-message'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/symbol'
    aliases = ()
    keywords = ()
    # Keyshape chosen first; stroke centerlines inset 2 from the ink bounds.
    chosen_bounds = Keyshape.VRECT_L.bounds_for(Profile.SOLO48)
    def build(self):
        # Tall phone behind an overlapping bubble; preserve the pin as one closed teardrop.
        self.add_polyline('phone',(30,12),(30,4),(8,4),(8,44),(30,44),(30,36))
        self.add_polyline('bubble',(16,12),(40,12),(40,36),(24,36),(16,42),closed=True)
        self.relate('connect','phone','bubble')
        self.add_arc('pin-cap',(24,24),(32,24),radius_x=4)
        self.add_line('pin-tip-1',(32,24),(28,28))
        self.add_line('pin-tip-2',(28,28),(24,24))
        self.add_contour('pin','pin-cap','pin-tip-1','pin-tip-2',closed=True)
