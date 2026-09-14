"""CIRCLE: center (24,24), centerline radius 20, visible ink radius 22. Lucide disc, disc-3 and glasses inform shared-center and paired construction."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '35902389-7674-5992-88ac-62b704c11f7f'
SOURCE_PATH = 'pictographic-primitives/computers/batch-04/cd broken_35902389-7674-5992-88ac-62b704c11f7f.svg'
AUTHOR = 'gpt-6'

class CrackedCompactDiscVariant3(Solo48):
    icon_id = 'cracked-compact-disc-v3'
    variant_of = 'cracked-compact-disc'
    variant_label = 'Exact circle envelope and clear internal spacing'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/device'
    aliases = ()
    keywords = ('cd', 'disc', 'broken', 'cracked', 'damaged', 'media', 'storage', 'error', 'disk')

    def _circle(self, name, x, y, r):
        pts = [(x, y - r), (x + r, y), (x, y + r), (x - r, y), (x, y - r)]
        for i in range(4):
            self.add_arc(f'{name}-{i}', pts[i], pts[i + 1], radius_x=r, radius_y=r)
        self.add_contour(name, *[f'{name}-{i}' for i in range(4)], closed=True)

    def build(self):
        pts = [(12, 8), (4, 24), (24, 44), (44, 24), (24, 4)]
        for i in range(4):
            self.add_arc(f'rim-{i}', pts[i], pts[i + 1], radius_x=20, sweep=False)
        self.add_contour('rim', *[f'rim-{i}' for i in range(4)])
        self.add_polyline('crack', (24, 4), (16, 18), (29, 18), (18, 34))
        self.relate('connect', 'rim', 'crack')
