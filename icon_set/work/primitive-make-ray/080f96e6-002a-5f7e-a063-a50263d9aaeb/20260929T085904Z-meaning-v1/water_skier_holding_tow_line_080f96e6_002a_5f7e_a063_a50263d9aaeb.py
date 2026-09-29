from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.icons.solo._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = '080f96e6-002a-5f7e-a063-a50263d9aaeb'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__water-skier-holding-tow-line/20260929T085904Z-thuan-mac/reference/nautic sports water skiing_080f96e6-002a-5f7e-a063-a50263d9aaeb.svg'
AUTHOR = "gpt-6"

# Comparison: The horizontal tow line and gripping arms disappeared, leaving a seated shape on a wave.
# Revision: Restore forward gripping hands on a straight tow line, a crouched torso and feet on an upturned ski.
# Plan: coherent subject contours; named parts own attachments; paired features share parameters.
# Human construction: icon_set/references/human_ref/full_body_ref.png; detached heads use 8 centerline / 4 ink gap at torso junction.
class Drawing(Solo48):
    icon_id = 'water-skier-holding-tow-line'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('nautic', 'sports', 'water', 'skiing')

    def build(self):
        ellipse(self,'head',12,9,5)
        path(self,'torso',(12,22),('C',(12,27),(13,30),(18,32)))
        self.mark_human_figure('skier',head='head',torso='torso-1',torso_junction='start')
        poly(self,'arm',(12,22),(26,22),(29,18))
        line(self,'rope',(29,18),(44,18))
        poly(self,'leg',(18,32),(24,33),(27,39))
        path(self,'ski',(5,39),('L',(36,39)),('A',5,5,False,(41,34)))
        path(self,'water',(5,45),('C',(13,40),(19,47),(26,44)),('C',(33,40),(38,47),(44,42)))
        contacts(self)
