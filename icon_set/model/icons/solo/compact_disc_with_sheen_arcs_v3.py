"""CIRCLE: center (24,24), centerline radius 20, visible ink radius 22. Lucide disc, disc-3 and glasses inform shared-center and paired construction."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'ff3648e6-111a-5162-b458-16f454b6ef2e'
SOURCE_PATH = 'pictographic-primitives/computers/batch-04/cd_ff3648e6-111a-5162-b458-16f454b6ef2e.svg'
AUTHOR = 'gpt-6'

class CompactDiscWithSheenArcsVariant3(Solo48):
    icon_id = 'compact-disc-with-sheen-arcs-v3'
    variant_of = 'compact-disc-with-sheen-arcs'
    variant_label = 'Exact circle envelope and clear internal spacing'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/device'
    aliases = ()
    keywords = ('cd', 'disc', 'dvd', 'media', 'storage', 'music', 'shine', 'disk')

    def _circle(self, name, x, y, r):
        pts = [(x, y - r), (x + r, y), (x, y + r), (x - r, y), (x, y - r)]
        for i in range(4):
            self.add_arc(f'{name}-{i}', pts[i], pts[i + 1], radius_x=r, radius_y=r)
        self.add_contour(name, *[f'{name}-{i}' for i in range(4)], closed=True)

    def build(self):
        self._circle('rim', 24, 24, 20)
        self._circle('hub', 24, 24, 3)
        self.add_arc('sheen-upper', (25, 13), (35, 23), radius_x=10)
        self.add_arc('sheen-lower', (23, 35), (13, 25), radius_x=10)
