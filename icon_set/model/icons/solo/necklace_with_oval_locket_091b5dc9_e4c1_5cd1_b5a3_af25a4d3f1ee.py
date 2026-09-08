"""Wide U necklace with oval locket. SQUARE extremes (2,2)-(46,46). Tiny bail simplified to connector; symmetric ellipse arcs. No useful Lucide match."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '091b5dc9-e4c1-5cd1-b5a3-af25a4d3f1ee'
SOURCE_PATH = 'pictographic-primitives/accessories/batch-03/necklace locket_091b5dc9-e4c1-5cd1-b5a3-af25a4d3f1ee.svg'
AUTHOR = 'astra-chatgpt'


class NecklaceWithOvalLocket(Solo48):
    icon_id = 'necklace-with-oval-locket'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/accessories"
    aliases = ()
    keywords = ('necklace', 'locket', 'pendant', 'oval', 'chain', 'jewellery', 'jewelry', 'accessory')

    def build(self) -> None:
        self.add_arc('chain-left', (2, 2), (24, 21), radius_x=22, radius_y=19, sweep=False)
        self.add_arc('chain-right', (24, 21), (46, 2), radius_x=22, radius_y=19, sweep=False)
        self.add_contour('chain', 'chain-left', 'chain-right', closed=False)
        self.add_line('bail', (24, 21), (24, 28))
        self.add_arc('locket-0', (24, 28), (31, 37), radius_x=7, radius_y=9, sweep=True)
        self.add_arc('locket-1', (31, 37), (24, 46), radius_x=7, radius_y=9, sweep=True)
        self.add_arc('locket-2', (24, 46), (17, 37), radius_x=7, radius_y=9, sweep=True)
        self.add_arc('locket-3', (17, 37), (24, 28), radius_x=7, radius_y=9, sweep=True)
        self.add_contour('locket', 'locket-0', 'locket-1', 'locket-2', 'locket-3', closed=True)
        self.relate("connect", 'chain', 'bail')
        self.relate("connect", 'bail', 'locket')
