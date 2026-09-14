# Variant of academic-graduation-cap; parent file remains unchanged.
"""Diamond mortarboard above a curved crown. Lucide graduation-cap informs the board and elliptical crown; no tassel in source."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'ac0c8839-9020-4a65-9a30-af5a45d63503'
SOURCE_PATH = 'pictographic-primitives/accessories/batch-07/cap_ac0c8839-9020-4a65-9a30-af5a45d63503.svg'
AUTHOR = 'astra-chatgpt'

class AcademicGraduationCapVariant2(Solo48):
    icon_id = 'academic-graduation-cap-v2'
    variant_of = 'academic-graduation-cap'
    variant_label = 'Correct width and full spacing review'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/accessories'
    aliases = ()
    keywords = ('academic', 'graduation', 'cap')

    def build(self) -> None:
        self.add_polyline('board', (2, 18), (24, 8), (46, 18), (35, 23), (24, 28), (13, 23), closed=True)
        self.add_line('crown-right', (35, 23), (35, 32))
        self.add_arc('crown-bottom', (35, 32), (13, 32), radius_x=11, radius_y=8)
        self.add_line('crown-left', (13, 32), (13, 23))
        self.add_contour('crown', 'crown-right', 'crown-bottom', 'crown-left')
        self.relate('connect', 'board', 'crown')
