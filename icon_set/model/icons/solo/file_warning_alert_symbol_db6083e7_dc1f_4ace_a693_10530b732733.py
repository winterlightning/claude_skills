"""File Warning Alert Symbol. Reference retains the complete subject following saved user classification.
Plan: VRECT_L envelope; shared page/currency dimensions and true beam attachment nodes.
Lucide files informs page contour continuity; dollar-sign informs paired currency bowls.
Source supplies count, relative placement and intentional asymmetry. Decorative thickness and redundant warning-triangle outline omitted; the exclamation retains the file-alert identity.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'db6083e7-dc1f-4ace-a693-10530b732733'
SOURCE_PATH = 'pictographic-primitives/files/virus files alert_db6083e7-dc1f-4ace-a693-10530b732733.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'file-warning-alert-symbol'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'files'
    categories = ('files', 'primitives')
    aliases = ()
    keywords = ('file', 'warning', 'alert', 'symbol')

    def build(self):

        def rect(name,l,t,r,b):
            self.add_polyline(name,(l,t),(r,t),(r,b),(l,b),closed=True)

        rect('front-file',8,12,32,44)
        self.add_polyline('rear-file',(16,4),(40,4),(40,36))
        self.add_line('warning-stem',(20,20),(20,28))
        self.add_dot('warning-dot',(20,36))
