'helmet-83968c0b: independent smooth-curve repair.\n\nConstruction: Protective helmet with a smooth dome and narrow center ridge; broad brim. Simplified redundant ridge walls to one centerline.\nKeyshape: HRECT_L; exact SOLO48 envelope.\nReference inspected: icon_set/references/lucide/original/hard-hat.svg and atomic-debug/hard-hat.svg (geometric construction).\nOriginal source and parent geometry preserved.'
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = '83968c0b-0769-4e90-a1c4-33974d290536'
SOURCE_PATH = 'pictographic-primitives/protection/helmet_83968c0b-0769-4e90-a1c4-33974d290536.svg'
AUTHOR = 'gpt-6'


class Helmet83968c0bVariant2(Solo48):
    icon_id = 'helmet-83968c0b-v2'
    variant_of = 'helmet-83968c0b'
    variant_label = 'Smooth curves and symmetry'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'protection'
    aliases = ()
    keywords = ('helmet', 'protection')
    keyshape = Keyshape.HRECT_L

    def build(self):
        path(self,'dome',(8,30),('L',(8,24)),('A',16,16,True,(24,8)),('A',16,16,True,(40,24)),('L',(40,30)))
        box(self,'brim',4,30,44,40,3,xs=(8,40))
        line(self,'ridge',(24,8),(24,24))
        contacts(self)
