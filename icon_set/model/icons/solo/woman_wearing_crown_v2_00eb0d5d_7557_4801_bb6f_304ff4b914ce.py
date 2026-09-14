"""Three-point crown, center-parted face outline and straight long hair. Facial marks and outward hair flares omitted.
Lucide hand, crown and user/laptop construction; independently revised on SOLO48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '00eb0d5d-7557-4801-bb6f-304ff4b914ce'
SOURCE_PATH = 'pictographic-primitives/work/workflow manager female crown_00eb0d5d-7557-4801-bb6f-304ff4b914ce.svg'
AUTHOR = 'gpt-6'

class WomanWearingCrownVariant2(Solo48):
    icon_id = 'woman-wearing-crown-v2'
    variant_of = 'woman-wearing-crown'
    variant_label = 'Cleaner silhouette and spacing'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/work'
    aliases = ()
    keywords = ('woman', 'crown', 'queen', 'leader', 'head', 'royalty')

    def build(self) -> None:
        self.add_polyline('crown', (14, 16), (10, 4), (18, 10), (24, 4), (30, 10), (38, 4), (34, 16), closed=True)
        self.add_line('hair-left-side', (8, 44), (8, 32))
        self.add_arc('hair-left-top', (8, 32), (24, 16), radius_x=16, radius_y=16, sweep=True, large_arc=False)
        self.add_arc('hair-right-top', (24, 16), (40, 32), radius_x=16, radius_y=16, sweep=True, large_arc=False)
        self.add_line('hair-right-side', (40, 32), (40, 44))
        self.add_contour('hair', 'hair-left-side', 'hair-left-top', 'hair-right-top', 'hair-right-side', closed=False)
        self.relate("connect", 'hair', 'crown')
        self.add_arc('part-left', (17, 25), (24, 16), radius_x=7, radius_y=9, sweep=True, large_arc=False)
        self.add_arc('part-right', (24, 16), (31, 25), radius_x=7, radius_y=9, sweep=True, large_arc=False)
        self.add_line('cheek-right', (31, 25), (31, 32))
        self.add_arc('chin', (31, 32), (17, 32), radius_x=7, radius_y=8, sweep=True, large_arc=False)
        self.add_line('cheek-left', (17, 32), (17, 25))
        self.add_contour('face', 'part-left', 'part-right', 'cheek-right', 'chin', 'cheek-left', closed=True)
        self.relate("connect", 'face', 'crown')
        self.relate("connect", 'face', 'hair')
