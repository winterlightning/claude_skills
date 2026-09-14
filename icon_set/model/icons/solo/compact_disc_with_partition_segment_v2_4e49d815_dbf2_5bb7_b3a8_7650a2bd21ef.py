# Variant of compact-disc-with-partition-segment; parent file remains unchanged.
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
        self.add_arc('rim-0', (24, 6), (42, 24), radius_x=22, radius_y=22, sweep=True, large_arc=False)
        self.add_arc('rim-1', (42, 24), (24, 42), radius_x=22, radius_y=22, sweep=True, large_arc=False)
        self.add_arc('rim-2', (24, 42), (6, 24), radius_x=22, radius_y=22, sweep=True, large_arc=False)
        self.add_arc('rim-3', (6, 24), (24, 6), radius_x=22, radius_y=22, sweep=True, large_arc=False)
        self.add_contour('rim', 'rim-0', 'rim-1', 'rim-2', 'rim-3', closed=True)
        self.add_line('sector-right', (42, 24), (36, 24))
        self.add_arc('sector-turn', (36, 24), (24, 36), radius_x=12, radius_y=12, sweep=True, large_arc=False)
        self.add_line('sector-bottom', (24, 36), (24, 42))
        self.add_contour('sector', 'sector-right', 'sector-turn', 'sector-bottom', closed=False)
        self.relate('connect', 'rim', 'sector')
        self.add_dot('hub', (24, 24))
