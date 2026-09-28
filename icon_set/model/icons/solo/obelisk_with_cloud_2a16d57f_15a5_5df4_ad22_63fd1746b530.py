"""A tapered obelisk with a pointed cap, baseline and detached cloud."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2a16d57f-15a5-5df4-ad22-63fd1746b530'
SOURCE_PATH = 'pictographic-primitives/landmarks/batch-02/tower_2a16d57f-15a5-5df4-ad22-63fd1746b530.svg'
AUTHOR = 'gpt-6'


class ObeliskWithCloud(Solo48):
    icon_id = 'obelisk-with-cloud'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "landmarks"
    categories = ("landmarks", "primitives")
    aliases = ()
    keywords = ('obelisk', 'monument', 'memorial', 'tower', 'landmark', 'cloud', 'washington', 'pillar')

    def build(self) -> None:
        # Symbol plan: preserve the subject, contour topology and curve types.
        # Rebalance whole parts on the SOLO48 integer grid; keep real shared contacts.
        self.add_line('obelisk-1', (11, 42), (14, 9))
        self.add_line('obelisk-2', (14, 9), (18, 6))
        self.add_line('obelisk-3', (18, 6), (22, 9))
        self.add_line('obelisk-4', (22, 9), (25, 42))
        self.add_line('ground-1', (6, 42), (11, 42))
        self.add_line('ground-2', (11, 42), (25, 42))
        self.add_line('ground-3', (25, 42), (42, 42))
        self.add_arc('cloud-top', (32, 11), (41, 11), radius_x=7, radius_y=7, large_arc=False, sweep=True)
        self.add_arc('cloud-right', (41, 11), (39, 16), radius_x=6, radius_y=6, large_arc=False, sweep=True)
        self.add_line('cloud-base', (39, 16), (32, 16))
        self.add_arc('cloud-left', (32, 16), (32, 11), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_contour('obelisk', *('obelisk-1', 'obelisk-2', 'obelisk-3', 'obelisk-4'), closed=False)
        self.add_contour('ground', *('ground-1', 'ground-2', 'ground-3'), closed=False)
        self.add_contour('cloud', *('cloud-top', 'cloud-right', 'cloud-base', 'cloud-left'), closed=True)
        self.relate('connect', *('ground', 'obelisk'))
