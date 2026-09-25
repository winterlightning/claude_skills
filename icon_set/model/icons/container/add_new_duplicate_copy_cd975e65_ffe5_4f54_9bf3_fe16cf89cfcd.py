"""Two overlapping sheets with a centered plus on the front. A single rear open outline sits ten units from the front; plus arms share one center. Lucide copy-plus informed interrupted overlap and centered mark.
Hosting probes using plus-sign-state-131, heart-state-63, check-mark: invalid, invalid, invalid. Full content occupies the slot; see batch hosting report.
Whole subject explicitly authorized by user; preserve saved family.
Keyshape: SQUARE; fine source details simplified only for native readability.
"""
from ._base import Container64
from ...keyshapes import Keyshape
SOURCE_ICON_ID = 'cd975e65-ffe5-4f54-9bf3-fe16cf89cfcd'
SOURCE_PATH = 'pictographic-primitives/files/copy_cd975e65-ffe5-4f54-9bf3-fe16cf89cfcd.svg'
AUTHOR = "gpt-6"

class Icon(Container64):
    icon_id = 'add-new-duplicate-copy'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'files'
    categories = ('files', 'primitives')
    aliases = ('Add New Duplicate Copy',)
    keywords = ('add', 'new', 'duplicate', 'copy')
    def build(self):
        self.add_polyline("rear",(2,46),(2,2),(46,2))
        self.add_polyline("front",(14,14),(62,14),(62,62),(14,62),closed=True)
        center=(38,38)
        for name,p in (("left",(26,38)),("right",(50,38)),("top",(38,26)),("bottom",(38,50))):
            self.add_line(name,center,p)
        self.relate("connect","left","right","top","bottom")
