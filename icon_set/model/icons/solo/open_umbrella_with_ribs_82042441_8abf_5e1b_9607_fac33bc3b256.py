"""An open umbrella with a scalloped canopy, two ribs and a right-turning hook handle."""

from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '82042441-8abf-5e1b-9607-fac33bc3b256'
SOURCE_PATH = 'pictographic-primitives/accessories/batch-01/umbrella_82042441-8abf-5e1b-9607-fac33bc3b256.svg'
AUTHOR = 'astra-chatgpt'


class OpenUmbrellaWithRibs(Solo48):
    icon_id = 'open-umbrella-with-ribs'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/accessories"
    aliases = ()
    keywords = ('umbrella', 'rain', 'parasol', 'weather', 'canopy', 'rib', 'handle', 'shelter')

    def build(self) -> None:
        # SQUARE: authored directly to its SOLO48 centerline extremes.
        self.add_arc('canopy-l', (2, 24), (24, 2), radius_x=22, radius_y=22, sweep=True)
        self.add_arc('canopy-r', (24, 2), (46, 24), radius_x=22, radius_y=22, sweep=True)
        self.add_arc('scallop-r', (46, 24), (34, 24), radius_x=6, radius_y=3, sweep=False)
        self.add_arc('scallop-mid-r', (34, 24), (24, 21), radius_x=10, radius_y=3, sweep=False)
        self.add_arc('scallop-mid-l', (24, 21), (14, 24), radius_x=10, radius_y=3, sweep=False)
        self.add_arc('scallop-l', (14, 24), (2, 24), radius_x=6, radius_y=3, sweep=False)
        self.add_contour('canopy', 'canopy-l', 'canopy-r', 'scallop-r', 'scallop-mid-r', 'scallop-mid-l', 'scallop-l', closed=True)
        self.add_arc('rib-l', (24, 2), (14, 24), radius_x=10, radius_y=22, sweep=False)
        self.add_arc('rib-r', (24, 2), (34, 24), radius_x=10, radius_y=22, sweep=True)
        self.relate("connect", 'rib-l', 'canopy')
        self.relate("connect", 'rib-r', 'canopy')
        self.relate("connect", 'rib-l', 'rib-r')
        self.add_line('shaft', (24, 21), (24, 40))
        self.add_arc('hook', (24, 40), (36, 40), radius_x=6, radius_y=6, sweep=False)
        self.add_line('hook-tip', (36, 40), (36, 36))
        self.add_contour('handle', 'shaft', 'hook', 'hook-tip', closed=False)
        self.relate("connect", 'handle', 'canopy')
