'massage-pillow: independent smooth-curve repair.\n\nConstruction: Soft pillow perimeter with broad concave sides and paired curved recess marks.\nKeyshape: SQUARE; exact SOLO48 envelope.\nReference inspected: icon_set/references/lucide/original/rectangle-horizontal.svg and atomic-debug/rectangle-horizontal.svg (geometric construction).\nOriginal source and parent geometry preserved.'
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = '91f652e5-405c-55eb-a732-b57512c93cdb'
SOURCE_PATH = 'pictographic-primitives/health/massage pillow_91f652e5-405c-55eb-a732-b57512c93cdb.svg'
AUTHOR = 'gpt-6'


class MassagePillowVariant2(Solo48):
    icon_id = 'massage-pillow-v2'
    variant_of = 'massage-pillow'
    variant_label = 'Smooth curves and symmetry'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'health'
    aliases = ()
    keywords = ('massage', 'pillow', 'health')
    keyshape = Keyshape.SQUARE

    def build(self):
        path(self,'pillow',(6,6),('C',(17,10),(31,10),(42,6)),('C',(38,17),(38,31),(42,42)),('C',(31,38),(17,38),(6,42)),('C',(10,31),(10,17),(6,6)),closed=True)
        path(self,'left-mark',(20,17),('C',(18,21),(18,27),(20,31)))
        path(self,'right-mark',(28,17),('C',(30,21),(30,27),(28,31)))
        contacts(self)
