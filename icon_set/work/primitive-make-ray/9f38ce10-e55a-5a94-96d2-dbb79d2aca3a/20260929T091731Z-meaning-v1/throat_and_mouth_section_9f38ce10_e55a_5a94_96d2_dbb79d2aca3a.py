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
        path(self,'head',(12,14),('C',(12,6),(17,4),(24,4)),('C',(40,4),(48,20),(40,30)),('C',(36,35),(39,40),(40,44)))
        poly(self,'nose-lip',(12,14),(6,22),(11,23),(11,27))
        path(self,'palate',(11,23),('C',(29,16),(36,27),(36,44)))
        path(self,'mouth-floor',(11,27),('C',(23,23),(29,29),(29,44)))
        path(self,'chin',(12,32),('C',(12,38),(22,36),(22,40)),('L',(22,44)))
        contacts(self)
