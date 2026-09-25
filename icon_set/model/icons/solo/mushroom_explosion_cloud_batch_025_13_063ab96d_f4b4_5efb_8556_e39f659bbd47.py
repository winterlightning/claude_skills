"""Three-lobed mushroom canopy over a narrow flaring smoke column.
Keyshape ink bounds: (4, 4, 44, 44).
Construction reference: Lucide cloud; source render establishes subject.
Reduction: Cross-band dropped to leave the rising column open at 48px.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '063ab96d-f4b4-5efb-8556-e39f659bbd47'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/atomic bomb_063ab96d-f4b4-5efb-8556-e39f659bbd47.svg'
EXPORTED_REFERENCE = 'work/brief-exports/20260918-all-todo-batches-15/batches/batch-025/references/atomic bomb_063ab96d-f4b4-5efb-8556-e39f659bbd47.svg'
AUTHOR = 'gpt-6'

class Batch025Icon(Solo48):
    icon_id = 'mushroom-explosion-cloud-batch-025-13'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ()
    keywords = ('mushroom', 'explosion', 'cloud')

    def build(self):
        self.add_arc('crown',(16,14),(32,14),radius_x=8)
        self.add_arc('right-lobe',(32,14),(42,24),radius_x=10)
        self.add_arc('right-bottom',(42,24),(34,32),radius_x=8)
        self.add_line('under-right-1', (34, 32), (29, 32))
        self.add_bezier('stem-right',(29,32),((29,36),(31,40),(34,42)))
        self.add_line('ground',(34,42),(14,42))
        self.add_bezier('stem-left',(14,42),((17,40),(19,36),(19,32)))
        self.add_line('under-left',(19,32),(14,32))
        self.add_arc('left-bottom',(14,32),(6,24),radius_x=8)
        self.add_arc('left-lobe',(6,24),(16,14),radius_x=10)
        self.add_contour('cloud','crown','right-lobe','right-bottom','under-right-1','stem-right','ground','stem-left','under-left','left-bottom','left-lobe',closed=True)
