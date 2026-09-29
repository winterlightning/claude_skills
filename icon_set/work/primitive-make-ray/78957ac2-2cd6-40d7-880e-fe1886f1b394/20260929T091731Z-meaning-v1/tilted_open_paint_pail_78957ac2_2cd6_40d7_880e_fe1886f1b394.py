from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.icons.solo._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = '78957ac2-2cd6-40d7-880e-fe1886f1b394'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__tilted-open-paint-pail/20260929T091731Z-thuan-mac/reference/color bucket_78957ac2-2cd6-40d7-880e-fe1886f1b394.svg'
AUTHOR = "gpt-6"

# Original/rejected comparison: The open pail mouth became a pill-shaped capsule and the drip became a circular ring.
# Revision: Restore an elliptical tilted opening, a deep pail body and a pointed paint drop.
# Symbol plan: named contours own silhouettes; paired features share dimensions and attachment nodes.
class Drawing(Solo48):
    icon_id = 'tilted-open-paint-pail'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('color', 'bucket')

    def build(self):
        path(self,'rim',(23,5),('C',(27,1),(48,21),(43,25)),('C',(39,29),(18,9),(23,5)),closed=True)
        path(self,'pail',(23,5),('L',(5,28)),('C',(2,32),(15,45),(20,43)),('L',(43,25)))
        path(self,'paint-drop',(40,33),('C',(36,39),(35,42),(38,44)),('C',(45,47),(47,41),(40,33)),closed=True)
        contacts(self)

# Exact drawing accepted under the user-authorized visual-exception workflow.
Drawing.exception = {'reason': 'Preserve the tilted elliptical opening and separate pointed drip; the wider natural envelope and compact pail/drop clearance remain clear.', 'approved_by': 'gpt-6 under explicit user authorization for visual exceptions', 'approved_on': '2026-09-29', 'svg_sha256': '810d2365f7b080dfcb07c882e40346f2601568fb1e9162418e34124a83f3328f'}
