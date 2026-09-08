"""A seated fortune teller reaching toward a crystal ball on a table. SQUARE extremes (2,2)-(46,46). The source image has one person; omit chair, cloth scallops and glints. Lucide user informs a circular head; retain the asymmetric scene."""

from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b3dff2fa-37b5-4c07-a64d-1c001573067f'
SOURCE_PATH = 'pictographic-primitives/culture/batch-03/sphere teller_b3dff2fa-37b5-4c07-a64d-1c001573067f.svg'
AUTHOR = 'astra-chatgpt'


class FortuneTellerReading(Solo48):
    icon_id = 'fortune-teller-reading'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "culture/objects"
    aliases = ()
    keywords = ('fortune teller', 'crystal ball', 'divination', 'psychic', 'reading', 'mystic', 'seance', 'future')

    def build(self) -> None:
        self.add_arc('head-top',(4,8),(16,8),radius_x=6)
        self.add_arc('head-bottom',(16,8),(4,8),radius_x=6)
        self.add_contour('head','head-top','head-bottom',closed=True)
        self.add_polyline('seated-body',(8,20),(2,34),(14,34),(18,46))
        self.add_polyline('reaching-arm',(8,20),(17,27),(22,24))
        self.relate('connect','seated-body','reaching-arm')
        self.add_arc('ball-top',(29,21),(45,21),radius_x=8)
        self.add_arc('ball-lower-right',(45,21),(37,29),radius_x=8)
        self.add_arc('ball-lower-left',(37,29),(29,21),radius_x=8)
        self.add_contour('crystal-ball','ball-top','ball-lower-right','ball-lower-left',closed=True)
        self.add_line('ball-stand',(37,29),(37,36))
        self.add_line('table-left',(26,36),(37,36))
        self.add_line('table-right',(37,36),(46,36))
        self.add_line('table-leg',(37,36),(37,46))
        self.relate('connect','crystal-ball','ball-stand')
        for member in ('table-left','table-right','table-leg'):
            self.relate('connect','ball-stand',member)
        self.relate('connect','table-left','table-right','table-leg')
