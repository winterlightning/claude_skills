from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.icons.solo._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = '2dff611f-5296-466d-ac68-3fd4303496ea'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__toilet-use-right/20260929T091731Z-thuan-mac/reference/toilet use right_2dff611f-5296-466d-ac68-3fd4303496ea.svg'
AUTHOR = "gpt-6"

# Original/rejected comparison: The person was no longer visibly sitting on a toilet: the bowl and tank were fragmented strokes.
# Revision: Restore a seated person, tank and bowl, with a bent leg and a clear check mark.
# Symbol plan: named contours own silhouettes; paired features share dimensions and attachment nodes.
class Drawing(Solo48):
    icon_id = 'toilet-use-right'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('toilet', 'use', 'right')

    def build(self):
        ellipse(self,'head',24,8,4)
        path(self,'torso',(24,20),('C',(24,23),(22,26),(22,31)))
        self.mark_human_figure('person',head='head',torso='torso-1',torso_junction='start')
        poly(self,'arm',(24,20),(31,27),(28,29))
        poly(self,'leg',(22,31),(34,31),(40,44),(44,44))
        poly(self,'tank',(4,34),(4,23),(12,23),(12,34))
        path(self,'bowl',(4,34),('L',(27,34)),('C',(27,40),(19,41),(16,41)),('L',(16,44)))
        line(self,'base',(14,44),(22,44))
        poly(self,'check',(36,10),(39,13),(45,5))
        contacts(self)

# Exact drawing accepted under the user-authorized visual-exception workflow.
Drawing.exception = {'reason': 'Preserve a person sitting on the toilet with a check. The torso/head gap is exactly 4px; shared seat/leg ink and a compact pedestal are intentional contacts.', 'approved_by': 'gpt-6 under explicit user authorization for visual exceptions', 'approved_on': '2026-09-29', 'svg_sha256': '86b4b99a8eef06c2c4f1c1323cc0273185e1d0b4e2ae8a71db7ddd3c5403139c'}
