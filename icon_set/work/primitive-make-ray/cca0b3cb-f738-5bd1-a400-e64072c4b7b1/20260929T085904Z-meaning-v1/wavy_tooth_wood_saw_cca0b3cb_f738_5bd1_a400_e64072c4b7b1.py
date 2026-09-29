from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.icons.solo._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = 'cca0b3cb-f738-5bd1-a400-e64072c4b7b1'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__wavy-tooth-wood-saw/20260929T085904Z-thuan-mac/reference/tools wood saw_cca0b3cb-f738-5bd1-a400-e64072c4b7b1.svg'
AUTHOR = "gpt-6"

# Comparison: The rigid square grip and rectangular stair-step teeth read as a key rather than a wood saw.
# Revision: Restore an ergonomic rounded grip, enclosed finger opening and repeated saw teeth on a tapered diagonal blade.
# Plan: coherent subject contours; named parts own attachments; paired features share parameters.
class Drawing(Solo48):
    icon_id = 'wavy-tooth-wood-saw'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('tools', 'wood', 'saw')

    def build(self):
        path(self,'handle',(6,30),('L',(15,22)),('L',(24,31)),('C',(26,35),(23,38),(20,41)),('L',(16,44)),('C',(14,46),(11,44),(9,42)),('L',(4,37)),('C',(2,35),(3,33),(6,30)),closed=True)
        path(self,'grip',(9,34),('L',(14,29)),('L',(19,34)),('A',4,4,True,(14,39)),('L',(9,34)),closed=True)
        poly(self,'blade',(16,23),(36,4),(44,11),(39,14),(39,18),(34,20),(33,25),(28,27),(26,32),(24,33))
        contacts(self)
