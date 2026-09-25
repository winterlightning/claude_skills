'Koala: round head and ear, smooth sitting back and a single clear gripping arm on the branch.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '95f00a8c-536e-5767-97fa-8968fad8e99a'
SOURCE_PATH = 'pictographic-primitives/animals/koala bamboo_95f00a8c-536e-5767-97fa-8968fad8e99a.svg'
AUTHOR = 'gpt-6'


class KoalaWithBranch(Solo48):
    icon_id = 'koala-with-branch'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "animals"
    aliases = ()
    keywords = ('koala', 'branch', 'eucalyptus', 'holding', 'marsupial', 'australia', 'animal', 'sitting')

    def build(self) -> None:
        # Symbol plan: preserve the subject, contour topology and curve types.
        # Rebalance whole parts on the SOLO48 integer grid; keep real shared contacts.
        self.add_arc('head-top', (10, 18), (30, 18), radius_x=10, radius_y=10, large_arc=False, sweep=True)
        self.add_arc('head-bottom', (30, 18), (10, 18), radius_x=10, radius_y=10, large_arc=False, sweep=True)
        self.add_line('ear-top-1', (20, 8), (16, 6))
        self.add_line('ear-top-2', (16, 6), (10, 6))
        self.add_arc('ear-left', (10, 6), (6, 10), radius_x=4, radius_y=4, large_arc=False, sweep=False)
        self.add_line('ear-side', (6, 10), (6, 14))
        self.add_arc('ear-bottom', (6, 14), (10, 18), radius_x=4, radius_y=4, large_arc=False, sweep=False)
        self.add_line('nose', (20, 18), (20, 18))
        self.add_arc('back', (12, 24), (10, 36), radius_x=18, radius_y=14, large_arc=False, sweep=False)
        self.add_arc('bottom', (10, 36), (20, 42), radius_x=10, radius_y=6, large_arc=False, sweep=False)
        self.add_line('foot', (20, 42), (30, 42))
        self.add_line('branch', (30, 42), (42, 8))
        self.add_line('arm', (20, 28), (36, 25))
        self.add_contour('head', *('head-top', 'head-bottom'), closed=True)
        self.add_contour('ear-top', *('ear-top-1', 'ear-top-2'), closed=False)
        self.add_contour('body', *('back', 'bottom', 'foot'), closed=False)
        self.relate('connect', *('ear-top', 'ear-left'))
        self.relate('connect', *('ear-left', 'ear-side'))
        self.relate('connect', *('ear-side', 'ear-bottom'))
        self.relate('connect', *('ear-top', 'head'))
        self.relate('connect', *('ear-bottom', 'head'))
        self.relate('connect', *('body', 'head'))
        self.relate('connect', *('branch', 'body'))
        self.relate('connect', *('arm', 'branch'))
        self.relate('connect', *('arm', 'head'))
