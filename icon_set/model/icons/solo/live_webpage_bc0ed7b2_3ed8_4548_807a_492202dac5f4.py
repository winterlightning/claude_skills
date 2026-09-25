'LIVE webpage: upright evenly spaced lettering above a simple browser baseline.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'bc0ed7b2-3ed8-4548-807a-492202dac5f4'
SOURCE_PATH = 'pictographic-primitives/websites/webpage live_bc0ed7b2-3ed8-4548-807a-492202dac5f4.svg'
AUTHOR = 'gpt-6'


class LiveWebpage(Solo48):
    icon_id = 'live-webpage'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'websites'
    aliases = ()
    keywords = ('live', 'webpage', 'broadcast', 'text', 'website', 'page', 'streaming')

    def build(self) -> None:
        # Symbol plan: preserve the subject, contour topology and curve types.
        # Rebalance whole parts on the SOLO48 integer grid; keep real shared contacts.
        self.add_line('l-1', (4, 8), (4, 24))
        self.add_line('l-2', (4, 24), (10, 24))
        self.add_line('i', (18, 8), (18, 24))
        self.add_line('v-1', (26, 8), (30, 24))
        self.add_line('v-2', (30, 24), (34, 8))
        self.add_line('e-1', (44, 8), (42, 8))
        self.add_line('e-2', (42, 8), (42, 24))
        self.add_line('e-3', (42, 24), (44, 24))
        self.add_line('e-bar', (42, 16), (44, 16))
        self.add_line('page-1', (4, 32), (4, 40))
        self.add_line('page-2', (4, 40), (44, 40))
        self.add_line('page-3', (44, 40), (44, 32))
        self.add_line('page-line', (14, 32), (34, 32))
        self.add_contour('l', *('l-1', 'l-2'), closed=False)
        self.add_contour('v', *('v-1', 'v-2'), closed=False)
        self.add_contour('e', *('e-1', 'e-2', 'e-3'), closed=False)
        self.add_contour('page', *('page-1', 'page-2', 'page-3'), closed=False)
        self.relate('connect', *('e', 'e-bar'))
