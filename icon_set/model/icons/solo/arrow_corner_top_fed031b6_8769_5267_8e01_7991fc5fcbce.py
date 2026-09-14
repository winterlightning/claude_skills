"""Square arrow corner with two equal straight arms. Preserves the original direction; visible ink (4,4)-(44,44)."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'fed031b6-8769-5267-8e01-7991fc5fcbce'
SOURCE_PATH = 'icons-json/arrows/arrow corner top_fed031b6-8769-5267-8e01-7991fc5fcbce.json'
AUTHOR = 'gpt-6'

class ArrowCornerTop(Solo48):
    icon_id = 'arrow-corner-top'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('arrow', 'corner', 'top', 'arrows')

    def build(self):
        low, center, high = (6, 24, 42)
        a, joint, b = [(high, low), (low, low), (low, high)]
        self.add_line('arm-a', a, joint)
        self.add_line('arm-b', joint, b)
        self.add_contour('corner', 'arm-a', 'arm-b')
