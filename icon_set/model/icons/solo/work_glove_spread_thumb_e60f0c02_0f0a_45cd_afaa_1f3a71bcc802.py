"""Protective Safety Work Glove.
Plan: Four rounded fingertips and a left spread thumb above a broad cuff. Extrema (4,8)-(44,40).
Reference: Lucide hand: rounded fingers with shared interior separations and broad palm; human reference governs minimal anatomy.
Reduction: Diagonal orientation made upright to keep four rounded fingers readable; cuff edge retained.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e60f0c02-0f0a-45cd-afaa-1f3a71bcc802'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/farming/glove_e60f0c02-0f0a-45cd-afaa-1f3a71bcc802.svg'
AUTHOR = 'gpt-6'

class Batch29Icon(Solo48):
    icon_id = 'work-glove-spread-thumb'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/agriculture"
    aliases = ()
    keywords = ('protective', 'safety', 'work', 'glove')

    def build(self):

        self.add_line('thumb-1',(12,40),(4,32))
        self.add_line('thumb-2',(4,32),(4,28))
        self.add_arc('thumb-3',(4,28),(12,20),radius_x=8)
        self.add_line('thumb-4',(12,20),(12,16))
        self.add_arc('finger-0',(12,16),(20,16),radius_x=4)
        self.add_line('step-0',(20,16),(20,12))
        self.add_arc('finger-1',(20,12),(28,12),radius_x=4)
        self.add_line('step-1',(28,12),(28,16))
        self.add_arc('finger-2',(28,16),(36,16),radius_x=4)
        self.add_line('step-2',(36,16),(36,20))
        self.add_arc('finger-3',(36,20),(44,20),radius_x=4)
        self.add_line('palm-1',(44, 20),(44, 32))
        self.add_line('palm-2',(44, 32),(36, 40))
        self.add_line('palm-3',(36, 40),(12, 40))
        self.add_contour('glove',*[f'thumb-{i}' for i in range(1,5)],'finger-0','step-0','finger-1','step-1','finger-2','step-2','finger-3',*[f'palm-{i}' for i in range(1,4)],closed=True)
        for i,(x,y) in enumerate(((20,16),(28,16),(36,20))):
            self.add_line(f'divider-{i}',(x,y),(x,28));self.relate('connect','glove',f'divider-{i}')
