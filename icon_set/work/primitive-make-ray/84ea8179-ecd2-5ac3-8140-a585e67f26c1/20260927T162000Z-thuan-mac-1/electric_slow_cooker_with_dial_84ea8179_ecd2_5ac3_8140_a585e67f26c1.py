"""Electric Slow Cooker Appliance."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '84ea8179-ecd2-5ac3-8140-a585e67f26c1'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__electric-slow-cooker-with-dial/20260927T160114Z-thuan-mac-1/reference/appliances slow cooker_84ea8179-ecd2-5ac3-8140-a585e67f26c1.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'electric-slow-cooker-with-dial'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    categories = ('primitives', 'food')
    aliases = ()
    keywords = ('slow cooker', 'appliance', 'pot', 'lid', 'dial', 'kitchen', 'cooking')

    def build(self):
        # A knobbed domed lid meets the straight vessel rim; ring dial is centered.
        self.add_polyline('knob',(20,8),(28,8),(26,12),(22,12),closed=True)
        self.add_bezier('lid',(6,18),((9,13),(14,12),(22,12)),((30,12),(39,13),(42,18)))
        self.relate('connect','knob','lid')
        self.add_bezier('body',(4,18),((4,25),(5,34),(8,38)),
            ((10,40),(15,40),(24,40)),((33,40),(38,40),(40,38)),
            ((43,34),(44,25),(44,18)))
        self.add_line('rim',(44,18),(4,18))
        self.add_contour('pot','body','rim',closed=True)
        self.relate('connect','lid','pot')
        self.add_arc('dial-a',(21,29),(27,29),radius_x=3)
        self.add_arc('dial-b',(27,29),(21,29),radius_x=3)
        self.add_contour('dial','dial-a','dial-b',closed=True)
