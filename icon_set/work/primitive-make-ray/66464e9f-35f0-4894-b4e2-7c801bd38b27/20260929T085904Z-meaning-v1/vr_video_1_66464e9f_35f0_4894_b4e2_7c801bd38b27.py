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
        poly(self,'stylus',(7,5),(15,13),(17,19),(11,17),(3,9),closed=True)
        poly(self,'cube-left',(6,22),(18,27),(18,40),(6,34),closed=True)
        poly(self,'cube-top',(6,22),(17,17),(29,22),(18,27))
        line(self,'cube-right',(29,22),(29,26))
        path(self,'goggles',(26,29),('L',(40,29)),('A',4,4,True,(44,33)),('L',(44,41)),('A',3,3,True,(41,44)),('L',(37,44)),('L',(33,40)),('L',(29,44)),('L',(25,44)),('A',3,3,True,(22,41)),('L',(22,33)),('A',4,4,True,(26,29)),closed=True)
        self.add_dot('lens-left',(28,35));self.add_dot('lens-right',(38,35))
        contacts(self)
