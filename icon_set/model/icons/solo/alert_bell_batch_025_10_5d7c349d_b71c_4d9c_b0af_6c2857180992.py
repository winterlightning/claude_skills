"""Symmetric bell dome and broad rim, integrated crown loop and lower round clapper.
Keyshape ink bounds: (6, 2, 42, 46).
Construction reference: Lucide bell; source render establishes subject.
Reduction: Crown loop enlarged for four-unit internal clearance; round clapper retained below the rim.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5d7c349d-b71c-4d9c-b0af-6c2857180992'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/bell_5d7c349d-b71c-4d9c-b0af-6c2857180992.svg'
EXPORTED_REFERENCE = 'work/brief-exports/20260918-all-todo-batches-15/batches/batch-025/references/bell_5d7c349d-b71c-4d9c-b0af-6c2857180992.svg'
AUTHOR = 'gpt-6'

class Batch025Icon(Solo48):
    icon_id = 'alert-bell-batch-025-10'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ()
    keywords = ('alert', 'bell')

    def build(self):
        self.add_arc('loop',(20,8),(28,8),radius_x=4)
        self.add_line('loop-right',(28,8),(28,16))
        self.add_bezier('right',(28,16),((40,18),(33,28),(40,36)))
        self.add_line('rim-1', (40, 36), (32, 36))
        self.add_line('rim-2', (32, 36), (16, 36))
        self.add_line('rim-3', (16, 36), (8, 36))
        self.add_bezier('left',(8,36),((15,28),(8,18),(20,16)))
        self.add_line('loop-left',(20,16),(20,8))
        self.add_contour('bell','loop','loop-right','right','rim-1','rim-2','rim-3','left','loop-left',closed=True)
        self.add_arc('clapper',(32,36),(16,36),radius_x=8)
        self.relate('connect','clapper','bell')
        self.add_line('loop-base',(20,16),(28,16))
        self.relate('connect','loop-base','bell')
