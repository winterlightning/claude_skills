"""A girl faces right with long hair and a curved hairline. Lucide users informs rounded anatomy; no exact Lucide profile match. Eye and small ear curls are omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f404fb88-9a98-5205-866b-ada53c69d0f2'
SOURCE_PATH = 'pictographic-primitives/users/girl head_f404fb88-9a98-5205-866b-ada53c69d0f2.svg'
AUTHOR = 'gpt-6'


class GirlHeadProfile(Solo48):
    icon_id = 'girl-head-profile'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "users"
    aliases = ()
    keywords = ('girl', 'woman', 'head', 'profile', 'face', 'hair', 'female', 'person')

    def build(self) -> None:
        # Portrait extremes (8,6)-(40,42); right-facing silhouette is asymmetric.
        self.add_bezier('crown',(8,20),((8,11),(17,4),(26,4)))
        self.add_bezier('forehead',(26,4),((32,4),(36,8),(36,14)))
        self.add_line('face-1',(36,14),(36,21))
        self.add_line('face-2',(36,21),(40,27))
        self.add_line('face-3',(40,27),(35,29))
        self.add_line('face-4',(35,29),(35,33))
        self.add_arc('chin',(35,33),(30,38),radius_x=5)
        self.add_line('neck-1',(30,38),(26,38))
        self.add_line('neck-2',(26,38),(24,44))
        self.add_contour('profile','crown','forehead','face-1','face-2','face-3','face-4','chin','neck-1','neck-2')
        self.add_polyline('hair-back',(8,20),(8,33),(8,39),(14,39))
        self.relate('connect','profile','hair-back')
        self.add_arc('hairline',(36,14),(22,24),radius_x=20)
        self.add_arc('ear',(22,24),(22,32),radius_x=4,sweep=False)
        self.add_line('hair-end',(22,32),(14,39))
        self.add_contour('hair-front','hairline','ear','hair-end')
        self.relate('connect','profile','hair-front')
        self.relate('connect','hair-back','hair-front')
