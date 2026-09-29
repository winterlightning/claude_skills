from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.icons.solo._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = '9dfb6289-487a-4bfa-95e5-fdc48e5dd47a'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__wheelchair-user-at-ramp/20260929T085904Z-thuan-mac/reference/wheelchair way_9dfb6289-487a-4bfa-95e5-fdc48e5dd47a.svg'
AUTHOR = "gpt-6"

# Comparison: The wheelchair wheel was an isolated C and the person lacked bent knees and feet.
# Revision: Restore a circular wheel, aligned head and seated torso with a forward arm and bent leg beside a sloped ramp.
# Plan: coherent subject contours; named parts own attachments; paired features share parameters.
# Human construction: icon_set/references/human_ref/full_body_ref.png; detached heads use 8 centerline / 4 ink gap at torso junction.
class Drawing(Solo48):
    icon_id = 'wheelchair-user-at-ramp'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('wheelchair', 'way')

    def build(self):
        ellipse(self,'head',16,8,4)
        line(self,'torso',(16,20),(16,29))
        self.mark_human_figure('rider',head='head',torso='torso',torso_junction='start')
        line(self,'arm',(16,20),(25,22))
        poly(self,'leg',(16,29),(24,29),(30,37))
        path(self,'wheel',(10,23),('A',10,10,False,(22,39)))
        poly(self,'ramp',(24,44),(44,33),(44,44))
        contacts(self)
