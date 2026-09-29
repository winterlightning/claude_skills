from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.icons.solo._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = '333b76cc-b37e-568d-8fc3-aa0f76f2f559'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__vr-headset/20260929T085904Z-thuan-mac/reference/vr headset_333b76cc-b37e-568d-8fc3-aa0f76f2f559.svg'
AUTHOR = "gpt-6"

# Comparison: The visor merged into the skull and the face had a stair-step jaw rather than a recognizable profile.
# Revision: Separate the broad visor, horizontal strap, forehead, nose and rounded chin in a coherent head silhouette.
# Plan: coherent subject contours; named parts own attachments; paired features share parameters.
class Drawing(Solo48):
    icon_id = 'vr-headset'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('vr', 'headset')

    def build(self):
        path(self,'skull',(14,44),('L',(14,36)),('C',(5,27),(5,16),(12,9)),('C',(20,1),(30,4),(35,12)))
        box(self,'visor',25,12,42,26,4)
        line(self,'strap',(8,21),(25,21))
        path(self,'face',(37,26),('L',(40,33)),('L',(35,34)),('L',(35,36)),('A',5,5,True,(30,41)),('L',(26,41)),('L',(26,44)))
        contacts(self)

# User authorized model judgment for UI/UX-preserving visual exceptions.
Drawing.exception = {'reason': 'Retain the original broad visor and natural face profile; accept a wider head envelope and the short nose/visor junction clearance.', 'approved_by': 'gpt-6 under explicit user authorization for visual exceptions', 'approved_on': '2026-09-29', 'svg_sha256': '17effe0e88f5ab13a9249644f32f1595fc7972deda0c01467cecd3d62f9bbf91'}
