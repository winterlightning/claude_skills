# Independent container symbol; edit separately from linked side sub-icon.
"""Cross Mark: Two diagonal strokes cross at their centres, forming an evenly balanced X. Generate this component alone; exclude Rounded Rectangle Frame.

Construction: A centred diagonal X is isolated from its enclosing rectangular frame.
Keyshape: SQUARE; the four extrema follow the SUB32 contract.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '5c4ca37f-144e-4809-8a31-ca31fdd14824'
SOURCE_PATH = 'pictographic-primitives/state/rectangle remove_5c4ca37f-144e-4809-8a31-ca31fdd14824.svg'
AUTHOR = 'gpt-6'

class CrossMarkState231ContainerSymbol(Sub32):
    icon_id = 'cross-mark-state-231-symbol'
    variant_of = 'cross-mark-state-231'
    variant_label = 'Independent container symbol'
    usage_category = 'symbol'
    related_group = 'sub-origin/cross-mark-state-231'
    counterpart_icon_id = 'cross-mark-state-231'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    aliases = ()
    keywords = ('cross', 'mark', 'diagonal', 'strokes', 'centres', 'forming', 'evenly', 'balanced')

    def build(self):
        self.add_line('down', (2, 2), (30, 30))
        self.add_line('up', (2, 30), (30, 2))
        self.relate('connect', 'down', 'up')
