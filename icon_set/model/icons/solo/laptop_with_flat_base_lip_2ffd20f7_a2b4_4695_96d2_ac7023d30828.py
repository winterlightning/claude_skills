'laptop-with-flat-base-lip: Repositioned the outer contours to the exact keyshape width while retaining the defining details. Keyshape HRECT_L; SOLO48 stroke 4. Reviewed at 48 px in both themes.'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '2ffd20f7-a2b4-4695-96d2-ac7023d30828'
SOURCE_PATH = 'pictographic-primitives/computers/batch-02/laptop_2ffd20f7-a2b4-4695-96d2-ac7023d30828.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('2ffd20f7-a2b4-4695-96d2-ac7023d30828', 'pictographic-primitives/computers/batch-02/laptop_2ffd20f7-a2b4-4695-96d2-ac7023d30828.svg'),)

class LaptopWithFlatBaseLip(Solo48):
    icon_id = 'laptop-with-flat-base-lip'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'computers'
    aliases = ('notebook',)
    keywords = ('computer', 'screen', 'device', 'lucide-laptop')

    def build(self) -> None:
        self.add_line('screen-left', (6, 32), (6, 12))
        self.add_arc('screen-top-left', (6, 12), (10, 8), radius_x=4)
        self.add_line('screen-top', (10, 8), (38, 8))
        self.add_arc('screen-top-right', (38, 8), (42, 12), radius_x=4)
        self.add_line('screen-right', (42, 12), (42, 32))
        self.add_contour('screen', 'screen-left', 'screen-top-left', 'screen-top', 'screen-top-right', 'screen-right')
        self.add_polyline('base-top', (4, 32), (6, 32), (42, 32), (44, 32))
        self.add_arc('base-right', (44, 32), (38, 40), radius_x=6, radius_y=8)
        self.add_line('base-bottom', (38, 40), (10, 40))
        self.add_arc('base-left', (10, 40), (4, 32), radius_x=6, radius_y=8)
        self.add_contour('dish', 'base-right', 'base-bottom', 'base-left')
        self.relate('connect', 'screen', 'base-top')
        self.relate('connect', 'base-top', 'dish')
