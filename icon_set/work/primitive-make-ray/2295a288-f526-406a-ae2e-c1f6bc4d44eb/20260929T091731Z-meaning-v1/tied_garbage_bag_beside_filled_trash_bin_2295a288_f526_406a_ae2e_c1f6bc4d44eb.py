from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.icons.solo._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = '2295a288-f526-406a-ae2e-c1f6bc4d44eb'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__tied-garbage-bag-beside-filled-trash-bin/20260929T091731Z-thuan-mac/reference/garbage_2295a288-f526-406a-ae2e-c1f6bc4d44eb.svg'
AUTHOR = "gpt-6"

# Original/rejected comparison: The bag neck looked like a triangle on a circle, while the bin became an unrecognizable slanted frame.
# Revision: Restore a tied soft garbage bag in front of a tapered open bin with protruding rubbish.
# Symbol plan: named contours own silhouettes; paired features share dimensions and attachment nodes.
class Drawing(Solo48):
    icon_id = 'tied-garbage-bag-beside-filled-trash-bin'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('garbage',)

    def build(self):
        path(self,'bin',(24,25),('L',(23,17)),('L',(44,17)),('L',(41,44)),('L',(24,44)))
        poly(self,'rubbish',(28,17),(31,7),(41,9),(40,17))
        poly(self,'bag-tie',(11,25),(9,17),(18,15),(16,25))
        path(self,'bag',(13,25),('C',(5,25),(2,34),(4,41)),('C',(5,46),(25,46),(27,41)),('C',(29,35),(21,25),(13,25)),closed=True)
        contacts(self)

# Exact drawing accepted under the user-authorized visual-exception workflow.
Drawing.exception = {'reason': 'Preserve the soft tied bag in front of a full tapered bin. Bag/bin overlap and small tie/paper openings are visible at native size.', 'approved_by': 'gpt-6 under explicit user authorization for visual exceptions', 'approved_on': '2026-09-29', 'svg_sha256': '02a2439d41dd50c8497bc08118a65292a233dea04acee04db2642b49572ba95f'}
