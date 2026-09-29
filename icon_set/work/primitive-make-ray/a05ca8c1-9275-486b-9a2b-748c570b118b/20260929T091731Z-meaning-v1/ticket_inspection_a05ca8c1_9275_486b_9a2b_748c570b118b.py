from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.icons.solo._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = 'a05ca8c1-9275-486b-9a2b-748c570b118b'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__ticket-inspection/20260929T091731Z-thuan-mac/reference/information desk ticket_a05ca8c1-9275-486b-9a2b-748c570b118b.svg'
AUTHOR = "gpt-6"

# Original/rejected comparison: The two people lost their torsos and legs and the ticket was placed between their shoulders instead of in a raised hand.
# Revision: Restore two standing figures, with one raising a ticket and the other reaching to inspect it.
# Symbol plan: named contours own silhouettes; paired features share dimensions and attachment nodes.
class Drawing(Solo48):
    icon_id = 'ticket-inspection'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('information', 'desk', 'ticket')

    def build(self):
        for x in (10,38):
         ellipse(self,f'head-{x}',x,8,4)
         line(self,f'torso-{x}',(x,20),(x,32))
         self.mark_human_figure(f'person-{x}',head=f'head-{x}',torso=f'torso-{x}',torso_junction='start')
         poly(self,f'legs-{x}',(x-4,44),(x,32),(x+4,44))
        poly(self,'raised-arm',(10,20),(19,20),(23,12))
        box(self,'ticket',21,4,29,12,1)
        path(self,'checking-arm',(38,20),('C',(30,20),(32,29),(22,30)))
        line(self,'left-outer-arm',(10,20),(5,29))
        line(self,'right-outer-arm',(38,20),(44,29))
        contacts(self)

# Exact drawing accepted under the user-authorized visual-exception workflow.
Drawing.exception = {'reason': 'Keep two full standing figures with an elevated ticket and a reaching inspector. Both detached head gaps are exactly 4px; compact head-to-ticket spacing preserves the scene.', 'approved_by': 'gpt-6 under explicit user authorization for visual exceptions', 'approved_on': '2026-09-29', 'svg_sha256': '72c1879de7d230f37e92ab848b570dd89719fa2b4c0bd11ab4f70fcb9eaff837'}
