# Variant of peacock-feather; parent file remains unchanged.
'A peacock feather with a dot eye. VRECT_L extremes (8,2)-(40,46) retain the tall diagonal vane and quill. The circular eye loop is replaced by one dot. Lucide feather informs the sparse vane and diagonal shaft; the diagonal pose is intentional.'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'f40b6248-c81f-53b7-82f1-64f0cd1d0e22'
SOURCE_PATH = 'pictographic-primitives/animals/peacock feather_f40b6248-c81f-53b7-82f1-64f0cd1d0e22.svg'
AUTHOR = 'gpt-6'

class PeacockFeatherVariant2(Solo48):
    icon_id = 'peacock-feather-v2'
    variant_of = 'peacock-feather'
    variant_label = 'Dot feather eye'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'nature/animals'
    aliases = ()
    keywords = ('peacock', 'feather')

    def build(self) -> None:
        self.add_arc('vane-left', (40, 2), (12, 30), radius_x=28, radius_y=28, sweep=False, large_arc=False)
        self.add_line('vane-base', (12, 30), (12, 38))
        self.add_arc('vane-right', (12, 38), (40, 10), radius_x=28, radius_y=28, sweep=False, large_arc=False)
        self.add_line('vane-tip', (40, 10), (40, 2))
        self.add_contour('vane', 'vane-left', 'vane-base', 'vane-right', 'vane-tip', closed=True)
        self.add_line('quill', (12, 38), (8, 46))
        self.relate('connect', 'vane', 'quill')
        self.add_dot('eye', (25, 20))
