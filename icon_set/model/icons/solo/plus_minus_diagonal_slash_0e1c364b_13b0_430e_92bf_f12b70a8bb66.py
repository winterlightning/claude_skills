"""Plus and minus separated by a rising slash form one arithmetic symbol. SQUARE keeps the slash diagonal and balances the signs across it. Plus shares one central node with equal arms; no details omitted. Source contributes arrangement; Lucide plus contributes orthogonal balanced strokes."""
from ._base import Solo48
from ...keyshapes import Keyshape
SOURCE_ICON_ID = '0e1c364b-13b0-430e-92bf-f12b70a8bb66'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_26/lus minus math symbol circle 1_0e1c364b-13b0-430e-92bf-f12b70a8bb66.svg'
AUTHOR = "gpt-6-astra"

class Drawing(Solo48):
    icon_id = 'plus-minus-diagonal-slash'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ('Plus and Minus Divided by Diagonal Slash',)
    keywords = ('plus', 'minus', 'diagonal', 'slash')
    def build(self):
        c = (12,12)
        for name, end in [('left',(6,12)),('right',(18,12)),('top',(12,6)),('bottom',(12,18))]:
            self.add_line('plus-'+name,c,end)
        self.relate('connect','plus-left','plus-right','plus-top','plus-bottom')
        self.add_line('slash',(6,42),(42,6))
        self.add_line('minus',(30,36),(42,36))
