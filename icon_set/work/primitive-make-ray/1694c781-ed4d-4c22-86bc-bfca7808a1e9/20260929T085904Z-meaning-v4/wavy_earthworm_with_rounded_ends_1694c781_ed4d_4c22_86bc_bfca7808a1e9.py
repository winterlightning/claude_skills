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
        # Construct the tube with concentric 10/2 radii: a constant 8-unit boundary width.
        path(self,'worm',(8,32),('L',(8,20)),('A',10,10,True,(28,20)),('L',(28,30)),('A',2,2,False,(32,30)),('L',(32,10)),('A',4,4,True,(40,10)),('L',(40,30)),('A',10,10,True,(20,30)),('L',(20,20)),('A',2,2,False,(16,20)),('L',(16,32)),('A',8,8,True,(8,40)),('A',4,4,True,(8,32)),closed=True)
        contacts(self)
