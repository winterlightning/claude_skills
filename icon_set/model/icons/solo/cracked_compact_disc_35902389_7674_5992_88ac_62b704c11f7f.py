"""Open the crack entry further around the rim and spread the zigzag so it has a clear gap to the disc edge. Applied to the original icon identity."""
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
    category = 'computers'
    aliases = ()
    keywords = ('cd', 'disc', 'broken', 'cracked', 'damaged', 'media', 'storage', 'error', 'disk')

    def build(self) -> None:
        """Symbol plan: Open the crack entry further around the rim and spread the zigzag so it has a clear gap to the disc edge. Reference: Lucide disc: one circular rim; deliberate asymmetric open crack."""

        def circle(name, cx, cy, radius):
            points = [(cx + radius, cy), (cx, cy + radius), (cx - radius, cy), (cx, cy - radius)]
            for i in range(4):
                self.add_arc(f'{name}-{i}', points[i], points[(i + 1) % 4], radius_x=radius)
            self.add_contour(name, *[f'{name}-{i}' for i in range(4)], closed=True)
        self.add_arc('rim-upper-left', (8, 12), (4, 24), radius_x=20, sweep=False)
        self.add_arc('rim-lower-left', (4, 24), (24, 44), radius_x=20, sweep=False)
        self.add_arc('rim-lower-right', (24, 44), (44, 24), radius_x=20, sweep=False)
        self.add_arc('rim-upper-right', (44, 24), (24, 4), radius_x=20, sweep=False)
        self.add_contour('rim', 'rim-upper-left', 'rim-lower-left', 'rim-lower-right', 'rim-upper-right')
        self.add_polyline('crack', (24, 4), (14, 20), (28, 20), (22, 32))
        self.relate('connect', 'rim', 'crack')
