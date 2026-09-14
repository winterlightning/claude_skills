"""CIRCLE: center (24,24), centerline radius 20, visible ink radius 22. Lucide disc, disc-3 and glasses inform shared-center and paired construction."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '4e49d815-dbf2-5bb7-b3a8-7650a2bd21ef'
SOURCE_PATH = 'pictographic-primitives/computers/batch-04/cd partition_4e49d815-dbf2-5bb7-b3a8-7650a2bd21ef.svg'
AUTHOR = 'gpt-6'

class CompactDiscWithPartitionSegmentVariant4(Solo48):
    icon_id = 'compact-disc-with-partition-segment-v4'
    variant_of = 'compact-disc-with-partition-segment'
    variant_label = 'Exact circle envelope and clear internal spacing'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/device'
    aliases = ()
    keywords = ('cd', 'disc', 'partition', 'segment', 'storage', 'disk', 'sector', 'media')

    def _circle(self, name, x, y, r):
        pts = [(x, y - r), (x + r, y), (x, y + r), (x - r, y), (x, y - r)]
        for i in range(4):
            self.add_arc(f'{name}-{i}', pts[i], pts[i + 1], radius_x=r, radius_y=r)
        self.add_contour(name, *[f'{name}-{i}' for i in range(4)], closed=True)

    def build(self):
        self._circle('rim', 24, 24, 20)
        self._circle('hub', 24, 24, 4)
        self.add_line('sector-right', (44, 24), (37, 24))
        self.add_arc('sector-turn', (37, 24), (24, 37), radius_x=13)
        self.add_line('sector-bottom', (24, 37), (24, 44))
        self.add_contour('sector', 'sector-right', 'sector-turn', 'sector-bottom')
        self.relate('connect', 'rim', 'sector')
