"""Protective laboratory goggles with a smooth lens, nose recess and paired arms. Repaired in place from bad-stroke feedback."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'c6456c8f-9c22-54f5-8ffc-ddc18ca120ed'
SOURCE_PATH = 'pictographic-primitives/science/lab protection glasses_c6456c8f-9c22-54f5-8ffc-ddc18ca120ed.svg'
AUTHOR = 'gpt-6'

class LabProtectionGlasses(Solo48):
    icon_id = 'lab-protection-glasses'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'science'
    categories = ('science', 'primitives')
    aliases = ()
    keywords = ('lab', 'protection', 'glasses', 'science')

    def build(self) -> None:
        # A single protective lens with a rounded nose recess and mirrored arms.
        # Lucide glasses informs equal temple hooks and bilateral construction.
        # HRECT_L centerline extremes: (4, 8)-(44, 40).
        self.add_line('brow', (8, 20), (40, 20))
        self.add_arc('upper-right', (40, 20), (44, 24), radius_x=4)
        self.add_line('right-side', (44, 24), (44, 32))
        self.add_arc('right-bottom', (44, 32), (36, 40), radius_x=8)
        self.add_arc('right-nose', (36, 40), (28, 32), radius_x=8)
        self.add_arc('nose-bridge', (28, 32), (20, 32), radius_x=4, sweep=False)
        self.add_arc('left-nose', (20, 32), (12, 40), radius_x=8)
        self.add_arc('left-bottom', (12, 40), (4, 32), radius_x=8)
        self.add_line('left-side', (4, 32), (4, 24))
        self.add_arc('upper-left', (4, 24), (8, 20), radius_x=4)
        self.add_contour('lens', 'brow', 'upper-right', 'right-side', 'right-bottom',
                         'right-nose', 'nose-bridge', 'left-nose', 'left-bottom',
                         'left-side', 'upper-left', closed=True)
        for side in ('left', 'right'):
            x = (lambda value: value) if side == 'left' else (lambda value: 48 - value)
            self.add_arc(side + '-hook', (x(18), 12), (x(10), 12),
                         radius_x=4, sweep=side == 'right')
            self.add_line(side + '-arm', (x(10), 12), (x(8), 20))
            self.add_contour(side + '-temple', side + '-hook', side + '-arm')
            self.relate('connect', 'lens', side + '-temple')
