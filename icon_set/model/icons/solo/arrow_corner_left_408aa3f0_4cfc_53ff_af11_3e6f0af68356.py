"""Square arrow corner with two equal straight arms. Preserves the original direction; visible ink (4,4)-(44,44)."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '408aa3f0-4cfc-53ff-af11-3e6f0af68356'
SOURCE_PATH = 'icons-json/arrows/arrow corner left_408aa3f0-4cfc-53ff-af11-3e6f0af68356.json'
AUTHOR = 'gpt-6'

class ArrowCornerLeft(Solo48):
    icon_id = 'arrow-corner-left'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('arrow', 'corner', 'left', 'arrows')

    def build(self):
        low, center, high = (6, 24, 42)
        a, joint, b = [(low, low), (low, high), (high, high)]
        self.add_line('arm-a', a, joint)
        self.add_line('arm-b', joint, b)
        self.add_contour('corner', 'arm-a', 'arm-b')
