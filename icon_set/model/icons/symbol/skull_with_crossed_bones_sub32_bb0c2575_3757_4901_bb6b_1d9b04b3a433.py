"""Independent 32px profile of skull-with-crossed-bones.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = 'bb0c2575-3757-4901-bb6b-1d9b04b3a433'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/skull_bb0c2575-3757-4901-bb6b-1d9b04b3a433.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('bb0c2575-3757-4901-bb6b-1d9b04b3a433', '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/skull_bb0c2575-3757-4901-bb6b-1d9b04b3a433.svg'),)
PROFILE_SOURCE_KEYS = ('solo/skull-with-crossed-bones',)
SOLO_SOURCE_ICON_IDS = ('skull-with-crossed-bones',)
REFERENCE_EXPORT_SHA256 = '331dbcf163d11adc08d6e034c1269b8832cdd30964e245bf432d937a1340d2ab'

class Drawing(Sub32):
    icon_id = 'skull-with-crossed-bones-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'interface-essential'
    categories = ('interface-essential', 'primitives')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        # Skull: rounded cranium narrowing to the jaw, two eye dots, a tooth line.
        self.add_bezier('s-1', (8, 30), ((8, 28), (8, 26), (7, 24)))
        self.add_bezier('s-2', (7, 24), ((5, 21), (4, 20), (4, 15)))
        self.add_bezier('s-3', (4, 15), ((4, 8), (9, 2), (16, 2)))
        self.add_bezier('s-4', (16, 2), ((23, 2), (28, 8), (28, 15)))
        self.add_bezier('s-5', (28, 15), ((28, 20), (27, 21), (25, 24)))
        self.add_bezier('s-6', (25, 24), ((24, 26), (24, 28), (24, 30)))
        self.add_contour('skull', 's-1', 's-2', 's-3', 's-4', 's-5', 's-6')
        self.add_dot('eye-l', (12, 15))
        self.add_dot('eye-r', (20, 15))
        self.add_line('tooth', (16, 26), (16, 30))
        # Crossed bones behind the skull, one from each corner to the skull's edge.
        self.add_line('bone-tl', (2, 2), (6, 7))
        self.add_line('bone-tr', (30, 2), (26, 7))
        self.add_line('bone-bl', (2, 30), (7, 24))
        self.add_line('bone-br', (30, 30), (25, 24))
        self.relate('connect', 'skull', 'bone-tl')
        self.relate('connect', 'skull', 'bone-tr')
        self.relate('connect', 'skull', 'bone-bl')
        self.relate('connect', 'skull', 'bone-br')
