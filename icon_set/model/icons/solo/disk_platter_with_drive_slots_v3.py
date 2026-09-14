"""CIRCLE: center (24,24), centerline radius 20, visible ink radius 22. Lucide disc, disc-3 and glasses inform shared-center and paired construction."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '80af2806-9c69-5162-a492-892383b21556'
SOURCE_PATH = 'pictographic-primitives/computers/batch-04/floppy disk_80af2806-9c69-5162-a492-892383b21556.svg'
AUTHOR = 'gpt-6'

class DiskPlatterWithDriveSlotsVariant3(Solo48):
    icon_id = 'disk-platter-with-drive-slots-v3'
    variant_of = 'disk-platter-with-drive-slots'
    variant_label = 'Exact circle envelope and clear internal spacing'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/device'
    aliases = ()
    keywords = ('disk', 'platter', 'floppy', 'hub', 'storage', 'media', 'spindle', 'drive')

    def _circle(self, name, x, y, r):
        pts = [(x, y - r), (x + r, y), (x, y + r), (x - r, y), (x, y - r)]
        for i in range(4):
            self.add_arc(f'{name}-{i}', pts[i], pts[i + 1], radius_x=r, radius_y=r)
        self.add_contour(name, *[f'{name}-{i}' for i in range(4)], closed=True)

    def build(self):
        self._circle('rim', 24, 24, 20)
        self._circle('hub', 24, 24, 3)
        self.add_arc('slot-top', (22, 13), (26, 13), radius_x=3)
        self.add_line('slot-left', (14, 29), (15, 31))
        self.add_line('slot-right', (34, 29), (33, 31))
