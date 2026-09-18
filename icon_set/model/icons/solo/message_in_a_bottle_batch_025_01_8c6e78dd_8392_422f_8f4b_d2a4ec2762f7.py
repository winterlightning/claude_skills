"""Diagonal bottle outline and a single rolled-message stroke above a detached wave.
Keyshape ink bounds: (4, 4, 44, 44).
Construction reference: Lucide milk; source render establishes subject.
Reduction: Cork seam and tight scroll curl reduced to an oblique paper mark.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8c6e78dd-8392-422f-8f4b-d2a4ec2762f7'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/message bottle_8c6e78dd-8392-422f-8f4b-d2a4ec2762f7.svg'
EXPORTED_REFERENCE = 'work/brief-exports/20260918-all-todo-batches-15/batches/batch-025/references/message bottle_8c6e78dd-8392-422f-8f4b-d2a4ec2762f7.svg'
AUTHOR = 'gpt-6'

class Batch025Icon(Solo48):
    icon_id = 'message-in-a-bottle-batch-025-01'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/other"
    aliases = ()
    keywords = ('message', 'in', 'a', 'bottle')

    def build(self):
        self.add_polyline('bottle', (10,30),(16,18),(24,14),(30,6),(40,12),(34,22),(34,30))
        self.add_bezier('message',(20,31),((21,29),(22,26),(23,25)),((23,24),(24,24),(25,25)))
        self.add_bezier('water',(6,42),((10,42),(12,38),(14,38)),((18,42),(20,42),(24,38)),((28,42),(30,42),(34,38)),((38,42),(40,42),(42,42)))
