'helmet: independent smooth-curve repair.\n\nConstruction: Protective helmet with a smooth dome and narrow center ridge; broad brim. Simplified redundant ridge walls to one centerline.\nKeyshape: HRECT_L; exact SOLO48 envelope.\nReference inspected: icon_set/references/lucide/original/hard-hat.svg and atomic-debug/hard-hat.svg (geometric construction).\nOriginal source and parent geometry preserved.'
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = '0209d9df-8004-4d01-8d63-b5f783021ddb'
SOURCE_PATH = 'pictographic-primitives/protection/helmet_0209d9df-8004-4d01-8d63-b5f783021ddb.svg'
AUTHOR = 'gpt-6'


class HelmetVariant2(Solo48):
    icon_id = 'helmet-v2'
    variant_of = 'helmet'
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
