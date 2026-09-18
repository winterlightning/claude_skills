'Mirrored open jaws share actuator base nodes; capsule cap and long actuator. No useful Lucide claw match; omit extra collar band.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2f1d22c1-6735-46a3-a249-52243f83d20a'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_21/gripper_2f1d22c1-6735-46a3-a249-52243f83d20a.svg'
AUTHOR = 'gpt-6'

class Result(Solo48):
    icon_id = 'mechanical-claw-gripper-batch-057'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects/tools'
    aliases = ()
    keywords = ('robot', 'claw', 'gripper', 'mechanical', 'tool', 'automation')

    def build(self):
        self.add_arc('cap',(16,12),(32,12),radius_x=8)
        self.add_polyline('actuator',(32,12),(32,24),(16,24),(16,12))
        self.relate('connect','cap','actuator')
        for side in (-1,1):
            p=lambda x,y:(24+side*x,y)
            self.add_polyline(f'jaw-{side}',p(8,24),p(16,34),p(12,44),p(8,40))
            self.relate('connect','actuator',f'jaw-{side}')
