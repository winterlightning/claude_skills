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
        # Open the handle/body junction and use a single larger grip window with a round lower turn.
        path(self,'handle',(6,29),('L',(15,21)),('L',(25,31)),('C',(25,36),(21,41),(16,44)),('C',(13,46),(10,43),(8,41)),('L',(4,37)),('C',(2,34),(3,32),(6,29)),closed=True)
        path(self,'grip',(10,33),('L',(14,29)),('L',(19,34)),('L',(15,38)),('A',3,3,True,(11,37)),('L',(10,33)),closed=True)
        poly(self,'blade',(16,22),(36,4),(44,11),(39,14),(39,18),(34,20),(33,25),(28,27),(25,31))
        contacts(self)
