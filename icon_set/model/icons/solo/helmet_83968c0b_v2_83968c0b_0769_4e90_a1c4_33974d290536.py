'helmet-83968c0b: distinct review variant.\n\nConstruction: Broad safety helmet with a single lower rim and a center ridge; the shell itself reaches the outer width.\nKeyshape: HRECT_L; exact SOLO48 envelope.\nConstruction reference: hard-hat from the previously inspected Lucide original and atomic-debug library.\nPrevious canonical model is preserved.'
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = '83968c0b-0769-4e90-a1c4-33974d290536'
SOURCE_PATH = 'pictographic-primitives/protection/helmet_83968c0b-0769-4e90-a1c4-33974d290536.svg'
AUTHOR = 'gpt-6'


class Helmet83968c0bVariant2(Solo48):
    icon_id = 'helmet-83968c0b-v2'
    variant_of = 'helmet-83968c0b'
    variant_label = 'Distinct subject and smooth curves'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'protection'
    aliases = ()
    keywords = ('helmet', 'protection')
    keyshape = Keyshape.HRECT_L

    def build(self):
        path(self,'shell',(4,40),('L',(4,28)),('A',20,20,True,(24,8)),('A',20,20,True,(44,28)),('L',(44,40)),('L',(4,40)),closed=True)
        line(self,'ridge',(24,8),(24,24))
        contacts(self)
