"""A front-facing human statuette on a broad pedestal; omit facial and finger detail.

Live VRECT_L bounds: visible (6,2)-(42,46), centerline (8,4)-(40,44)
for VRECT_L; SQUARE uses visible (4,4)-(44,44), centerline (6,6)-(42,42).
Lucide trophy informs the pedestal hierarchy; no useful local statuette
match was found. The supplied source sets the head, close arms and lower body. Geometry authored independently on SOLO48.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '2b86f2d7-36fb-55d6-9d23-df0241b674c4'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__oscar-statuette/20260927T153322Z-thuan-mac-1/reference/award oscar_2b86f2d7-36fb-55d6-9d23-df0241b674c4.svg'
AUTHOR = "gpt-6"

class OscarStatuette(Solo48):
    icon_id = 'oscar-statuette'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'rewards'
    categories = ('rewards', 'primitives')
    aliases = ()
    keywords = ('award', 'prize', 'recognition', 'oscar-statuette')

    def build(self) -> None:
        # Slim figure with tapered torso and arms at its sides, on a stepped base.
        self.add_arc('head-right',(24,4),(24,14),radius_x=4,radius_y=5)
        self.add_arc('head-left',(24,14),(24,4),radius_x=4,radius_y=5)
        self.add_contour('head','head-right','head-left',closed=True)
        self.add_polyline('figure',(24,14),(18,18),(17,25),(18,29),(18,36),(30,36),(30,29),(31,25),(30,18),(24,14),closed=True)
        self.relate('connect','head','figure')
        self.add_polyline('base',(8,44),(8,36),(18,36))
        self.add_polyline('base-right',(30,36),(40,36),(40,44),(8,44))
        self.relate('connect','figure','base')
        self.relate('connect','figure','base-right')
        self.relate('connect','base','base-right')
