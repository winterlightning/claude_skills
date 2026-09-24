"""Doctor behind open laptop with medical cross. HRECT_L bounds4,8,44,40. Shared head/broad shoulder human reference; actual laptop/body contact at20,32."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.profiles import Profile
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'bc0dbbdb-7b2e-4bb7-b53e-d84b9f2a2265'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_29/online doctor laptop facetime_bc0dbbdb-7b2e-4bb7-b53e-d84b9f2a2265.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'online-doctor-laptop-facetime'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/symbol'
    aliases = ()
    keywords = ()
    # Keyshape chosen first; stroke centerlines inset 2 from the ink bounds.
    chosen_bounds = Keyshape.HRECT_L.bounds_for(Profile.SOLO48)
    def build(self):
        self.add_arc('head-a',(25,13),(35,13),radius_x=5)
        self.add_arc('head-b',(35,13),(25,13),radius_x=5)
        self.add_contour('head','head-a','head-b',closed=True)
        # human_ref/user.svg: head bottom18 to shoulder apex26 =8 centerline /4 ink.
        self.add_bezier('shoulder-left',(20,32),((22,28),(26,26),(30,26)))
        self.add_arc('shoulder-right',(30,26),(44,40),radius_x=14)
        self.add_contour('body','shoulder-left','shoulder-right')
        self.add_polyline('laptop',(4,40),(6,32),(20,32),(23,40),closed=True)
        self.add_polyline('screen',(6,32),(6,24),(8,24))
        self.relate('connect','screen','laptop')
        self.relate('connect','body','laptop')
        self.add_line('medical-h',(31,37),(35,37))
        self.add_line('medical-v',(33,35),(33,39))
        self.relate('connect','medical-h','medical-v')
