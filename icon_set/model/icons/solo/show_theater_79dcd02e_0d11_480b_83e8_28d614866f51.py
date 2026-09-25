'show-theater: independent smooth-curve repair.\n\nConstruction: Theater stage with flowing paired curtain sweeps; curtain edges meet exact frame nodes.\nKeyshape: SQUARE; exact SOLO48 envelope.\nReference inspected: icon_set/references/lucide/original/theater.svg and atomic-debug/theater.svg (geometric construction).\nOriginal source and parent geometry preserved.'
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = '79dcd02e-0d11-480b-83e8-28d614866f51'
SOURCE_PATH = 'pictographic-primitives/entertainment/show theater_79dcd02e-0d11-480b-83e8-28d614866f51.svg'
AUTHOR = 'gpt-6'


class ShowTheater(Solo48):
    icon_id = 'show-theater'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'entertainment'
    categories = ('entertainment', 'primitives')
    aliases = ()
    keywords = ('show', 'theater', 'entertainment')
    keyshape = Keyshape.SQUARE

    def build(self):
        box(self,'frame',6,6,42,42,3,xs=(24,),ys=(24,))
        path(self,'left-curtain',(24,6),('C',(24,16),(16,24),(6,24)))
        path(self,'right-curtain',(24,6),('C',(24,16),(32,24),(42,24)))
        path(self,'left-tail',(6,24),('C',(13,28),(16,34),(16,42)))
        path(self,'right-tail',(42,24),('C',(35,28),(32,34),(32,42)))
        contacts(self)
