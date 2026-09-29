from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.icons.solo._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = '776076fa-8de2-42b1-9fac-cc7b5225e2bd'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__ticket-basketball-game/20260929T091731Z-thuan-mac/reference/ticket basketball game_776076fa-8de2-42b1-9fac-cc7b5225e2bd.svg'
AUTHOR = "gpt-6"

# Original/rejected comparison: The basketball and ticket fused into an arched box, and the ball seams no longer read as a basketball.
# Revision: Restore a round seamed basketball behind a diagonally notched ticket, plus the small upper ball.
# Symbol plan: named contours own silhouettes; paired features share dimensions and attachment nodes.
class Drawing(Solo48):
    icon_id = 'ticket-basketball-game'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('ticket', 'basketball', 'game')

    def build(self):
        path(self,'basketball',(10,30),('C',(1,26),(0,11),(10,6)),('C',(19,0),(31,8),(31,18)),('C',(31,22),(29,24),(27,26)))
        path(self,'ball-seam-a',(4,18),('C',(14,20),(23,14),(28,10)))
        path(self,'ball-seam-b',(10,6),('C',(20,13),(19,22),(24,27)))
        ellipse(self,'small-ball',42,7,4)
        path(self,'ticket',(14,30),('L',(39,22)),('L',(41,28)),('C',(35,30),(38,35),(43,33)),('L',(44,38)),('L',(19,46)),('L',(17,40)),('C',(23,38),(20,33),(15,35)),('L',(14,30)),closed=True)
        line(self,'ticket-label',(26,36),(34,33))
        contacts(self)

# Exact drawing accepted under the user-authorized visual-exception workflow.
Drawing.exception = {'reason': 'Keep the seamed basketball behind the angled notched ticket, plus the small upper ball. Compact ticket marks and occluded ball joins remain legible at 48px.', 'approved_by': 'gpt-6 under explicit user authorization for visual exceptions', 'approved_on': '2026-09-29', 'svg_sha256': '7a8fca11060b21b6ff28c2d1b3f7bf9fd6f12cd43002d30dd320dbb8927c4fb9'}
