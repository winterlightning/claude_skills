"""A-shaped mast with crossbar and signal arcs. Lucide radio-tower informs the mast and paired curves. Reduced two wave pairs to one pair to preserve clearance around the mast.

SOLO48 SQUARE; live visible envelope (4, 4, 44, 44).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'eb0a1297-ca44-44fa-a815-5e5ae09e5934'
SOURCE_PATH = 'pictographic-primitives/symbol/signal antenna_eb0a1297-ca44-44fa-a815-5e5ae09e5934.svg'
AUTHOR = 'gpt-6'


class AntennaSignal(Solo48):
    icon_id = 'antenna-signal'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "symbol"
    categories = ("symbol", "state")
    aliases = ()
    keywords = ('antenna', 'signal', 'broadcast', 'radio', 'tower', 'wireless', 'transmission', 'hotspot')

    def build(self) -> None:

        self.add_polyline('mast',(12,42),(18,28),(24,14),(30,28),(36,42))
        self.add_line('crossbar',(18,28),(30,28))
        self.relate('connect','mast','crossbar')
        self.add_arc('wave-left',(10,6),(10,22),radius_x=4,radius_y=8,sweep=False)
        self.add_arc('wave-right',(38,6),(38,22),radius_x=4,radius_y=8)
