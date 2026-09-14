"""A LIVE webpage heading above a simplified page and footer compartment."""
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
    category = 'objects/interface'
    aliases = ()
    keywords = ('live', 'webpage', 'broadcast', 'text', 'website', 'page', 'streaming')

    def build(self) -> None:
        # Live HRECT_L centerline extremes: (6,8)-(42,40).
        # The four letters share a 16-unit cap height and an 8-unit minimum gap.
        top, middle, baseline = 8, 16, 24
        self.add_polyline('letter-l', (4,top), (4,baseline), (8,baseline))
        self.add_line('letter-i', (16,top), (16,baseline))
        self.add_polyline('letter-v', (24,top), (28,baseline), (32,top))
        self.add_polyline('letter-e-spine', (40,top), (40,middle), (40,baseline))
        for n,y in enumerate((top,middle,baseline)):
            self.add_line(f'letter-e-bar-{n}', (40,y), (44,y))
            self.relate('connect', f'letter-e-bar-{n}', 'letter-e-spine')
        # Open upper sides give the lettering its own room without shrinking it.
        self.add_polyline('page', (6,32), (6,40), (36,40), (42,40), (42,32), (36,32), (36,40))
        self.add_line('text', (12,32), (28,32))
