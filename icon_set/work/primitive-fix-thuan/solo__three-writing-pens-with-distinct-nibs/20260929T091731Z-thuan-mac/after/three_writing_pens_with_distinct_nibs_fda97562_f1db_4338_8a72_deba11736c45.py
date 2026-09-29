from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.icons.solo._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = 'fda97562-f1db-4338-8a72-deba11736c45'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__three-writing-pens-with-distinct-nibs/20260929T091731Z-thuan-mac/reference/pens_fda97562-f1db-4338-8a72-deba11736c45.svg'
AUTHOR = "gpt-6"

# Original/rejected comparison: The three pens became nearly identical pointed bars and lost their clips and distinct nib shapes.
# Revision: Restore a fountain nib, sharpened pencil and fine-tip pen, with different barrel tops and clear tip structures.
# Symbol plan: named contours own silhouettes; paired features share dimensions and attachment nodes.
class Drawing(Solo48):
    icon_id = 'three-writing-pens-with-distinct-nibs'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('pens',)

    def build(self):
        box(self,'fountain-barrel',4,6,14,29,2)
        path(self,'fountain-nib',(4,29),('C',(3,34),(7,39),(9,43)),('C',(11,39),(15,34),(14,29)))
        path(self,'clip-left',(4,10),('C',(2,10),(2,12),(2,16)),('L',(2,23)))
        path(self,'pencil',(20,28),('L',(20,8)),('A',4,4,True,(28,8)),('L',(28,28)),('L',(24,44)),('L',(20,28)),closed=True)
        line(self,'pencil-band',(20,13),(28,13))
        box(self,'pen-barrel',34,6,42,32,1)
        poly(self,'fine-nib',(36,32),(36,37),(40,37),(40,32))
        line(self,'pen-tip',(38,37),(38,44))
        path(self,'clip-right',(42,10),('C',(44,10),(44,12),(44,16)),('L',(44,23)))
        contacts(self)

# Exact drawing accepted under the user-authorized visual-exception workflow.
Drawing.exception = {'reason': 'Preserve three distinct writing instruments and their identifying tip shapes. Compact barrel gaps, clips and nib openings are visible at 48px.', 'approved_by': 'gpt-6 under explicit user authorization for visual exceptions', 'approved_on': '2026-09-29', 'svg_sha256': '0dfa965f2c28db14551dbd1bd5226b27ec5348013f654da179983e1d77051d56'}
