"""Restore three ascending fire trails and a pointed enclosed lower flame beneath a crisp right arrow.
Construction plan: Directional arrow at top; three individually owned flame tongues flow upward to the right. Square centerline extremes (6,6)-(42,42). Intentional directional asymmetry.
Human construction: icon_set/references/human_ref/full_body_ref.png.
Lucide person-standing original and atomic-debug: articulated limbs and shared torso nodes.
Source comparison: The rejected arrow sits over two short generic squiggles; it loses the original flowing fire and outlined lower flame.
Omissions: fine source outline doubling; preserve the complete action and its identifying prop.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '10fe00ef-bdce-47d7-95cd-4727e2fc9f1a'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__safety-fire-right/20260929T084652Z-thuan-mac/reference/safety fire right_10fe00ef-bdce-47d7-95cd-4727e2fc9f1a.svg'
AUTHOR = 'gpt-6'
class AuthoredIcon(Solo48):
    icon_id = 'safety-fire-right'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/activity'
    aliases = ()
    keywords = ('safety', 'fire', 'right')

    def circle(self, name, cx, cy, r):
        self.add_arc(name+'-top', (cx-r,cy), (cx+r,cy), radius_x=r)
        self.add_arc(name+'-bottom', (cx+r,cy), (cx-r,cy), radius_x=r)
        self.add_contour(name, name+'-top', name+'-bottom', closed=True)

    def build(self):

        self.add_polyline('arrow', (31,6), (42,17), (31,28))
        self.add_line('shaft', (6,17), (42,17))
        self.relate('connect','arrow','shaft')
        self.add_bezier('upper-flame', (6,27), ((14,27),(17,27),(21,23)))
        self.add_bezier('middle-flame', (6,35), ((12,27),(19,36),(26,29)))
        self.add_bezier('lower-flame-top', (6,42), ((10,32),(19,42),(25,36)))
        self.add_bezier('lower-flame-bottom', (25,36), ((22,43),(13,42),(6,42)))
        self.add_contour('lower-flame','lower-flame-top','lower-flame-bottom',closed=True)

