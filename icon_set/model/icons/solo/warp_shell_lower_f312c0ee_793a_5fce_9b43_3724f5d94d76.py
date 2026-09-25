'warp-shell-lower: independent smooth-curve repair.\n\nConstruction: Shell bowl with two smoothly concave shoulders and a broad semicircular base.\nKeyshape: SQUARE; exact SOLO48 envelope.\nReference inspected: icon_set/references/lucide/original/shield.svg and atomic-debug/shield.svg (geometric construction).\nOriginal source and parent geometry preserved.'
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = 'f312c0ee-793a-5fce-9b43-3724f5d94d76'
SOURCE_PATH = 'pictographic-primitives/design/warp shell lower_f312c0ee-793a-5fce-9b43-3724f5d94d76.svg'
AUTHOR = 'gpt-6'


class WarpShellLower(Solo48):
    icon_id = 'warp-shell-lower'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    categories = ('design', 'primitives')
    aliases = ()
    keywords = ('warp', 'shell', 'lower', 'design')
    keyshape = Keyshape.SQUARE

    def build(self):
        path(self,'shell',(17,6),('L',(31,6)),('L',(31,10)),('C',(31,18),(35,20),(42,20)),('C',(42,34),(34,42),(24,42)),('C',(14,42),(6,34),(6,20)),('C',(13,20),(17,18),(17,10)),('L',(17,6)),closed=True)
        contacts(self)
