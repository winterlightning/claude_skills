'Open disc with an asymmetric lightning crack; Lucide disc informs the enclosing contour. Hub absent in source. CIRCLE visible radius 22; SOLO48 stroke 4.'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '35902389-7674-5992-88ac-62b704c11f7f'
SOURCE_PATH = 'pictographic-primitives/computers/batch-04/cd broken_35902389-7674-5992-88ac-62b704c11f7f.svg'
AUTHOR = 'gpt-6'

class CrackedCompactDisc(Solo48):
    icon_id = 'cracked-compact-disc'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/device'
    aliases = ()
    keywords = ('cd', 'disc', 'broken', 'cracked', 'damaged', 'media', 'storage', 'error', 'disk')

    def build(self) -> None:
        # CIRCLE envelope: center (24,24), centerline radius 20, visible radius 22.
        # Shared cardinal nodes keep concentric geometry and attachments exact.
        def circle(name, cx, cy, radius):
            points = [(cx + radius, cy), (cx, cy + radius), (cx - radius, cy), (cx, cy - radius)]
            for i in range(4):
                self.add_arc(f'{name}-{i}', points[i], points[(i + 1) % 4], radius_x=radius)
            self.add_contour(name, *[f'{name}-{i}' for i in range(4)], closed=True)
        self.add_arc('rim-upper-left', (12, 8), (4, 24), radius_x=20, sweep=False)
        self.add_arc('rim-lower-left', (4, 24), (24, 44), radius_x=20, sweep=False)
        self.add_arc('rim-lower-right', (24, 44), (44, 24), radius_x=20, sweep=False)
        self.add_arc('rim-upper-right', (44, 24), (24, 4), radius_x=20, sweep=False)
        self.add_contour('rim', 'rim-upper-left', 'rim-lower-left', 'rim-lower-right', 'rim-upper-right')
        self.add_polyline('crack', (24, 4), (16, 18), (29, 18), (18, 34))
        self.relate('connect', 'rim', 'crack')
