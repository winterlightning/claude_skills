from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.icons.solo._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = '60df543d-dca5-4914-a5c9-114df422b161'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__witch-in-pointed-hat/20260929T085904Z-thuan-mac/reference/witch_60df543d-dca5-4914-a5c9-114df422b161.svg'
AUTHOR = "gpt-6"

# Comparison: The witch lost her eye, mouth, chin and bent hat tip, becoming a pointed hat over an anonymous hook.
# Revision: Restore a hooked nose, eye and smiling mouth beneath a floppy pointed hat, with flowing hair at the back.
# Plan: coherent subject contours; named parts own attachments; paired features share parameters.
class Drawing(Solo48):
    icon_id = 'witch-in-pointed-hat'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('witch',)

    def build(self):
        path(self,'hat',(14,18),('C',(21,9),(31,4),(38,4)),('C',(45,4),(42,13),(44,20)),('L',(36,12)),('L',(32,25)))
        path(self,'brim',(14,18),('C',(9,12),(5,12),(7,17)),('C',(12,25),(25,31),(35,32)))
        path(self,'face',(12,24),('L',(7,29)),('L',(4,30)),('A',3,3,False,(7,33)),('L',(9,33)),('L',(8,38)),('C',(7,44),(16,46),(23,41)))
        self.add_dot('eye',(15,29))
        path(self,'smile',(10,37),('C',(14,38),(17,37),(19,35)))
        path(self,'hair',(27,30),('C',(25,37),(35,36),(34,44)))
        contacts(self)

# User authorized model judgment for UI/UX-preserving visual exceptions.
Drawing.exception = {'reason': 'Retain the bent hat tip, brim, hooked nose, eye, smile and hair. Connected facial/hat ink and compact facial spacing are intentional and legible at 48px.', 'approved_by': 'gpt-6 under explicit user authorization for visual exceptions', 'approved_on': '2026-09-29', 'svg_sha256': 'ae2a7ba0e8a650aaf52110fb176389540b115b1258e9bfaacb88334fa9012edc'}
