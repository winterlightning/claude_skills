# Variant of cd-rom-drive; parent file remains unchanged.
"""An optical drive with an emerging disc and solid hub dot. SQUARE preserves the housing proportions. Lucide disc-3 informs concentric construction."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'd406f0a9-1f6f-4920-b53b-7a3fa72f9697'
SOURCE_PATH = 'pictographic-primitives/computers/batch-03/cd rom_d406f0a9-1f6f-4920-b53b-7a3fa72f9697.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('d406f0a9-1f6f-4920-b53b-7a3fa72f9697', 'pictographic-primitives/computers/batch-03/cd rom_d406f0a9-1f6f-4920-b53b-7a3fa72f9697.svg'),)

class CdRomDriveVariant2(Solo48):
    icon_id = 'cd-rom-drive-v2'
    variant_of = 'cd-rom-drive'
    variant_label = 'Solid disc hub'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/device'
    aliases = ()
    keywords = ('cd', 'rom', 'drive')

    def build(self) -> None:
        self.add_line('housing-0', (2, 30), (2, 22))
        self.add_line('housing-1', (2, 22), (8, 2))
        self.add_line('housing-2', (8, 2), (40, 2))
        self.add_line('housing-3', (40, 2), (46, 22))
        self.add_line('housing-4', (46, 22), (46, 30))
        self.add_contour('housing', 'housing-0', 'housing-1', 'housing-2', 'housing-3', 'housing-4', closed=False)
        self.add_line('slot', (12, 22), (36, 22))
        self.add_arc('disc-bottom', (36, 22), (12, 22), radius_x=15, large_arc=True, sweep=True)
        self.add_contour('ejecting-disc', 'slot', 'disc-bottom', closed=True)
        self.add_dot('hole', (24, 32))
