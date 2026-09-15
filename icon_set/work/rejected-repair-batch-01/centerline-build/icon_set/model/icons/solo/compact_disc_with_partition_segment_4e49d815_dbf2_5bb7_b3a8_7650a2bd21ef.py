"""Replace the circular hub with one centered dot. Independent feedback revision; parent preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '4e49d815-dbf2-5bb7-b3a8-7650a2bd21ef'
SOURCE_PATH = 'pictographic-primitives/computers/batch-04/cd partition_4e49d815-dbf2-5bb7-b3a8-7650a2bd21ef.svg'
AUTHOR = 'gpt-6'

class CompactDiscWithPartitionSegment(Solo48):
    icon_id = 'compact-disc-with-partition-segment'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/device'
    aliases = ()
    keywords = ('cd', 'disc', 'partition', 'segment', 'storage', 'disk', 'sector', 'media')

    def build(self) -> None:
        """Symbol plan: Replace the circular hub with one centered dot. Reference: Lucide disc: concentric rim and hub."""

        def circle(name, cx, cy, radius):
            points = [(cx + radius, cy), (cx, cy + radius), (cx - radius, cy), (cx, cy - radius)]
            for i in range(4):
                self.add_arc(f'{name}-{i}', points[i], points[(i + 1) % 4], radius_x=radius)
            self.add_contour(name, *[f'{name}-{i}' for i in range(4)], closed=True)
        circle('rim', 24, 24, 20)
        self.add_dot('hub', (24, 24))
        self.add_line('sector-right', (44, 24), (36, 24))
        self.add_arc('sector-turn', (36, 24), (24, 36), radius_x=12)
        self.add_line('sector-bottom', (24, 36), (24, 44))
        self.add_contour('sector', 'sector-right', 'sector-turn', 'sector-bottom')
        self.relate('connect', 'rim', 'sector')
