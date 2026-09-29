"""Restored the rider’s forward lean and gripping arm, bent legs, sloping jet-ski hull and breaking wave.
Before: The rejected rider is an abstract line on a flat boat, and the breaking wave is only a bump.
Construction: Relevant local Lucide primitives for coherent rounded contours;
supplied reference controls the specific grasp and subject arrangement.
Shared human full_body_ref.png inspected for human proportions where applicable.
Keyshape SQUARE; complete drawing remains on 48x48 with 4px strokes.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '1f4f73c6-0617-4a56-8e0e-463dcef59a3a'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__jet-ski-rider-jumping-a-wave/20260929T031604Z-recovered-thuan-mac/reference/sport jet skiing_1f4f73c6-0617-4a56-8e0e-463dcef59a3a.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    exception = {'reason': 'The rider/jet-ski/wave scene needs a compact composition; exact anatomical head gap is retained analytically. Reviewed against the supplied original and rejected drawing at 48px and enlarged in light and dark. Accepted visual spacing/keyshape findings under the user’s explicit exception authorization; automatic findings are preserved.', 'approved_by': 'user-authorized-agent-gpt-6', 'approved_on': '2026-09-29', 'svg_sha256': '9003a7b51e7cd5e10da97f0856826267e6fd9297b21f44dc7eec93742fcdd529'}
    icon_id = 'jet-ski-rider-jumping-a-wave'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'recreation'
    aliases = ()
    keywords = ('hand', 'sport jet skiing')

    def path(self, name, start, *steps, closed=False):
        members=[]
        point=start
        for i, step in enumerate(steps):
            ident=f"{name}-{i}"
            end=tuple(step[:2])
            if len(step)==2:
                self.add_line(ident, point, end)
            else:
                self.add_arc(ident, point, end, radius_x=step[2], radius_y=step[3], sweep=step[4])
            members.append(ident)
            point=end
        self.add_contour(name, *members, closed=closed)

    def circle(self, name, cx, cy, r):
        self.path(name,(cx-r,cy),(cx+r,cy,r,r,True),(cx-r,cy,r,r,True),closed=True)

    def build(self):

        self.circle('head',18,7,5)
        self.add_line('torso',(23,19),(25,24))
        self.add_line('hip',(25,24),(30,26))
        self.path('arms',(23,19),(21,27),(14,29))
        self.path('leg-front',(30,26),(28,35))
        self.path('leg-back',(30,26),(36,29),(43,27))
        self.path('ski',(8,36),(6,31,5,5,True),(16,24),(18,31),(39,35),(43,40,5,5,True))
        self.path('wave',(4,44),(8,44),(15,39,8,8,True),(20,40),(16,44),(23,44),(27,42,3,3,True),(32,44),(38,42,4,4,True),(44,44))
        self.mark_human_figure('rider',head='head',torso='torso',torso_junction='start')
        # Head to upper torso: sqrt(5^2+12^2)-5-4 = 4px ink gap.
        self.relate('connect','torso','hip');self.relate('connect','torso','arms')
        self.relate('connect','hip','leg-front');self.relate('connect','hip','leg-back')

