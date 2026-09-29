from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.icons.solo._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = '7e29c513-d49d-4943-a3b9-d82d5a705611'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__three-pin-cluster/20260929T091731Z-thuan-mac/reference/trip pin multiple_7e29c513-d49d-4943-a3b9-d82d5a705611.svg'
AUTHOR = "gpt-6"

# Original/rejected comparison: The back pins became tall triangular ears and lost their rounded teardrop proportions.
# Revision: Restore three rounded map pins in an overlapping triangular cluster, with a tapered foreground point.
# Symbol plan: named contours own silhouettes; paired features share dimensions and attachment nodes.
class Drawing(Solo48):
    icon_id = 'three-pin-cluster'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('trip', 'pin', 'multiple')

    def build(self):
        path(self,'pin-left',(20,15),('C',(21,2),(5,2),(4,12)),('C',(2,18),(8,26),(12,30)),('L',(15,27)))
        path(self,'pin-right',(28,15),('C',(27,2),(43,2),(44,12)),('C',(46,18),(40,26),(36,30)),('L',(33,27)))
        path(self,'pin-front',(24,44),('C',(21,37),(14,30),(14,25)),('C',(14,12),(34,12),(34,25)),('C',(34,30),(27,37),(24,44)),closed=True)
        contacts(self)

# Exact drawing accepted under the user-authorized visual-exception workflow.
Drawing.exception = {'reason': 'Keep the overlapping three-pin composition and rounded rear pins; local overlap and the wider envelope preserve their clear native-size silhouettes.', 'approved_by': 'gpt-6 under explicit user authorization for visual exceptions', 'approved_on': '2026-09-29', 'svg_sha256': '90d6bfe68e564c1f70dc0707434b15c2aef2ad923fb2aecce13cb91db685eaab'}
