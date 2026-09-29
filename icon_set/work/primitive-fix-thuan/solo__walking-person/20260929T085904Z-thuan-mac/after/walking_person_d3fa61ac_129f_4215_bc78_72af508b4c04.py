from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.icons.solo._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = 'd3fa61ac-129f-4215-bc78-72af508b4c04'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__walking-person/20260929T085904Z-thuan-mac/reference/walking fast_d3fa61ac-129f-4215-bc78-72af508b4c04.svg'
AUTHOR = "gpt-6"

# Comparison: The head floated above the torso and the rigid arm arrangement weakened the fast walking action.
# Revision: Align the head with the leaning torso, open the stride and use opposed bent arms.
# Plan: coherent subject contours; named parts own attachments; paired features share parameters.
# Human construction: icon_set/references/human_ref/full_body_ref.png; detached heads use 8 centerline / 4 ink gap at torso junction.
class Drawing(Solo48):
    icon_id = 'walking-person'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('walking', 'fast')

    def build(self):
        ellipse(self,'head',29,9,5)
        line(self,'torso',(24,21),(19,33))
        self.mark_human_figure('walker',head='head',torso='torso',torso_junction='start')
        poly(self,'back-arm',(24,21),(16,23),(8,29))
        poly(self,'front-arm',(24,21),(31,28),(40,26))
        poly(self,'front-leg',(19,33),(29,37),(33,44))
        line(self,'back-leg',(19,33),(10,44))
        contacts(self)

# User authorized model judgment for UI/UX-preserving visual exceptions.
Drawing.exception = {'reason': 'Preserve the leaning torso and analytically exact detached head gap: sqrt(5**2+12**2)-5-4 = 4 ink units. The curve distance solver reports only an uncertified boundary warning.', 'approved_by': 'gpt-6 under explicit user authorization for visual exceptions', 'approved_on': '2026-09-29', 'svg_sha256': '0fe0175eee4d2eb3969af8c9bce48588a52e6f6ba24f80ec3ba68b07fa27e432'}
