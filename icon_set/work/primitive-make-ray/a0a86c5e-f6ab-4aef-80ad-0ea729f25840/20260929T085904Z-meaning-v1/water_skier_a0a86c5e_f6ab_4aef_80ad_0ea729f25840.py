from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.icons.solo._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = 'a0a86c5e-f6ab-4aef-80ad-0ea729f25840'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__water-skier/20260929T085904Z-thuan-mac/reference/skating_a0a86c5e-f6ab-4aef-80ad-0ea729f25840.svg'
AUTHOR = "gpt-6"

# Comparison: The skier became a head, diagonal arm and wave with no recognizable ski or crouched legs.
# Revision: Show a crouched skier gripping a tow rope, with bent knees and a separate upturned ski.
# Plan: coherent subject contours; named parts own attachments; paired features share parameters.
# Human construction: icon_set/references/human_ref/full_body_ref.png; detached heads use 8 centerline / 4 ink gap at torso junction.
class Drawing(Solo48):
    icon_id = 'water-skier'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('skating',)

    def build(self):
        ellipse(self,'head',13,9,5)
        line(self,'torso',(13,22),(16,30))
        self.mark_human_figure('skier',head='head',torso='torso',torso_junction='start')
        poly(self,'arms',(13,22),(24,25),(31,21))
        line(self,'tow-rope',(31,21),(44,16))
        poly(self,'legs',(16,30),(26,32),(29,39))
        path(self,'ski',(6,39),('L',(37,39)),('A',5,5,False,(42,34)))
        path(self,'water',(6,45),('C',(13,41),(18,47),(25,44)),('C',(31,41),(38,47),(43,43)))
        contacts(self)
