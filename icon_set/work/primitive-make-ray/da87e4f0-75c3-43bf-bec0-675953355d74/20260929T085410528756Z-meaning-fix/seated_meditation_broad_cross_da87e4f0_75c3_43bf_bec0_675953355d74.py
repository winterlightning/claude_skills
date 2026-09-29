"""Replace the crossed sticks with rounded folded knees and overlapping shins, and angle relaxed arms down to the knees.
Construction plan: Head centered (24,11), r5; neck (24,24), exact 4 ink gap. Mirrored arms rest beside the folded lap. Crossed shin owns its diagonal; rear shin stops behind it. Square extremes (6,6)-(42,42).
Human construction: icon_set/references/human_ref/full_body_ref.png.
Lucide person-standing original and atomic-debug: articulated limbs and shared torso nodes.
Source comparison: The rejected figure has arched wing-like arms and two floating crossed sticks instead of folded seated legs.
Omissions: fine source outline doubling; preserve the complete action and its identifying prop.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'da87e4f0-75c3-43bf-bec0-675953355d74'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__seated-meditation-broad-cross/20260929T084652Z-thuan-mac/reference/yoga meditation pose_da87e4f0-75c3-43bf-bec0-675953355d74.svg'
AUTHOR = 'gpt-6'
class AuthoredIcon(Solo48):
    icon_id = 'seated-meditation-broad-cross'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/activity'
    aliases = ()
    keywords = ('seated', 'meditation', 'broad', 'cross')

    def circle(self, name, cx, cy, r):
        self.add_arc(name+'-top', (cx-r,cy), (cx+r,cy), radius_x=r)
        self.add_arc(name+'-bottom', (cx+r,cy), (cx-r,cy), radius_x=r)
        self.add_contour(name, name+'-top', name+'-bottom', closed=True)

    def build(self):

        self.circle('head',24,11,5)
        self.add_line('torso',(24,24),(24,32))
        self.add_polyline('left-arm',(24,24),(17,24),(12,32),(6,32))
        self.add_polyline('right-arm',(24,24),(31,24),(36,32),(42,32))
        self.add_bezier('folded-legs',(15,32),((9,32),(6,35),(6,37)),((6,40),(10,42),(14,42)),((20,42),(28,42),(34,42)),((38,42),(42,40),(42,37)),((42,35),(39,32),(33,32)))
        self.add_line('front-shin',(15,32),(30,42))
        self.add_line('rear-shin',(33,32),(26,36))
        for a,b in [('torso','left-arm'),('torso','right-arm'),('left-arm','right-arm'),('folded-legs','front-shin'),('folded-legs','rear-shin')]:
            self.relate('connect',a,b)
        self.mark_human_figure('person',head='head',torso='torso',torso_junction='start')

