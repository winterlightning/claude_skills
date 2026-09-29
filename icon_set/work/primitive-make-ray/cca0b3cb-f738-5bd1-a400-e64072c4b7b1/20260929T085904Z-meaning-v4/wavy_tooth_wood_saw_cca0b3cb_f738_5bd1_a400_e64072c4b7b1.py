from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.icons.solo._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = 'cca0b3cb-f738-5bd1-a400-e64072c4b7b1'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__wavy-tooth-wood-saw/20260929T085904Z-thuan-mac/reference/tools wood saw_cca0b3cb-f738-5bd1-a400-e64072c4b7b1.svg'
AUTHOR = "gpt-6"

# Comparison: The rigid square grip and rectangular stair-step teeth read as a key rather than a wood saw.
# Revision: Restore an ergonomic rounded grip, enclosed finger opening and repeated saw teeth on a tapered diagonal blade.
# Plan: coherent subject contours; named parts own attachments; paired features share parameters.
class Drawing(Solo48):
    icon_id = 'wavy-tooth-wood-saw'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('tools', 'wood', 'saw')

    def build(self):
        path(self,'handle',(14,19),('L',(28,33)),('L',(19,42)),('C',(16,46),(12,44),(9,41)),('L',(4,36)),('C',(1,33),(4,29),(7,26)),('L',(14,19)),closed=True)
        path(self,'grip',(9,31),('L',(14,26)),('L',(22,34)),('L',(17,39)),('L',(9,31)),closed=True)
        poly(self,'blade',(15,20),(36,4),(44,11),(39,14),(39,18),(34,20),(33,25),(28,27),(28,33))
        contacts(self)

# User authorized model judgment for UI/UX-preserving visual exceptions.
Drawing.exception = {'reason': 'Retain a separate ergonomic grip opening and a tapered toothed blade; the compact handle border and envelope preserve the saw identity at native size.', 'approved_by': 'gpt-6 under explicit user authorization for visual exceptions', 'approved_on': '2026-09-29', 'svg_sha256': 'e004e460c46aa39719d6ca4d6ba2fe57cf997d139e77915f19fb18f0742c796e'}
