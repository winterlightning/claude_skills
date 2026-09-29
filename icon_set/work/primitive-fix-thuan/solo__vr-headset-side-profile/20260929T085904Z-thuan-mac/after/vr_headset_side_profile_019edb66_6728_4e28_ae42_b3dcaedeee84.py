from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.icons.solo._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = '019edb66-6728-4e28-ae42-b3dcaedeee84'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__vr-headset-side-profile/20260929T085904Z-thuan-mac/reference/vr headset 1_019edb66-6728-4e28-ae42-b3dcaedeee84.svg'
AUTHOR = "gpt-6"

# Comparison: The lower face collapsed into a stair-step hook and the headset looked like a loose oval.
# Revision: Rebuild a left-facing head with a broad visor, strap, distinct nose and rounded chin.
# Plan: coherent subject contours; named parts own attachments; paired features share parameters.
class Drawing(Solo48):
    icon_id = 'vr-headset-side-profile'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('vr', 'headset', '1')

    def build(self):
        path(self,'skull',(34,44),('L',(34,36)),('C',(43,27),(43,16),(36,9)),('C',(28,1),(18,4),(13,12)))
        box(self,'visor',6,12,23,26,4)
        line(self,'strap',(40,21),(23,21))
        path(self,'face',(11,26),('L',(8,33)),('L',(13,34)),('L',(13,36)),('A',5,5,False,(18,41)),('L',(22,41)),('L',(22,44)))
        contacts(self)

# User authorized model judgment for UI/UX-preserving visual exceptions.
Drawing.exception = {'reason': 'Retain the original broad visor and left-facing anatomical profile; accept the wider envelope and short nose/visor junction clearance.', 'approved_by': 'gpt-6 under explicit user authorization for visual exceptions', 'approved_on': '2026-09-29', 'svg_sha256': '60be4d04488565b2d8308ff1092e6b16d6244502b136526b16f1dfaa326b5050'}
