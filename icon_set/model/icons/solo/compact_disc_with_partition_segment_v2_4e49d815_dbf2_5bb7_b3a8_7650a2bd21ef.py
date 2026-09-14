"""A compact disc with a solid hub dot and lower-right sector boundary. CIRCLE preserves the radial envelope. Lucide disc-3 informs concentric construction; the sector is deliberately asymmetric."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '4e49d815-dbf2-5bb7-b3a8-7650a2bd21ef'
SOURCE_PATH = 'pictographic-primitives/computers/batch-04/cd partition_4e49d815-dbf2-5bb7-b3a8-7650a2bd21ef.svg'
AUTHOR = 'gpt-6'

class CompactDiscWithPartitionSegmentVariant2(Solo48):
    icon_id = 'compact-disc-with-partition-segment-v2'
    variant_of = 'compact-disc-with-partition-segment'
    variant_label = 'Solid disc hub'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/device'
    aliases = ()
    keywords = ('cd', 'disc', 'partition', 'segment', 'storage', 'disk', 'sector', 'media')

    def build(self) -> None:
        """Opening repair: Restored the circular disc rim and widened the lower-right partition band."""
        self.add_arc('rim-0', (24, 4), (44, 24), sweep=True, large_arc=False, radius_x=20, radius_y=20)
        self.add_arc('rim-1', (44, 24), (24, 44), sweep=True, large_arc=False, radius_x=20, radius_y=20)
        self.add_arc('rim-2', (24, 44), (4, 24), sweep=True, large_arc=False, radius_x=20, radius_y=20)
        self.add_arc('rim-3', (4, 24), (24, 4), sweep=True, large_arc=False, radius_x=20, radius_y=20)
        self.add_contour('rim', 'rim-0', 'rim-1', 'rim-2', 'rim-3', closed=True)
        self.add_line('sector-right', (44, 24), (35, 24))
        self.add_arc('sector-turn', (35, 24), (24, 35), sweep=True, large_arc=False, radius_x=11, radius_y=11)
        self.add_line('sector-bottom', (24, 35), (24, 44))
        self.add_contour('sector', 'sector-right', 'sector-turn', 'sector-bottom', closed=False)
        self.relate('connect', 'rim', 'sector')
        self.add_dot('hub', (24, 24))
