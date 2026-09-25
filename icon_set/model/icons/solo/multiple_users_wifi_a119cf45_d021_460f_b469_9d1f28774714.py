"""Three people under Wi-Fi; square exact extremes6,6,42,42. Shared human_ref/user.svg round heads and broad shoulders. One radio arc omitted to budget real gaps."""
from ...keyshapes import Keyshape
from icon_set.model.profiles import Profile
from ._base import Solo48
SOURCE_ICON_ID = 'a119cf45-d021-460f-b469-9d1f28774714'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_28/multiple users wifi_a119cf45-d021-460f-b469-9d1f28774714.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'multiple-users-wifi'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ()
    # Keyshape chosen first; stroke centerlines inset 2 from the ink bounds.
    chosen_bounds = Keyshape.SQUARE.bounds_for(Profile.SOLO48)
    def build(self):
        # Two spaced radio arcs over three heads; shoulders retain exact detached-head clearance.
        self.add_arc('wifi-outer',(6,14),(42,14),radius_x=18,radius_y=8)
        self.add_arc('wifi-inner',(15,20),(33,20),radius_x=9,radius_y=5)
        self.add_arc('center-head-a',(21,27),(27,27),radius_x=3)
        self.add_arc('center-head-b',(27,27),(21,27),radius_x=3)
        self.add_contour('center-head','center-head-a','center-head-b',closed=True)
        self.add_arc('left-head-a',(8,31),(12,31),radius_x=2)
        self.add_arc('left-head-b',(12,31),(8,31),radius_x=2)
        self.add_contour('left-head','left-head-a','left-head-b',closed=True)
        self.add_arc('right-head-a',(36,31),(40,31),radius_x=2)
        self.add_arc('right-head-b',(40,31),(36,31),radius_x=2)
        self.add_contour('right-head','right-head-a','right-head-b',closed=True)
        self.add_bezier('center-body',(16,42),((16,38),(20,38),(24,38)),((28,38),(32,38),(32,42)))
        self.add_bezier('left-body',(6,42),((6,41),(8,41),(10,41)),((12,41),(14,42),(16,42)))
        self.add_bezier('right-body',(32,42),((34,42),(36,41),(38,41)),((40,41),(42,41),(42,42)))
        self.relate('connect','center-body','left-body')
        self.relate('connect','center-body','right-body')
        # Head bottoms30/33 and shoulder crests38/41: exact 8 centerline /4 ink gaps.
