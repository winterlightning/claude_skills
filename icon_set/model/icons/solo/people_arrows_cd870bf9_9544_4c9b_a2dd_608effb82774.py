"""Two people and a two-way exchange arrow. SQUARE extremes6,6,42,42. Shared human_ref/user.svg head/shoulder proportions; mirrored people, actual shared arrow endpoints."""
from ...keyshapes import Keyshape
from icon_set.model.profiles import Profile
from ._base import Solo48
SOURCE_ICON_ID = 'cd870bf9-9544-4c9b-a2dd-608effb82774'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_30/people arrows_cd870bf9-9544-4c9b-a2dd-608effb82774.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'people-arrows'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ()
    # Keyshape chosen first; stroke centerlines inset 2 from the ink bounds.
    chosen_bounds = Keyshape.SQUARE.bounds_for(Profile.SOLO48)
    def build(self):
        # Two equal busts; detached head bottom14 and shoulder apex22 leave4 visible units.
        self.add_arc('left-head-a',(9,10),(17,10),radius_x=4)
        self.add_arc('left-head-b',(17,10),(9,10),radius_x=4)
        self.add_contour('left-head','left-head-a','left-head-b',closed=True)
        self.add_arc('left-shoulders',(6,27),(20,27),radius_x=7,radius_y=5)
        self.add_arc('right-head-a',(31,10),(39,10),radius_x=4)
        self.add_arc('right-head-b',(39,10),(31,10),radius_x=4)
        self.add_contour('right-head','right-head-a','right-head-b',closed=True)
        self.add_arc('right-shoulders',(28,27),(42,27),radius_x=7,radius_y=5)
        self.add_line('shaft',(12,38),(36,38))
        self.add_polyline('arrow-left',(16,34),(12,38),(16,42))
        self.add_polyline('arrow-right',(32,34),(36,38),(32,42))
        self.relate('connect','shaft','arrow-left')
        self.relate('connect','shaft','arrow-right')
