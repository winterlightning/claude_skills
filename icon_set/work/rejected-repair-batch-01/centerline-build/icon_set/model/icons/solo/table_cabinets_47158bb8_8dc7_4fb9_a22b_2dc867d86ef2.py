'Desk and cabinets: preserve the chair and storage blocks, with clearer separation around the chair and table leg.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '47158bb8-8dc7-4fb9-a22b-2dc867d86ef2'
SOURCE_PATH = 'pictographic-primitives/office/table cabinets_47158bb8-8dc7-4fb9-a22b-2dc867d86ef2.svg'
AUTHOR = 'gpt-6'

class TableCabinets(Solo48):
    icon_id = 'table-cabinets'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'office'
    aliases = ()
    keywords = ('table', 'cabinets', 'office')

    def build(self) -> None:
        self.add_polyline('desk',(4,17),(4,8),(44,8),(44,40),(32,40),(32,17),(4,17))
        self.add_polyline('cabinet',(32,8),(32,17),(44,17));self.relate('connect','desk','cabinet')
        self.add_line('shelf',(32,28),(44,28));self.relate('connect','shelf','desk')
        self.add_line('leg',(4,27),(4,40))
        self.add_polyline('chair',(22,25),(21,31),(14,31))
        self.add_line('stand',(18,31),(18,37));self.relate('connect','stand','chair')
        self.add_polyline('chair-base',(13,40),(18,37),(23,40));self.relate('connect','stand','chair-base')
