from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.icons.solo._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = '49d9fd72-8a7d-597e-816c-4096337fbbd2'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__tilted-champagne-bottle-in-flared-bucket/20260929T091731Z-thuan-mac/reference/champagne cooler_49d9fd72-8a7d-597e-816c-4096337fbbd2.svg'
AUTHOR = "gpt-6"

# Original/rejected comparison: The champagne bottle became an angular lump with a cross-shaped top, while the bucket lost its rim.
# Revision: Restore a diagonally tilted bottle with neck and cap, above a flared bucket with a visible rim.
# Symbol plan: named contours own silhouettes; paired features share dimensions and attachment nodes.
class Drawing(Solo48):
    icon_id = 'tilted-champagne-bottle-in-flared-bucket'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('champagne', 'cooler')

    def build(self):
        poly(self,'bottle-cap',(35,4),(43,10),(40,14),(32,8),closed=True)
        path(self,'bottle-left',(32,8),('L',(27,15)),('C',(24,16),(20,18),(18,24)))
        path(self,'bottle-right',(40,14),('L',(35,21)),('L',(35,24)))
        box(self,'rim',6,24,42,30,2)
        path(self,'bucket',(8,30),('L',(12,42)),('A',2,2,False,(14,44)),('L',(34,44)),('A',2,2,False,(36,42)),('L',(40,30)))
        contacts(self)

# Exact drawing accepted under the user-authorized visual-exception workflow.
Drawing.exception = {'reason': 'Preserve the diagonal bottle neck/cap above a flared cooler with a visible rim. Compact cap and rim openings are visible in both themes.', 'approved_by': 'gpt-6 under explicit user authorization for visual exceptions', 'approved_on': '2026-09-29', 'svg_sha256': 'a6f1c52dc0bf17aa8f88c5ec5ce147534bb40c90cae4b71280ed5e633a8402a4'}
