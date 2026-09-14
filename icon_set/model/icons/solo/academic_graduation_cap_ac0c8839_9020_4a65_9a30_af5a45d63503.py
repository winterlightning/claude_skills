'academic-graduation-cap: Repositioned the outer contours to the exact keyshape width while retaining the defining details. Keyshape HRECT_L; SOLO48 stroke 4. Reviewed at 48 px in both themes.'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'ac0c8839-9020-4a65-9a30-af5a45d63503'
SOURCE_PATH = 'pictographic-primitives/accessories/batch-07/cap_ac0c8839-9020-4a65-9a30-af5a45d63503.svg'
AUTHOR = 'gpt-6'

class AcademicGraduationCap(Solo48):
    icon_id = 'academic-graduation-cap'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/accessories'
    aliases = ()
    keywords = ('academic', 'graduation', 'cap')

    def build(self) -> None:
        self.add_polyline('board', (4, 18), (24, 8), (44, 18), (35, 23), (24, 28), (13, 23), closed=True)
        self.add_line('crown-right', (35, 23), (35, 32))
        self.add_arc('crown-bottom', (35, 32), (13, 32), radius_x=11, radius_y=8)
        self.add_line('crown-left', (13, 32), (13, 23))
        self.add_contour('crown', 'crown-right', 'crown-bottom', 'crown-left')
        self.relate('connect', 'board', 'crown')
