'construction-hard-hat: Repositioned the outer contours to the exact keyshape width while retaining the defining details. Keyshape HRECT_L; SOLO48 stroke 4. Reviewed at 48 px in both themes.'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'b14b6641-0dd7-524f-a069-fc2f7884f0f3'
SOURCE_PATH = 'pictographic-primitives/accessories/batch-03/hat architect_b14b6641-0dd7-524f-a069-fc2f7884f0f3.svg'
AUTHOR = 'gpt-6'

class ConstructionHardHat(Solo48):
    icon_id = 'construction-hard-hat'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'accessories'
    aliases = ()
    keywords = ('hard hat', 'helmet', 'construction', 'safety', 'builder', 'architect', 'worker', 'headwear')

    def build(self) -> None:
        self.add_line('brim-0', (8, 30), (40, 30))
        self.add_arc('brim-1', (40, 30), (44, 34), radius_x=4, radius_y=4, sweep=True)
        self.add_line('brim-2', (44, 34), (44, 36))
        self.add_arc('brim-3', (44, 36), (40, 40), radius_x=4, radius_y=4, sweep=True)
        self.add_line('brim-4', (40, 40), (8, 40))
        self.add_arc('brim-5', (8, 40), (4, 36), radius_x=4, radius_y=4, sweep=True)
        self.add_line('brim-6', (4, 36), (4, 34))
        self.add_arc('brim-7', (4, 34), (8, 30), radius_x=4, radius_y=4, sweep=True)
        self.add_contour('brim', 'brim-0', 'brim-1', 'brim-2', 'brim-3', 'brim-4', 'brim-5', 'brim-6', 'brim-7', closed=True)
        self.add_arc('shell-left', (8, 30), (18, 12), radius_x=10, radius_y=18, sweep=True)
        self.add_arc('shell-right', (30, 12), (40, 30), radius_x=10, radius_y=18, sweep=True)
        self.add_line('badge-0', (21, 8), (27, 8))
        self.add_arc('badge-1', (27, 8), (30, 11), radius_x=3, radius_y=3, sweep=True)
        self.add_line('badge-2-attach-0', (30, 11), (30, 12))
        self.add_line('badge-2-attach-1', (30, 12), (30, 18))
        self.add_arc('badge-3', (30, 18), (27, 21), radius_x=3, radius_y=3, sweep=True)
        self.add_line('badge-4', (27, 21), (21, 21))
        self.add_arc('badge-5', (21, 21), (18, 18), radius_x=3, radius_y=3, sweep=True)
        self.add_line('badge-6-attach-0', (18, 18), (18, 12))
        self.add_line('badge-6-attach-1', (18, 12), (18, 11))
        self.add_arc('badge-7', (18, 11), (21, 8), radius_x=3, radius_y=3, sweep=True)
        self.add_contour('badge', 'badge-0', 'badge-1', 'badge-2-attach-0', 'badge-2-attach-1', 'badge-3', 'badge-4', 'badge-5', 'badge-6-attach-0', 'badge-6-attach-1', 'badge-7', closed=True)
        self.relate('connect', 'shell-left', 'brim')
        self.relate('connect', 'shell-right', 'brim')
        self.relate('connect', 'shell-left', 'badge')
        self.relate('connect', 'shell-right', 'badge')
