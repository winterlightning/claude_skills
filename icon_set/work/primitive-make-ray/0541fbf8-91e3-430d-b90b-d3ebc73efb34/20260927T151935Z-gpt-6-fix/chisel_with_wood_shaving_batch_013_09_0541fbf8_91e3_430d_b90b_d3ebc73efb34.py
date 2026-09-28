"""Chisel with Wood Shaving.

SOLO48 visible bounds: (4, 4, 44, 44). Centerline extremes: (6, 6, 42, 42).

Symbol plan: Diagonal long chisel beside an open curled shaving.
Reduction: Open the curl to preserve a wide central hole.
Construction reference: No useful local Lucide subject match; supplied reference governs.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '0541fbf8-91e3-430d-b90b-d3ebc73efb34'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__chisel-with-wood-shaving-batch-013-09/20260927T151732Z-thuan-mac-1/reference/crafts carving_0541fbf8-91e3-430d-b90b-d3ebc73efb34.svg'
SAVED_REFERENCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/hobbies/crafts carving_0541fbf8-91e3-430d-b90b-d3ebc73efb34.svg'
EXPORTED_REFERENCE_PATH = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-013/references/crafts carving_0541fbf8-91e3-430d-b90b-d3ebc73efb34.svg'
AUTHOR = 'gpt-6'
BATCH_AUTHORING_RUN = "20260917-011-015"


class GeneratedSolo(Solo48):
    icon_id = 'chisel-with-wood-shaving-batch-013-09'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "hobbies"
    categories = ("primitives", "hobbies")
    aliases = ()
    keywords = ('chisel', 'wood', 'shaving', 'carving', 'craft', 'tool')

    def build(self):
        self.add_polyline('chisel', (34, 6), (42, 12), (29, 31),
                          (23, 42), (15, 37), (22, 24), closed=True)
        # The rejected short hook hid the wood shaving's characteristic curl.
        self.add_bezier('shaving-1', (6, 36), ((6, 31), (6, 24), (6, 19)))
        self.add_bezier('shaving-2', (6, 19), ((7, 13), (12, 13), (14, 16)))
        self.add_contour('shaving', 'shaving-1', 'shaving-2', closed=False)
