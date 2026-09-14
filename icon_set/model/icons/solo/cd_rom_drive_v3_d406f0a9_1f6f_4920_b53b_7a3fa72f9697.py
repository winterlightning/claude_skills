"""Moved the emerging circular disc upward; joined the shallow housing at the slot corners. Solid concentric hub retained.

Keyshape SQUARE: visible bounds (4, 4, 44, 44).
Reference: disc-3: concentric circular construction.
"""
# Independent repair of cd-rom-drive-v2; parent preserved.
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'd406f0a9-1f6f-4920-b53b-7a3fa72f9697'
SOURCE_PATH = 'pictographic-primitives/computers/batch-03/cd rom_d406f0a9-1f6f-4920-b53b-7a3fa72f9697.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('d406f0a9-1f6f-4920-b53b-7a3fa72f9697', 'pictographic-primitives/computers/batch-03/cd rom_d406f0a9-1f6f-4920-b53b-7a3fa72f9697.svg'),)

class CdRomDriveVariant3(Solo48):
    icon_id = 'cd-rom-drive-v3'
    variant_of = 'cd-rom-drive-v2'
    variant_label = 'Fit current SOLO48 bounds and spacing'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/device'
    aliases = ()
    keywords = ('cd', 'rom', 'drive')

    def build(self) -> None:
        # SQUARE (6,6)-(42,42). A shallow perspective housing shares
        # slot corners with the emerging circular disc (center 24,27; r15).
        self.add_polyline('housing',(12,18),(6,18),(8,6),(40,6),(42,18),(36,18))
        self.add_line('slot',(12,18),(36,18))
        self.add_arc('disc',(36,18),(12,18),radius_x=15,large_arc=True)
        self.relate('connect','housing','slot')
        self.relate('connect','housing','disc')
        self.relate('connect','slot','disc')
        self.add_dot('hub',(24,27))
