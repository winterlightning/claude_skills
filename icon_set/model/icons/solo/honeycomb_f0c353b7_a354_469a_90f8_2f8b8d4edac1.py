'honeycomb: independent smooth-curve repair.\n\nConstruction: Three joined honeycomb cells derived from one shared grid; shared walls emitted once.\nKeyshape: SQUARE; exact SOLO48 envelope.\nReference inspected: icon_set/references/lucide/original/hexagon.svg and atomic-debug/hexagon.svg (geometric construction).\nOriginal source and parent geometry preserved.'
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = 'f0c353b7-a354-469a-90f8-2f8b8d4edac1'
SOURCE_PATH = 'pictographic-primitives/symbol/honeycomb_f0c353b7-a354-469a-90f8-2f8b8d4edac1.svg'
AUTHOR = 'gpt-6'


class Honeycomb(Solo48):
    icon_id = 'honeycomb'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    categories = ('symbol', 'state')
    aliases = ()
    keywords = ('honeycomb', 'symbol')
    keyshape = Keyshape.SQUARE

    def build(self):
        poly(self,'top',(24,6),(34,12),(34,24),(24,30),(14,24),(14,12),closed=True)
        poly(self,'left',(14,24),(6,29),(6,37),(14,42),(24,37),(24,30))
        poly(self,'right',(34,24),(42,29),(42,37),(34,42),(24,37))
        contacts(self)
