"""Three larger heads and distinct shoulders under one clear Wi-Fi arc on a SQUARE envelope. Shared human_ref/user.svg guided their proportions."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.profiles import Profile
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'a119cf45-d021-460f-b469-9d1f28774714'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__multiple-users-wifi/20260927T142540Z-thuan-mac-1/reference/multiple users wifi_a119cf45-d021-460f-b469-9d1f28774714.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'multiple-users-wifi'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ()
    # Keyshape chosen first; stroke centerlines inset 2 from the ink bounds.
    chosen_bounds = Keyshape.SQUARE.bounds_for(Profile.SOLO48)
    def build(self):
        # Three distinct heads and shoulders sit below one broad Wi-Fi arc.
        self.add_arc('wifi',(6,12),(42,12),radius_x=18,radius_y=6)
        for name,x in (('left',9),('center',24),('right',39)):
            self.add_arc(name+'-head-top',(x-3,24),(x+3,24),radius_x=3)
            self.add_arc(name+'-head-bottom',(x+3,24),(x-3,24),radius_x=3)
            self.add_contour(name+'-head',name+'-head-top',name+'-head-bottom',closed=True)
        self.add_bezier('left-body',(6,42),((6,38),(7,36),(9,36)),((11,36),(14,38),(16,42)))
        self.add_bezier('center-body',(16,42),((16,38),(19,36),(24,36)),((29,36),(32,38),(32,42)))
        self.add_bezier('right-body',(32,42),((34,38),(37,36),(39,36)),((41,36),(42,38),(42,42)))
        self.relate('connect','left-body','center-body')
        self.relate('connect','center-body','right-body')
