"""Zener diode (electronics), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5761e51b-6ba1-422a-83d1-966f39538a63'
SOURCE_PATH = 'icons-json/electronics/zener diode_5761e51b-6ba1-422a-83d1-966f39538a63.json'
AUTHOR = 'gpt-6'

class ZenerDiode(Solo48):
    icon_id = 'zener-diode'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'electronics'
    aliases = ()
    keywords = ('zener', 'diode', 'electronics')

    def build(self) -> None:
        # Symbol plan: preserve the subject, contour topology and curve types.
        # Rebalance whole parts on the SOLO48 integer grid; keep real shared contacts.
        self.add_line('e0', (32, 8), (32, 24))
        self.add_line('e1', (4, 24), (14, 24))
        self.add_line('e2', (34, 40), (32, 24))
        self.add_line('e3', (44, 24), (32, 24))
        self.add_line('e4', (14, 8), (14, 40))
        self.add_line('e5', (14, 40), (32, 24))
        self.add_line('e6', (32, 24), (14, 8))
        self.add_contour('c0', *('e0',), closed=False)
        self.add_contour('c1', *('e1',), closed=False)
        self.add_contour('c2', *('e2',), closed=False)
        self.add_contour('c3', *('e3',), closed=False)
        self.add_contour('c4', *('e4', 'e5', 'e6'), closed=True)
        self.relate('connect', *('c0', 'c2'))
        self.relate('connect', *('c0', 'c3'))
        self.relate('connect', *('c2', 'c3'))
        self.relate('connect', *('c1', 'c4'))
