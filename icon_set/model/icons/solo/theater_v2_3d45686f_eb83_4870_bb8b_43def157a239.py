'theater: distinct review variant.\n\nConstruction: Theater with a straight overhead valance and two long flowing side drapes, distinct from the gathered curtains.\nKeyshape: SQUARE; exact SOLO48 envelope.\nConstruction reference: theater from the previously inspected Lucide original and atomic-debug library.\nPrevious canonical model is preserved.'
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = '3d45686f-eb83-4870-bb8b-43def157a239'
SOURCE_PATH = 'pictographic-primitives/symbol/theater_3d45686f-eb83-4870-bb8b-43def157a239.svg'
AUTHOR = 'gpt-6'


class TheaterVariant2(Solo48):
    icon_id = 'theater-v2'
    variant_of = 'theater'
    variant_label = 'Distinct subject and smooth curves'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('theater', 'symbol')
    keyshape = Keyshape.SQUARE

    def build(self):
        box(self,'frame',6,6,42,42,3,xs=(16,32),ys=(16,))
        line(self,'valance',(6,16),(42,16))
        path(self,'left-drape',(6,16),('C',(16,20),(16,32),(16,42)))
        path(self,'right-drape',(42,16),('C',(32,20),(32,32),(32,42)))
        contacts(self)
