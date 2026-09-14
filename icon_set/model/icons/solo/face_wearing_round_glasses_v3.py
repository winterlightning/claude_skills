"""CIRCLE: center (24,24), centerline radius 20, visible ink radius 22. Lucide disc, disc-3 and glasses inform shared-center and paired construction."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '44a429e7-b8bc-58df-94d2-a0236dce12a0'
SOURCE_PATH = 'pictographic-primitives/accessories/batch-05/glasses_44a429e7-b8bc-58df-94d2-a0236dce12a0.svg'
AUTHOR = 'gpt-6'

class FaceWearingRoundGlassesVariant3(Solo48):
    icon_id = 'face-wearing-round-glasses-v3'
    variant_of = 'face-wearing-round-glasses'
    variant_label = 'Exact circle envelope and clear internal spacing'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/accessories'
    aliases = ()
    keywords = ('face', 'glasses', 'spectacles', 'smile', 'avatar', 'person', 'eyewear', 'portrait')

    def _circle(self, name, x, y, r):
        pts = [(x, y - r), (x + r, y), (x, y + r), (x - r, y), (x, y - r)]
        for i in range(4):
            self.add_arc(f'{name}-{i}', pts[i], pts[i + 1], radius_x=r, radius_y=r)
        self.add_contour(name, *[f'{name}-{i}' for i in range(4)], closed=True)

    def build(self):
        self._circle('face', 24, 24, 20)
        for name, x in [('lens-left', 17), ('lens-right', 31)]:
            self._circle(name, x, 21, 4)
        self.add_line('bridge', (21, 21), (27, 21))
        for n in ['lens-left', 'lens-right']:
            self.relate('connect', 'bridge', n)
        self.add_arc('smile', (18, 33), (30, 33), radius_x=8, radius_y=4, sweep=False)
