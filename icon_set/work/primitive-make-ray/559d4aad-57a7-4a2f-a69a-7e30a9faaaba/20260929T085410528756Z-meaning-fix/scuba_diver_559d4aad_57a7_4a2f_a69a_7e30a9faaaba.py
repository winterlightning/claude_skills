"""Draw a horizontal swimmer with a compact solid back tank, bent leg and flat flipper stroke, forward reaching arm, circular head and a water surface.
Construction plan: Head (39,23), radius 5; neck (27,28) is exactly 13 away, so head/body ink gap is 4. Torso tangent follows (12,-5); first arm direction (5,12) is perpendicular, keeping the neck nearest. Tank is a compact solid rounded cylinder above the back. HRECT_L extremes (4,8)-(44,40).
Human construction: icon_set/references/human_ref/full_body_ref.png.
Lucide person-standing original and atomic-debug: articulated limbs and shared torso nodes.
Source comparison: The rejected diver has a box-shaped tank dominating an angular body, a floating head, and no clear flipper silhouette.
Omissions: fine source outline doubling; preserve the complete action and its identifying prop.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '559d4aad-57a7-4a2f-a69a-7e30a9faaaba'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__scuba-diver/20260929T084652Z-thuan-mac/reference/diving diver_559d4aad-57a7-4a2f-a69a-7e30a9faaaba.svg'
AUTHOR = 'gpt-6'
class AuthoredIcon(Solo48):
    icon_id = 'scuba-diver'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/activity'
    aliases = ()
    keywords = ('scuba', 'diver')

    def circle(self, name, cx, cy, r):
        self.add_arc(name+'-top', (cx-r,cy), (cx+r,cy), radius_x=r)
        self.add_arc(name+'-bottom', (cx+r,cy), (cx-r,cy), radius_x=r)
        self.add_contour(name, name+'-top', name+'-bottom', closed=True)

    def build(self):

        self.add_bezier('surface',(4,8),((10,10),(15,10),(20,8)),((26,10),(32,10),(38,8)),((40,9),(42,10),(44,10)))
        self.circle('head',39,23,5)
        self.add_line('torso',(27,28),(15,33))
        self.add_polyline('leg',(15,33),(8,26),(4,26))
        self.add_polyline('arm',(27,28),(32,40),(44,40))
        self.add_line('tank',(15,21),(23,21))
        self.relate('connect','torso','leg')
        self.relate('connect','torso','arm')
        self.mark_human_figure('person',head='head',torso='torso',torso_junction='start')

