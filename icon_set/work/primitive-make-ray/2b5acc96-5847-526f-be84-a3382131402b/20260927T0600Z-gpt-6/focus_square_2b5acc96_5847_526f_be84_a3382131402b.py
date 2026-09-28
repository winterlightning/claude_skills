'focus-square: independent smooth-curve repair.\n\nConstruction: Four matching scan corners with true quarter arcs; content remains centered.\nKeyshape: SQUARE; exact SOLO48 envelope.\nReference inspected: icon_set/references/lucide/original/scan.svg and atomic-debug/scan.svg (geometric construction).\nOriginal source and parent geometry preserved.'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.icons.solo._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = '2b5acc96-5847-526f-be84-a3382131402b'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__focus-square/20260927T055558Z-thuan-mac-1/reference/focus square_2b5acc96-5847-526f-be84-a3382131402b.svg'
AUTHOR = "gpt-6"


class FocusSquare(Solo48):
    icon_id = 'focus-square'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'photography'
    categories = ('photography', 'primitives')
    aliases = ()
    keywords = ('focus', 'square', 'photography')
    keyshape = Keyshape.SQUARE

    def build(self) -> None:
        # Two concentric squares linked at the four side midpoints.
        self.add_polyline('outer',(6,6),(24,6),(42,6),(42,24),(42,42),(24,42),(6,42),(6,24),closed=True)
        self.add_polyline('inner',(16,16),(24,16),(32,16),(32,24),(32,32),(24,32),(16,32),(16,24),closed=True)
        for name,a,b in [('top',(24,6),(24,16)),('right',(42,24),(32,24)),('bottom',(24,42),(24,32)),('left',(6,24),(16,24))]:
            self.add_line('spoke-'+name,a,b)
            self.relate('connect','spoke-'+name,'outer')
            self.relate('connect','spoke-'+name,'inner')

