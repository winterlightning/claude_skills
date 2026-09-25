"""An overhead rail suspends an open claw over a workpiece; solid rails reduced to strokes."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '533b3311-8592-5951-93a2-3472f4aa5de1'
SOURCE_PATH = 'pictographic-primitives/tools/clamp machine_533b3311-8592-5951-93a2-3472f4aa5de1.svg'
AUTHOR = 'gpt-6'

class ClawGripperMachine(Solo48):
    icon_id = 'claw-gripper-machine'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "tools"
    aliases = ()
    keywords = ('claw', 'gripper', 'crane', 'machine', 'grab', 'robotic', 'clamp', 'industrial')

    def build(self) -> None:
        self.add_line('rail',(4,8),(44,8))
        self.add_line('stem',(24,8),(24,18))
        self.relate('connect','stem','rail')
        self.add_arc('left',(24,18),(12,30),radius_x=12,sweep=False)
        self.add_arc('right',(24,18),(36,30),radius_x=12)
        self.relate('connect','left','right','stem')
        self.add_line('block',(8,40),(40,40))
