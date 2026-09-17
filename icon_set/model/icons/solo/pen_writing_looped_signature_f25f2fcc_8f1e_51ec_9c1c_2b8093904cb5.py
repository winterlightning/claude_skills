"""Pen and Signature.
Plan: Diagonal pen at left and looped signature flowing right below. Extrema (6,6)-(42,42).
Reference: Lucide pen: simple diagonal barrel and pointed nib.
Reduction: Pen seam reduced to one nib divider; one broad signature loop retained.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f25f2fcc-8f1e-51ec-9c1c-2b8093904cb5'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/files/fill and sign_f25f2fcc-8f1e-51ec-9c1c-2b8093904cb5.svg'
AUTHOR = 'gpt-6'

class Batch29Icon(Solo48):
    icon_id = 'pen-writing-looped-signature'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/agriculture"
    aliases = ()
    keywords = ('pen', 'and', 'signature')

    def build(self):

        self.add_polyline('pen',(6,30),(10,18),(18,6),(26,10),(18,24),(6,30))
        self.add_line('nib',(10,18),(18,24));self.relate('connect','pen','nib')
        self.add_bezier('signature',(6,42),((16,42),(30,36),(34,28)),((40,16),(24,22),(26,34)),((28,46),(34,42),(38,38)),((40,42),(41,42),(42,42)))
