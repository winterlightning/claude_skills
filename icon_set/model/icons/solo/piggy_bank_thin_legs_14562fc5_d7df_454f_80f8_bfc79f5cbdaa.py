"""Money Saving Piggy Bank.
Plan: Left-facing rounded pig with pointed ear, short snout and thin legs. Extrema (4,8)-(44,40).
Reference: Lucide piggy-bank: coherent animal outline and integral feet; supplied source sets leftward direction.
Reduction: Eye and coin slot omitted; feet and tail retain source variation.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '14562fc5-d7df-454f-80f8-bfc79f5cbdaa'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/finance/saving piggy bank_14562fc5-d7df-454f-80f8-bfc79f5cbdaa.svg'
AUTHOR = 'gpt-6'

class Batch30Icon(Solo48):
    icon_id = 'piggy-bank-thin-legs'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "finance"
    aliases = ()
    keywords = ('money', 'saving', 'piggy', 'bank')

    def build(self):

        self.add_line('snout-1',(10, 28),(4, 28))
        self.add_line('snout-2',(4, 28),(4, 20))
        self.add_line('snout-3',(4, 20),(12, 16))
        self.add_line('ear-1',(12, 16),(12, 8))
        self.add_line('ear-2',(12, 8),(20, 12))
        self.add_bezier('back',(20,12),((30,10),(40,14),(40,24)))

        self.add_bezier('belly',(40,24),((40,32),(36,34),(32,34)),((27,34),(22,34),(18,34)),((14,34),(10,32),(10,28)))
        self.add_contour('pig',*[f'snout-{i}' for i in range(1,4)],*[f'ear-{i}' for i in range(1,3)],'back','belly',closed=True)
        for i,x in enumerate((18,32)):
            self.add_line(f'leg-{i}',(x,34),(x-2 if i==0 else x+2,40));self.relate('connect','pig',f'leg-{i}')
        self.add_arc('tail',(40,24),(44,20),radius_x=4,sweep=False);self.relate('connect','pig','tail')
