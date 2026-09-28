"""An open drawer with a recessed finger pull.
Plan: x24 symmetry, rear trapezoid attached to rounded front, central scoop.
HRECT_L centerline extremes (4,8)-(44,40) keep the wide drawer proportion.
Lucide inbox original and atomic-debug inform perspective sides and recessed
front. Source supplies the curved scoop. Omit the redundant rear seam to
preserve clearance. Radius4 corners; radius6 semicircular finger recess.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '244afd80-5d73-57d2-8e56-c06e1e49d855'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/emails/drawer open_244afd80-5d73-57d2-8e56-c06e1e49d855.svg'
AUTHOR = "gpt-6"

class OpenDrawer(Solo48):
    icon_id = 'open-drawer'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "emails"
    categories = ("emails", "primitives")
    aliases = ()
    keywords = ('open', 'drawer')

    def build(self):
        self.add_polyline('rear',(4,20),(10,8),(38,8),(44,20))
        self.add_line('front-left',(4,20),(18,20))
        self.add_arc('scoop',(18,20),(30,20),radius_x=6,sweep=False)
        self.add_line('front-right0',(30, 20),(44, 20))
        self.add_line('front-right1',(44, 20),(44, 36))
        self.add_arc('corner-right',(44,36),(40,40),radius_x=4)
        self.add_line('bottom',(40,40),(8,40))
        self.add_arc('corner-left',(8,40),(4,36),radius_x=4)
        self.add_line('left',(4,36),(4,20))
        self.add_contour('front','front-left','scoop','front-right0','front-right1','corner-right','bottom','corner-left','left',closed=True)
        self.relate('connect','rear','front')
