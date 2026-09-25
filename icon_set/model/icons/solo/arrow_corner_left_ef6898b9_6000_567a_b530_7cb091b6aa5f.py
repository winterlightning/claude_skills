"""Square arrow corner with two equal straight arms. Preserves the original direction; visible ink (4,4)-(44,44)."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'ef6898b9-6000-567a-b530-7cb091b6aa5f'
SOURCE_PATH = 'pictographic-primitives/arrows/arrow corner left_ef6898b9-6000-567a-b530-7cb091b6aa5f.svg'
AUTHOR = 'gpt-6'

class ArrowCornerLeftArrows(Solo48):
    icon_id = 'arrow-corner-left-arrows'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    categories = ('arrows', 'primitives')
    aliases = ()
    keywords = ('arrow', 'corner', 'left', 'arrows')

    def build(self):
        low, center, high = (6, 24, 42)
        a, joint, b = [(high, low), (low, center), (high, high)]
        self.add_line('arm-a', a, joint)
        self.add_line('arm-b', joint, b)
        self.add_contour('corner', 'arm-a', 'arm-b')
