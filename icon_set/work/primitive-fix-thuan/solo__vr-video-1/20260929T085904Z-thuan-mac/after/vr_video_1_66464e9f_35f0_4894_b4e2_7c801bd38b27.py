from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.icons.solo._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = '66464e9f-35f0-4894-b4e2-7c801bd38b27'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__vr-video-1/20260929T085904Z-thuan-mac/reference/vr video 1_66464e9f-35f0-4894-b4e2-7c801bd38b27.svg'
AUTHOR = "gpt-6"

# Comparison: The stylus was reduced to a floating dash, cube became an angular fragment, and goggles lost both lenses.
# Revision: Restore a pointed stylus, a three-face cube and a compact VR mask with paired lenses.
# Plan: coherent subject contours; named parts own attachments; paired features share parameters.
class Drawing(Solo48):
    icon_id = 'vr-video-1'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('vr', 'video', '1')

    def build(self):
        # The cube is visibly behind the goggles; break the concealed wall instead of nearly touching it.
        poly(self,'stylus',(6,5),(13,12),(15,17),(10,15),(3,8),closed=True)
        poly(self,'cube-left',(6,23),(17,28),(17,40),(6,35),closed=True)
        poly(self,'cube-top',(6,23),(17,18),(28,23),(17,28))
        path(self,'goggles',(26,30),('L',(39,30)),('A',4,4,True,(43,34)),('L',(43,41)),('A',3,3,True,(40,44)),('L',(37,44)),('L',(33,40)),('L',(29,44)),('L',(26,44)),('A',4,4,True,(22,40)),('L',(22,34)),('A',4,4,True,(26,30)),closed=True)
        self.add_dot('lens-left',(28,35));self.add_dot('lens-right',(38,35))
        contacts(self)

# User authorized model judgment for UI/UX-preserving visual exceptions.
Drawing.exception = {'reason': 'Preserve all three identifying components: stylus, perspective cube and two-lens VR mask. Compact symbol gaps and stylus opening remain legible at native size.', 'approved_by': 'gpt-6 under explicit user authorization for visual exceptions', 'approved_on': '2026-09-29', 'svg_sha256': '2586a05b6513549e7c8206009745988be623009adc31d0bdfec856c48f609849'}
