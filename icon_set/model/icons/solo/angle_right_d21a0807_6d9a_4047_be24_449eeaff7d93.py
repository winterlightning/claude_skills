'angle-right: independent smooth-curve repair.\n\nConstruction: A horizontal arrow with equal diagonal arms and one exact central junction.\nKeyshape: HRECT_L; exact SOLO48 envelope.\nReference inspected: icon_set/references/lucide/original/arrow-right.svg and atomic-debug/arrow-right.svg (geometric construction).\nOriginal source and parent geometry preserved.'
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = 'd21a0807-6d9a-4047-be24-449eeaff7d93'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_03/angle right_d21a0807-6d9a-4047-be24-449eeaff7d93.svg'
AUTHOR = 'gpt-6'


class AngleRight(Solo48):
    icon_id = 'angle-right'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = '_uncategorized_03'
    aliases = ()
    keywords = ('angle', 'right', '_uncategorized_03')
    keyshape = Keyshape.HRECT_L

    def build(self):
        poly(self,'head',(28,8),(44,24),(28,40))
        line(self,'shaft',(4,24),(44,24))
        contacts(self)
