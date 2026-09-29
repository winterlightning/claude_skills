from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.icons.solo._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = 'e6758494-42bf-4f9d-b4a8-0893ebe568ab'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__webhook-triangle/20260929T085904Z-thuan-mac/reference/web hook_e6758494-42bf-4f9d-b4a8-0893ebe568ab.svg'
AUTHOR = "gpt-6"

# Comparison: The three hooked nodes lost all connecting arms, so the webhook logo became unrelated curved fragments.
# Revision: Restore three open circular terminals linked in a triangular cycle, preserving their hook openings.
# Plan: coherent subject contours; named parts own attachments; paired features share parameters.
class Drawing(Solo48):
    icon_id = 'webhook-triangle'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('web', 'hook')

    def build(self):
        path(self,'top-hook',(28,7),('A',8,8,False,(16,16)),('L',(10,30)))
        path(self,'left-hook',(4,31),('A',8,8,False,(18,38)),('L',(35,38)))
        path(self,'right-hook',(36,44),('A',8,8,False,(35,29)),('L',(24,12)))
        contacts(self)

# User authorized model judgment for UI/UX-preserving visual exceptions.
Drawing.exception = {'reason': 'Keep all three hooked terminals and their triangular connecting arms; native-size terminal openings remain clear with spacing below the strict profile minimum.', 'approved_by': 'gpt-6 under explicit user authorization for visual exceptions', 'approved_on': '2026-09-29', 'svg_sha256': 'b94b4e996fd311812b0cc90ca583715f91046a58fc4c88163456d4f13a9795a2'}
