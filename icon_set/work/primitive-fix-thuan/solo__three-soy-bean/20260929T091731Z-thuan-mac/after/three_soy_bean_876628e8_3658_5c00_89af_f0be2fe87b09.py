from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.icons.solo._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = '876628e8-3658-5c00-89af-f0be2fe87b09'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__three-soy-bean/20260929T091731Z-thuan-mac/reference/black bean_876628e8-3658-5c00-89af-f0be2fe87b09.svg'
AUTHOR = "gpt-6"

# Original/rejected comparison: Three regular hollow ovals lost the kidney-bean silhouettes and seed crease.
# Revision: Draw three organic beans with unequal tilted silhouettes and a clear crease on the upper bean.
# Symbol plan: named contours own silhouettes; paired features share dimensions and attachment nodes.
class Drawing(Solo48):
    icon_id = 'three-soy-bean'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('black', 'bean')

    def build(self):
        path(self,'bean-top',(18,6),('C',(23,1),(40,7),(43,13)),('C',(49,24),(29,24),(20,16)),('C',(15,12),(14,9),(18,6)),closed=True)
        path(self,'crease',(29,11),('C',(32,11),(34,13),(35,15)))
        path(self,'bean-left',(5,28),('C',(12,17),(22,20),(18,29)),('C',(17,33),(13,34),(12,38)),('C',(7,46),(0,37),(5,28)),closed=True)
        path(self,'bean-right',(26,29),('C',(33,25),(45,33),(44,40)),('C',(43,49),(30,43),(25,37)),('C',(22,34),(22,31),(26,29)),closed=True)
        contacts(self)

# Exact drawing accepted under the user-authorized visual-exception workflow.
Drawing.exception = {'reason': 'Keep the three organic seed silhouettes and the identifying crease. The crease and compact bean arrangement remain visible in both themes.', 'approved_by': 'gpt-6 under explicit user authorization for visual exceptions', 'approved_on': '2026-09-29', 'svg_sha256': '22b7ed21bc75553572f9049e49950462c273668b0c6f0b0f2ae56aefbc98b14e'}
