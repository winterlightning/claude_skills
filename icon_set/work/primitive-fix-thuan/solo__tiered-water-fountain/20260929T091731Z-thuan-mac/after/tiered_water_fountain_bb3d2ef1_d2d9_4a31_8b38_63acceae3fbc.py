from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.icons.solo._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = 'bb3d2ef1-d2d9-4a31-8b38-63acceae3fbc'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__tiered-water-fountain/20260929T091731Z-thuan-mac/reference/park fonutain_bb3d2ef1-d2d9-4a31-8b38-63acceae3fbc.svg'
AUTHOR = "gpt-6"

# Original/rejected comparison: The curved basins became a trapezoid and an oval, and the water jets were reduced to two dots.
# Revision: Restore two rounded basins, a central pedestal and paired arcing water jets.
# Symbol plan: named contours own silhouettes; paired features share dimensions and attachment nodes.
class Drawing(Solo48):
    icon_id = 'tiered-water-fountain'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('park', 'fonutain')

    def build(self):
        path(self,'lower-basin',(4,32),('L',(44,32)),('A',20,10,True,(4,32)),closed=True)
        path(self,'upper-basin',(12,20),('L',(36,20)),('A',12,7,True,(12,20)),closed=True)
        line(self,'column',(24,27),(24,32))
        line(self,'pedestal',(24,42),(24,45))
        line(self,'base',(17,45),(31,45))
        line(self,'jet',(24,20),(24,9))
        path(self,'jet-left',(24,9),('C',(24,0),(14,1),(14,9)))
        path(self,'jet-right',(24,9),('C',(24,0),(34,1),(34,9)))
        contacts(self)

# Exact drawing accepted under the user-authorized visual-exception workflow.
Drawing.exception = {'reason': 'Preserve two curved basins and arcing water jets. Bowl openings, real pedestal contacts and the tall fountain envelope remain clear at 48px.', 'approved_by': 'gpt-6 under explicit user authorization for visual exceptions', 'approved_on': '2026-09-29', 'svg_sha256': 'cff0fd5ad5dd296377e20a64271c34b31ea13fcf651924d9383b32f82a36c858'}
