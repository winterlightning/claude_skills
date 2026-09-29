"""Restore a pointed enclosed lower flame and a rising open flame trail beneath a crisp right arrow; omit the third trail to give the flame opening room.
Construction plan: Directional arrow at top; open and enclosed flame tongues flow upward to the right. Square centerline extremes (6,6)-(42,42). Intentional directional asymmetry. No useful local Lucide flame-trail match.
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

        self.add_polyline('arrow', (32,6), (42,16), (32,26))
        self.add_line('shaft', (6,16), (42,16))
        self.relate('connect','arrow','shaft')
        self.add_bezier('upper-flame', (6,26), ((14,26),(17,26),(22,24)))
        self.add_bezier('lower-flame-top', (6,42), ((9,31),(18,37),(25,32)))
        self.add_bezier('lower-flame-bottom', (25,32), ((22,42),(15,42),(6,42)))
        self.add_contour('lower-flame','lower-flame-top','lower-flame-bottom',closed=True)

