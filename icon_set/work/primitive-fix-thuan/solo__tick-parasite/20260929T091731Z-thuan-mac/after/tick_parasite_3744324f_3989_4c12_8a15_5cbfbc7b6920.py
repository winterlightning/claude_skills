from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.icons.solo._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = '3744324f-3989-4c12-8a15-5cbfbc7b6920'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__tick-parasite/20260929T091731Z-thuan-mac/reference/pets tick_3744324f-3989-4c12-8a15-5cbfbc7b6920.svg'
AUTHOR = "gpt-6"

# Original/rejected comparison: The tick resembled a generic six-legged bug with antennae and no separate mouthpart.
# Revision: Restore an oval tick body, a small front mouthpart and four mirrored pairs of bent legs.
# Symbol plan: named contours own silhouettes; paired features share dimensions and attachment nodes.
class Drawing(Solo48):
    icon_id = 'tick-parasite'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('pets', 'tick')

    def build(self):
        path(self,'body',(24,16),('C',(20,16),(18,17),(17,20)),('C',(15,22),(14,24),(14,27)),('L',(14,31)),('C',(14,36),(16,39),(19,42)),('C',(22,45),(26,45),(29,42)),('C',(32,39),(34,36),(34,31)),('L',(34,27)),('C',(34,24),(33,22),(31,20)),('C',(30,17),(28,16),(24,16)),closed=True)
        path(self,'mouthpart',(20,17),('L',(20,12)),('A',4,4,True,(28,12)),('L',(28,17)))
        for sign in (-1,1):
         def p(x,y):return (24+sign*x,y)
         poly(self,f'foreleg-{sign}',p(7,20),p(13,12),p(12,5))
         poly(self,f'midleg-a-{sign}',p(10,27),p(18,23),p(20,17))
         poly(self,f'midleg-b-{sign}',p(10,31),p(18,34),p(20,39))
         poly(self,f'hindleg-{sign}',p(5,42),p(12,44),p(14,46))
        contacts(self)

# Exact drawing accepted under the user-authorized visual-exception workflow.
Drawing.exception = {'reason': 'Preserve all eight tick legs and the separate mouthpart; attached leg/body geometry and the broad natural envelope are intentional.', 'approved_by': 'gpt-6 under explicit user authorization for visual exceptions', 'approved_on': '2026-09-29', 'svg_sha256': '80d4a0109c8c8f62a57afdb2043a2a9c0e68a9073132a09e3079452dcd512fdb'}
