'Gamepad: smooth equal grips, clear directional pad and action button; preserve the low central grip notch.'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '0b5d6bf8-c665-542e-a1da-44b8d6221698'
SOURCE_PATH = 'pictographic-primitives/technology/controller_0b5d6bf8-c665-542e-a1da-44b8d6221698.svg'
AUTHOR = 'gpt-6'

class GamepadWithDpad(Solo48):
    icon_id = 'gamepad-with-dpad'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'technology'
    aliases = ()
    keywords = ('controller', 'gamepad', 'game', 'gaming', 'joypad', 'console', 'play')

    def build(self) -> None:
        self.add_line('top',(14,8),(34,8))
        self.add_bezier('right',(34,8),((41,8),(44,16),(44,26)),((44,35),(42,40),(37,40)),((32,40),(30,32),(24,32)))
        self.add_bezier('left',(24,32),((18,32),(16,40),(11,40)),((6,40),(4,35),(4,26)),((4,16),(7,8),(14,8)))
        self.add_contour('shell','top','right','left',closed=True)
        self.add_polyline('dpad-h',(13,20),(16,20),(19,20))
        self.add_polyline('dpad-v',(16,17),(16,20),(16,24))
        self.relate('connect','dpad-h','dpad-v')
        self.add_dot('button',(33,20))
