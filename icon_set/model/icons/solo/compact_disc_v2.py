"""CIRCLE: center (24,24), centerline radius 20, visible ink radius 22. Lucide disc, disc-3 and glasses inform shared-center and paired construction."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'c291f8c9-ddd6-4932-81de-5eec49892319'
SOURCE_PATH = 'pictographic-primitives/computers/batch-03/cd_c291f8c9-ddd6-4932-81de-5eec49892319.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('c291f8c9-ddd6-4932-81de-5eec49892319', 'pictographic-primitives/computers/batch-03/cd_c291f8c9-ddd6-4932-81de-5eec49892319.svg'),)

class CompactDiscVariant2(Solo48):
    icon_id = 'compact-disc-v2'
    variant_of = 'compact-disc'
    variant_label = 'Exact circle envelope and clear internal spacing'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/device'
    aliases = ()
    keywords = ('compact', 'disc')

    def _circle(self, name, x, y, r):
        pts = [(x, y - r), (x + r, y), (x, y + r), (x - r, y), (x, y - r)]
        for i in range(4):
            self.add_arc(f'{name}-{i}', pts[i], pts[i + 1], radius_x=r, radius_y=r)
        self.add_contour(name, *[f'{name}-{i}' for i in range(4)], closed=True)

    def build(self):
        self._circle('rim', 24, 24, 20)
        self._circle('hub', 24, 24, 6)
