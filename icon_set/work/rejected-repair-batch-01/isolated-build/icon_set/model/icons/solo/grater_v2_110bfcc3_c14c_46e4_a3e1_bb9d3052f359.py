'grater: independent smooth-curve repair.\n\nConstruction: Tapered grater silhouette with a broad rounded top handle and exact mirrored sides.\nKeyshape: VRECT_L; exact SOLO48 envelope.\nReference inspected: icon_set/references/lucide/original/bottle-wine.svg and atomic-debug/bottle-wine.svg (geometric construction).\nOriginal source and parent geometry preserved.'
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = '110bfcc3-c14c-46e4-a3e1-bb9d3052f359'
SOURCE_PATH = 'pictographic-primitives/food/grater_110bfcc3-c14c-46e4-a3e1-bb9d3052f359.svg'
AUTHOR = 'gpt-6'


class GraterVariant2(Solo48):
    icon_id = 'grater-v2'
    variant_of = 'grater'
    variant_label = 'Smooth curves and symmetry'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    aliases = ()
    keywords = ('grater', 'food')
    keyshape = Keyshape.VRECT_L

    def build(self):
        path(self,'body',(8,44),('L',(10,14)),('C',(10,8),(16,4),(24,4)),('C',(32,4),(38,8),(38,14)),('L',(40,44)),('L',(8,44)),closed=True)
        line(self,'rim',(10,14),(38,14))
        contacts(self)
