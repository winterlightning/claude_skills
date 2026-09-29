"""Restore a rounded folded lap with overlapping shins and rebalance the overhead arms around a larger head and short upright torso.
Construction plan: Head (24,14), r5, neck (24,27), exact 4 ink gap. Arms mirror about x24 and rise above the head. Folded lap uses the same vocabulary as meditation. Square extremes (6,6)-(42,42).
Human construction: icon_set/references/human_ref/full_body_ref.png.
Lucide person-standing original and atomic-debug: articulated limbs and shared torso nodes.
Source comparison: The rejected raised-arm figure sits above a disconnected X, so the lower half does not clearly read as a seated yoga pose.
Omissions: fine source outline doubling; preserve the complete action and its identifying prop.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'f67610a5-7a4d-4827-a29e-81df7c544fc5'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__seated-overhead-stretch/20260929T084652Z-thuan-mac/reference/yoga arms stretch_f67610a5-7a4d-4827-a29e-81df7c544fc5.svg'
AUTHOR = 'gpt-6'
class AuthoredIcon(Solo48):
    icon_id = 'seated-overhead-stretch'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/activity'
    aliases = ()
    keywords = ('seated', 'overhead', 'stretch')

    def circle(self, name, cx, cy, r):
        self.add_arc(name+'-top', (cx-r,cy), (cx+r,cy), radius_x=r)
        self.add_arc(name+'-bottom', (cx+r,cy), (cx-r,cy), radius_x=r)
        self.add_contour(name, name+'-top', name+'-bottom', closed=True)

    def build(self):

        self.circle('head',24,14,5)
        self.add_line('torso',(24,27),(24,32))
        self.add_bezier('left-arm',(24,27),((13,27),(6,19),(6,6)))
        self.add_bezier('right-arm',(24,27),((35,27),(42,19),(42,6)))
        self.add_bezier('folded-legs',(15,32),((9,32),(6,35),(6,37)),((6,40),(10,42),(14,42)),((20,42),(28,42),(34,42)),((38,42),(42,40),(42,37)),((42,35),(39,32),(33,32)))
        self.add_line('front-shin',(15,32),(30,42))
        self.add_line('rear-shin',(33,32),(26,36))
        for a,b in [('torso','left-arm'),('torso','right-arm'),('left-arm','right-arm'),('folded-legs','front-shin'),('folded-legs','rear-shin')]:
            self.relate('connect',a,b)
        self.mark_human_figure('person',head='head',torso='torso',torso_junction='start')

