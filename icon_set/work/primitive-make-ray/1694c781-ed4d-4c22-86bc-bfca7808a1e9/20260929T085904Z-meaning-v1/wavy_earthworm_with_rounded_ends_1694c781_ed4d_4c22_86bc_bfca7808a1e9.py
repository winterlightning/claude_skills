from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.icons.solo._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = '1694c781-ed4d-4c22-86bc-bfca7808a1e9'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__wavy-earthworm-with-rounded-ends/20260929T085904Z-thuan-mac/reference/earthworm_1694c781-ed4d-4c22-86bc-bfca7808a1e9.svg'
AUTHOR = "gpt-6"

# Comparison: The earthworm lost its two bends and became a closed peanut-shaped loop.
# Revision: Rebuild a continuous worm with two alternating bends, rounded endpoints and a clearly tubular silhouette.
# Plan: coherent subject contours; named parts own attachments; paired features share parameters.
class Drawing(Solo48):
    icon_id = 'wavy-earthworm-with-rounded-ends'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('earthworm',)

    def build(self):
        path(self,'worm',(6,36),('C',(12,36),(8,10),(18,10)),('C',(30,10),(22,34),(32,34)),('C',(39,34),(29,6),(42,6)),('A',4,4,True,(42,14)),('C',(36,14),(47,42),(32,42)),('C',(15,42),(24,18),(18,18)),('C',(14,18),(22,44),(6,44)),('A',4,4,True,(6,36)),closed=True)
        contacts(self)
