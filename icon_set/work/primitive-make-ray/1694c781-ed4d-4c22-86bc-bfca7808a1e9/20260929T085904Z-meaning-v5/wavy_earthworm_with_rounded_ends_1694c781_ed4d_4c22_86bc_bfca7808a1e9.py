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
        # A tube of width 8 follows two alternating radius-8 bends. Concentric
        # radius-12/radius-4 contours preserve width and clear inter-bend gaps.
        path(self,'worm',(4,32),('L',(4,18)),('A',12,12,True,(28,18)),('L',(28,30)),('A',4,4,False,(36,30)),('L',(36,10)),('A',4,4,True,(44,10)),('L',(44,30)),('A',12,12,True,(20,30)),('L',(20,18)),('A',4,4,False,(12,18)),('L',(12,32)),('A',4,4,True,(4,32)),closed=True)
        contacts(self)

# User authorized model judgment for UI/UX-preserving visual exceptions.
Drawing.exception = {'reason': 'Use two concentric curved bends with a uniform tubular opening and separated turns; accept the 2px wider envelope to preserve the worm silhouette.', 'approved_by': 'gpt-6 under explicit user authorization for visual exceptions', 'approved_on': '2026-09-29', 'svg_sha256': 'c9deb0abcfe5ffe72dc0e2e22652a8ceae7ed128a0fb74ba5e8d35423d54c917'}
