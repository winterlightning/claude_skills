"""A dining table stands beside one tall-backed chair. HRECT_L 4..44 x 8..40 gives room for distinct furniture. Source supplies left chair and right table; Lucide armchair reference considered for shared seat-leg nodes. Simplify outlined thin rails to single strokes. Table legs share height; chair joints use real endpoints."""
from ._base import Solo48
from ...keyshapes import Keyshape
SOURCE_ICON_ID = '0541c5ec-dbcc-416d-8de4-70b007cb32f0'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_15/dining table_0541c5ec-dbcc-416d-8de4-70b007cb32f0.svg'
AUTHOR = 'gpt-6-astra'
class Drawing(Solo48):
    icon_id = 'dining-table-with-single-side-chair'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'Uncategorized'
    aliases = ['Dining Table with Single Side Chair']
    keywords = ['table', 'chair', 'dining', 'furniture', 'seat', 'legs', 'interior']
    def build(self):
        self.add_line('chair-back',(4,8),(4,28))
        self.add_line('chair-seat',(4,28),(16,28))
        self.add_line('chair-left-leg',(4,28),(4,40))
        self.add_line('chair-right-leg',(16,28),(16,40))
        self.relate('connect','chair-back','chair-seat','chair-left-leg')
        self.relate('connect','chair-seat','chair-right-leg')
        self.add_line('table-top',(24,20),(44,20))
        for x in (24,44):
            self.add_line('table-leg-'+str(x),(x,20),(x,40))
            self.relate('connect','table-top','table-leg-'+str(x))
