"""Diagonal Hyperlink Chain Link.

SOLO48 visible bounds: (4, 4, 44, 44). Centerline extremes: (6, 6, 42, 42).

Symbol plan: Two diagonal open links joined by one central connector.
Reduction: Open crossing contours avoid a tiny lens-shaped hole.
Construction reference: link: open rings interlock through a clear diagonal connector
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f3554d59-4ee9-5ba8-bc14-5b1324691503'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/interface-essential/attachment_f3554d59-4ee9-5ba8-bc14-5b1324691503.svg'
SAVED_REFERENCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/attachment_f3554d59-4ee9-5ba8-bc14-5b1324691503.svg'
EXPORTED_REFERENCE_PATH = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-015/references/attachment_f3554d59-4ee9-5ba8-bc14-5b1324691503.svg'
AUTHOR = "gpt-6"
BATCH_AUTHORING_RUN = "20260917-011-015"


class GeneratedSolo(Solo48):
    icon_id = 'overlapping-chain-rings-batch-015-01'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "interface-essential"
    categories = ("interface-essential", "state")
    aliases = ()
    keywords = ('chain', 'rings', 'link', 'attachment', 'connection', 'diagonal')

    def build(self):
        self.add_line('lower-link-1', (14, 22), (10, 26))
        self.add_bezier('lower-link-2', (10, 26), ((6, 30), (6, 32), (6, 34)))
        self.add_bezier('lower-link-3', (6, 34), ((6, 39), (9, 42), (14, 42)))
        self.add_bezier('lower-link-4', (14, 42), ((18, 42), (20, 40), (23, 37)))
        self.add_line('lower-link-5', (23, 37), (26, 34))
        self.add_contour('lower-link', 'lower-link-1', 'lower-link-2', 'lower-link-3', 'lower-link-4', 'lower-link-5', closed=False)
        self.add_line('upper-link-1', (34, 26), (38, 22))
        self.add_bezier('upper-link-2', (38, 22), ((42, 18), (42, 16), (42, 14)))
        self.add_bezier('upper-link-3', (42, 14), ((42, 9), (39, 6), (34, 6)))
        self.add_bezier('upper-link-4', (34, 6), ((30, 6), (28, 8), (25, 11)))
        self.add_line('upper-link-5', (25, 11), (22, 14))
        self.add_contour('upper-link', 'upper-link-1', 'upper-link-2', 'upper-link-3', 'upper-link-4', 'upper-link-5', closed=False)
        self.add_line('connector', (17, 31), (31, 17))
