"""Two centered nested upward Wi-Fi arcs, without a dot beneath. Exclude the smartphone frame.

Plan: Two nested shallow half-ellipses sharing the center axis; no dot. Bounds (2,10)-(30,22).
Construction reference: Lucide wifi: concentric separated arcs; source has exactly two arcs and no dot."""
from ...keyshapes import Keyshape
from ._base import Symbol32

SOURCE_ICON_ID = 'a2e42ae3-1e50-4ab6-8845-45739f1e04ef'
SOURCE_PATH = 'pictographic-primitives/other/mobile phone wifi_a2e42ae3-1e50-4ab6-8845-45739f1e04ef.svg'
SOURCE_ICON_IDS = ('a2e42ae3-1e50-4ab6-8845-45739f1e04ef',)
AUTHOR = 'gpt-6'

class TwoWifiArcsSymbol(Symbol32):
    icon_id = 'two-wifi-arcs-symbol'
    keyshape = Keyshape.HRECT_S
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('two', 'wifi', 'arcs', 'symbol')

    def build(self) -> None:
        self.add_arc('outer',(2,15),(30,15),radius_x=14,radius_y=5)
        self.add_arc('inner',(8,22),(24,22),radius_x=8,radius_y=4)
