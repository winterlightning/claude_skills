"""Rounded reply bubble with integral leftward return arrow and lower-left tail.
Keyshape ink bounds: (4, 4, 44, 44).
Construction reference: Lucide message-circle-reply; source render establishes subject.
Reduction: No extra internal reply glyph; arrow is integral to border.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '61b0437a-7061-4185-ae9a-ef12d4e4d434'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/message bubble arrow 1_61b0437a-7061-4185-ae9a-ef12d4e4d434.svg'
EXPORTED_REFERENCE = 'work/brief-exports/20260918-all-todo-batches-15/batches/batch-025/references/message bubble arrow 1_61b0437a-7061-4185-ae9a-ef12d4e4d434.svg'
AUTHOR = 'gpt-6'

class Batch025Icon(Solo48):
    icon_id = 'reply-speech-bubble-batch-025-02'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/other"
    aliases = ()
    keywords = ('reply', 'speech', 'bubble')

    def build(self):
        self.add_line('upper',(24,14),(36,14))
        self.add_arc('tr',(36,14),(42,20),radius_x=6)
        self.add_line('right',(42,20),(42,30))
        self.add_arc('br',(42,30),(36,36),radius_x=6)
        self.add_line('bottom-1', (36, 36), (20, 36))
        self.add_line('bottom-2', (20, 36), (12, 42))
        self.add_line('bottom-3', (12, 42), (12, 36))
        self.add_arc('bl',(12,36),(6,30),radius_x=6)
        self.add_line('left',(6,30),(6,18))
        self.add_contour('bubble','upper','tr','right','br','bottom-1','bottom-2','bottom-3','bl','left')
        self.add_polyline('arrow',(32,22),(24,14),(32,6))
        self.relate('connect','arrow','bubble')
