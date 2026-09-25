"""A centered plus above a wider minus bar. SQUARE gives equal margins and 12 centerline separation below the plus. Plus arms derive from center24,18 with length12. Source provides stacked arrangement; Lucide plus supplies equal-arm construction. No details omitted."""
from ._base import Solo48
from ...keyshapes import Keyshape
SOURCE_ICON_ID = '434fcb89-ecc7-432c-9116-0fdf6e094dc0'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_26/lus minus math symbol circle 2_434fcb89-ecc7-432c-9116-0fdf6e094dc0.svg'
AUTHOR = "gpt-6-astra"

class Drawing(Solo48):
    icon_id = 'plus-above-minus'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ('Plus Sign Above Separate Minus Bar',)
    keywords = ('plus', 'above', 'minus')
    def build(self):
        c = (24,18)
        for name, end in [('left',(12,18)),('right',(36,18)),('top',(24,6)),('bottom',(24,30))]:
            self.add_line('plus-'+name,c,end)
        self.relate('connect','plus-left','plus-right','plus-top','plus-bottom')
        self.add_line('minus',(6,42),(42,42))
