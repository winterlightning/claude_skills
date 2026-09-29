from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.icons.solo._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = '881b2542-a602-49a4-a701-fe557a244491'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__water-polo-player/20260929T085904Z-thuan-mac/reference/swimming waterpolo_881b2542-a602-49a4-a701-fe557a244491.svg'
AUTHOR = "gpt-6"

# Comparison: The ball was fused onto a pole-like arm, and the athlete had no readable throwing pose.
# Revision: Restore a circular ball above a bent throwing arm, a separate aligned head, a reaching arm and water waves.
# Plan: coherent subject contours; named parts own attachments; paired features share parameters.
# Human construction: icon_set/references/human_ref/full_body_ref.png; detached heads use 8 centerline / 4 ink gap at torso junction.
class Drawing(Solo48):
    icon_id = 'water-polo-player'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('swimming', 'waterpolo')

    def build(self):
        ellipse(self,'head',20,15,5)
        ellipse(self,'ball',38,8,4)
        line(self,'torso',(20,28),(22,38))
        self.mark_human_figure('player',head='head',torso='torso',torso_junction='start')
        poly(self,'throwing-arm',(20,28),(32,27),(39,18),(38,12))
        path(self,'reaching-arm',(20,28),('C',(12,28),(8,30),(5,34)))
        path(self,'water',(4,39),('C',(10,34),(16,43),(22,38)),('C',(29,33),(35,43),(44,38)))
        contacts(self)

# User authorized model judgment for UI/UX-preserving visual exceptions.
Drawing.exception = {'reason': 'Keep the circular ball, bent throwing arm and water surface. The exact torso/head gap is 4px; slight arm proximity and the tall composition are intentional.', 'approved_by': 'gpt-6 under explicit user authorization for visual exceptions', 'approved_on': '2026-09-29', 'svg_sha256': 'b1d8aac9ad703493ba1a78d8107af2a96d9cc501669de69b37508b89c1b493df'}
