from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.icons.solo._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = 'af4b0bcf-b76c-4768-8a09-e4eb2d20860e'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__three-tined-spork-with-rounded-handle/20260929T091731Z-thuan-mac/reference/spork_af4b0bcf-b76c-4768-8a09-e4eb2d20860e.svg'
AUTHOR = "gpt-6"

# Original/rejected comparison: The utensil looked like a short-handled trident, with no spoon bowl and no long handle.
# Revision: Restore a rounded spoon bowl, three short tines and a long narrow handle with a round end.
# Symbol plan: named contours own silhouettes; paired features share dimensions and attachment nodes.
class Drawing(Solo48):
    icon_id = 'three-tined-spork-with-rounded-handle'
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('spork',)

    def build(self):
        path(self,'spork-outline',(14,4),('C',(7,16),(10,23),(20,25)),('L',(20,40)),('A',4,4,False,(28,40)),('L',(28,25)),('C',(38,23),(41,16),(34,4)))
        path(self,'tines',(14,4),('L',(14,12)),('A',5,5,False,(24,12)),('L',(24,4)),('L',(24,12)),('A',5,5,False,(34,12)),('L',(34,4)))
        contacts(self)
