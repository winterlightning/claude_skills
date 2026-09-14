"""Resistor (electronics), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a3c8bc32-4fd0-5a98-8e0a-20f80c3fed92'
SOURCE_PATH = 'icons-json/electronics/resistor_a3c8bc32-4fd0-5a98-8e0a-20f80c3fed92.json'
AUTHOR = 'gpt-6'

class Resistor(Solo48):
    icon_id = 'resistor'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'electronics'
    aliases = ()
    keywords = ('resistor', 'electronics')

    def build(self) -> None:
        # Symbol plan: preserve the subject, contour topology and curve types.
        # Rebalance whole parts on the SOLO48 integer grid; keep real shared contacts.
        self.add_line('e0', (19, 8), (16, 25))
        self.add_line('e1', (16, 25), (4, 25))
        self.add_line('e2', (24, 40), (19, 8))
        self.add_line('e3', (24, 40), (29, 9))
        self.add_line('e4', (29, 9), (34, 35))
        self.add_line('e5', (34, 35), (36, 26))
        self.add_line('e6', (36, 26), (44, 26))
        self.add_contour('c0', *('e0', 'e1'), closed=False)
        self.add_contour('c1', *('e2',), closed=False)
        self.add_contour('c2', *('e3', 'e4', 'e5', 'e6'), closed=False)
        self.relate('connect', *('c0', 'c1'))
