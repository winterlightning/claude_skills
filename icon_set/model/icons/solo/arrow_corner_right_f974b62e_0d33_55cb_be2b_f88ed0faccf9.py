"""Square arrow corner with two equal straight arms. Preserves the original direction; visible ink (4,4)-(44,44)."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'f974b62e-0d33-55cb-be2b-f88ed0faccf9'
SOURCE_PATH = 'icons-json/arrows/arrow corner right_f974b62e-0d33-55cb-be2b-f88ed0faccf9.json'
AUTHOR = 'gpt-6'

class ArrowCornerRight(Solo48):
    icon_id = 'arrow-corner-right'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('arrow', 'corner', 'right', 'arrows')

    def build(self):
        low, center, high = (6, 24, 42)
        a, joint, b = [(high, high), (high, low), (low, low)]
        self.add_line('arm-a', a, joint)
        self.add_line('arm-b', joint, b)
        self.add_contour('corner', 'arm-a', 'arm-b')
