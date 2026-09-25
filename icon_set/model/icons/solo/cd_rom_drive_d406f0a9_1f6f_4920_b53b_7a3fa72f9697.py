"""Square the drive housing on a shared horizontal baseline and retain one solid dot at the circular disc center. Applied to the original icon identity."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'd406f0a9-1f6f-4920-b53b-7a3fa72f9697'
SOURCE_PATH = 'pictographic-primitives/computers/batch-03/cd rom_d406f0a9-1f6f-4920-b53b-7a3fa72f9697.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('d406f0a9-1f6f-4920-b53b-7a3fa72f9697', 'pictographic-primitives/computers/batch-03/cd rom_d406f0a9-1f6f-4920-b53b-7a3fa72f9697.svg'),)

class CdRomDrive(Solo48):
    icon_id = 'cd-rom-drive'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'computers'
    aliases = ()
    keywords = ('cd', 'rom', 'drive')

    def build(self) -> None:
        """Symbol plan: Square the drive housing on a shared horizontal baseline and retain one solid dot at the circular disc center. Reference: Lucide disc: a circular disc and exactly centered dot hub."""
        self.add_polyline('housing', (12, 18), (6, 18), (6, 6), (42, 6), (42, 18), (36, 18))
        self.add_line('slot', (12, 18), (36, 18))
        self.add_arc('disc', (36, 18), (12, 18), radius_x=15, large_arc=True)
        self.relate('connect', 'housing', 'slot')
        self.relate('connect', 'housing', 'disc')
        self.relate('connect', 'slot', 'disc')
        self.add_dot('hub', (24, 27))
