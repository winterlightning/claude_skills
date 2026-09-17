"""Savings Piggy Bank.
Plan: Left-facing rounded pig with pointed ear, short snout and broad feet. Extrema (4,8)-(44,40).
Reference: Lucide piggy-bank: coherent animal outline and integral feet; supplied source sets leftward direction.
Reduction: Eye and coin slot omitted; feet and tail retain source variation.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8d426d16-eb32-5158-8c26-bbb0bf45f47a'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/finance/saving bank_8d426d16-eb32-5158-8c26-bbb0bf45f47a.svg'
AUTHOR = 'gpt-6'

class Batch30Icon(Solo48):
    icon_id = 'piggy-bank-broad-feet'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/finance"
    aliases = ()
    keywords = ('savings', 'piggy', 'bank')

    def build(self):

        self.add_line('snout-1',(10, 28),(4, 28))
        self.add_line('snout-2',(4, 28),(4, 20))
        self.add_line('snout-3',(4, 20),(12, 16))
        self.add_line('ear-1',(12, 16),(12, 8))
        self.add_line('ear-2',(12, 8),(20, 12))
        self.add_bezier('back',(20,12),((30,10),(40,14),(40,24)))

        self.add_bezier('rump',(40,24),((40,30),(38,32),(36,32)))
        self.add_line('feet-1',(36, 32),(36, 40))
        self.add_line('feet-2',(36, 40),(28, 40))
        self.add_line('feet-3',(28, 40),(28, 34))
        self.add_line('feet-4',(28, 34),(20, 34))
        self.add_line('feet-5',(20, 34),(20, 40))
        self.add_line('feet-6',(20, 40),(12, 40))
        self.add_line('feet-7',(12, 40),(12, 32))
        self.add_line('cheek',(12,32),(10,28))
        self.add_contour('pig',*[f'snout-{i}' for i in range(1,4)],*[f'ear-{i}' for i in range(1,3)],'back','rump',*[f'feet-{i}' for i in range(1,8)],'cheek',closed=True)
        self.add_line('tail',(40,24),(44,24));self.relate('connect','pig','tail')
