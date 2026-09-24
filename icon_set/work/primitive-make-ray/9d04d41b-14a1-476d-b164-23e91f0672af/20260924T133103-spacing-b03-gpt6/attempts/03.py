"""Rebalance the overlapping phone and message using a single shared left wall. Wider teardrop opens the pin hole; VRECT_L preserves top4 bottom44."""
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
        # Shared left wall is emitted once; actual overlap between phone and bubble is merged.
        self.add_polyline('phone-top',(30,12),(30,4),(8,4),(8,12))
        self.add_polyline('phone-bottom',(8,42),(8,44),(30,44),(30,36))
        self.add_polyline('bubble',(8,12),(40,12),(40,36),(16,36),(8,42),closed=True)
        self.relate('connect','phone-top','bubble')
        self.relate('connect','phone-bottom','bubble')
        self.add_arc('pin-cap',(18,25),(30,25),radius_x=6,radius_y=4)
        self.add_line('pin-right',(30,25),(24,28))
        self.add_line('pin-left',(24,28),(18,25))
        self.add_contour('pin','pin-cap','pin-right','pin-left',closed=True)
