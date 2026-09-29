from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.icons.solo._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = 'e7507033-a4fb-4857-8a9a-208685a6411c'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__three-women-pyramid/20260929T091731Z-thuan-mac/reference/user multiple half female group_e7507033-a4fb-4857-8a9a-208685a6411c.svg'
AUTHOR = "gpt-6"

# Original/rejected comparison: Only the top portrait had a recognizable body; the bottom pair became hair-framed dots without shoulders.
# Revision: Restore three female busts in a pyramid, with parted hair and visible shoulders for the lower pair.
# Symbol plan: named contours own silhouettes; paired features share dimensions and attachment nodes.
class Drawing(Solo48):
    icon_id = 'three-women-pyramid'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('user', 'multiple', 'half', 'female', 'group')
    human_construction = "bust"

    def build(self):
        # Shared human bust reference; circular heads and shoulder contact at 4 centerline units.
        for x,y,r in [(24,11,6),(11,30,6),(37,30,6)]:
         ellipse(self,f'head-{x}',x,y,r)
         path(self,f'hair-{x}',(x-r,y-1),('C',(x-3,y-1),(x-1,y-3),(x,y-4)),('C',(x+1,y-3),(x+3,y-1),(x+r,y-1)))
         poly(self,f'lock-left-{x}',(x-r,y),(x-r-2,y+6))
         poly(self,f'lock-right-{x}',(x+r,y),(x+r+2,y+6))
        path(self,'shoulders-top',(17,25),('C',(17,22),(20,21),(24,21)),('C',(28,21),(31,22),(31,25)))
        for x in (11,37):
         path(self,f'shoulders-{x}',(x-8,44),('A',8,4,True,(x,40)),('A',8,4,True,(x+8,44)))
         self.relate('connect',f'head-{x}',f'shoulders-{x}')
        self.relate('connect','head-24','shoulders-top')
        contacts(self)

# Exact drawing accepted under the user-authorized visual-exception workflow.
Drawing.exception = {'reason': 'Preserve three parted-hair female portraits with shoulders. Hair caps and small face openings remain readable at 48px; overlapping shoulder/hair details are intentional.', 'approved_by': 'gpt-6 under explicit user authorization for visual exceptions', 'approved_on': '2026-09-29', 'svg_sha256': '3d0c56ac665f9b1dcbd667b675df4dd65bf4589b18ba3c6cda03958f2e5b6c51'}
