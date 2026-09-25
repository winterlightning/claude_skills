'Disc platter with three short slots and a radius-two hub. Tangential slots retain visible lengths and safe radial clearance; Lucide disc informs the circles. CIRCLE visible radius 22; SOLO48 stroke 4.'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '80af2806-9c69-5162-a492-892383b21556'
SOURCE_PATH = 'pictographic-primitives/computers/batch-04/floppy disk_80af2806-9c69-5162-a492-892383b21556.svg'
AUTHOR = 'gpt-6'

class DiskPlatterWithDriveSlots(Solo48):
    icon_id = 'disk-platter-with-drive-slots'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'computers'
    categories = ('computers', 'primitives')
    aliases = ()
    keywords = ('disk', 'platter', 'floppy', 'hub', 'storage', 'media', 'spindle', 'drive')

    def build(self) -> None:
        # CIRCLE envelope: center (24,24), centerline radius 20, visible radius 22.
        # Shared cardinal nodes keep concentric geometry and attachments exact.
        def circle(name, cx, cy, radius):
            points = [(cx + radius, cy), (cx, cy + radius), (cx - radius, cy), (cx, cy - radius)]
            for i in range(4):
                self.add_arc(f'{name}-{i}', points[i], points[(i + 1) % 4], radius_x=radius)
            self.add_contour(name, *[f'{name}-{i}' for i in range(4)], closed=True)
        circle('rim', 24, 24, 20)
        self.add_dot('hub', (24,24))
        self.add_line('slot-top', (23, 13), (25, 13))
        for side in (-1, 1):
            self.add_line('slot-left' if side < 0 else 'slot-right', (24 + side * 10, 28), (24 + side * 9, 30))
