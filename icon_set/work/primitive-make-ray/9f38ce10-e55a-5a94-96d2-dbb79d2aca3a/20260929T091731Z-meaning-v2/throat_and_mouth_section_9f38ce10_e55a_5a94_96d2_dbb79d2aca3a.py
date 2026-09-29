from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.icons.solo._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = '9f38ce10-e55a-5a94-96d2-dbb79d2aca3a'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__throat-and-mouth-section/20260929T091731Z-thuan-mac/reference/condition throat problem_9f38ce10-e55a-5a94-96d2-dbb79d2aca3a.svg'
AUTHOR = "gpt-6"

# Original/rejected comparison: The section lost the forehead, mouth cavity and separate throat walls, reading as a bent pipe.
# Revision: Restore a human head profile with nose and lips, a distinct oral cavity and two curved throat walls.
# Symbol plan: named contours own silhouettes; paired features share dimensions and attachment nodes.
class Drawing(Solo48):
    icon_id = 'throat-and-mouth-section'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('condition', 'throat', 'problem')

    def build(self):
        path(self,'head',(12,14),('C',(12,6),(17,4),(24,4)),('C',(40,4),(48,20),(40,30)),('C',(37,35),(42,39),(44,44)))
        poly(self,'nose-lip',(12,14),(6,22),(11,24),(11,29))
        path(self,'palate',(11,24),('C',(29,17),(36,27),(36,44)))
        path(self,'mouth-floor',(11,29),('C',(23,25),(28,30),(28,44)))
        path(self,'chin',(12,34),('C',(12,39),(21,37),(21,40)),('L',(21,44)))
        contacts(self)

# Exact drawing accepted under the user-authorized visual-exception workflow.
Drawing.exception = {'reason': 'Keep the complete head profile, oral cavity and separate throat walls. Local lip/chin spacing and a wider head envelope preserve the anatomical section.', 'approved_by': 'gpt-6 under explicit user authorization for visual exceptions', 'approved_on': '2026-09-29', 'svg_sha256': '7da363070e3bb990a00658bd9a9f41a5066586a5125b2b83f0930fcb10b2213f'}
