"""A broad tapered obelisk on a flat plinth, with a cloud at upper right."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '58e11e3e-2b0c-402a-935d-87f070933827'
SOURCE_PATH = 'pictographic-primitives/landmarks/batch-02/tower_58e11e3e-2b0c-402a-935d-87f070933827.svg'
AUTHOR = 'gpt-6'


class ObeliskOnPlinth(Solo48):
    icon_id = 'obelisk-on-plinth'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "landmarks"
    aliases = ()
    keywords = ('obelisk', 'monument', 'memorial', 'tower', 'landmark', 'cloud', 'plinth', 'pillar')

    def build(self) -> None:
        # Symbol plan: preserve the subject, contour topology and curve types.
        # Rebalance whole parts on the SOLO48 integer grid; keep real shared contacts.
        self.add_line('obelisk-1', (11, 42), (14, 8))
        self.add_line('obelisk-2', (14, 8), (17, 6))
        self.add_line('obelisk-3', (17, 6), (18, 6))
        self.add_line('obelisk-4', (18, 6), (22, 8))
        self.add_line('obelisk-5', (22, 8), (25, 42))
        self.add_line('plinth-1', (6, 42), (11, 42))
        self.add_line('plinth-2', (11, 42), (25, 42))
        self.add_line('plinth-3', (25, 42), (42, 42))
        self.add_arc('cloud-top', (32, 11), (41, 11), radius_x=7, radius_y=7, large_arc=False, sweep=True)
        self.add_arc('cloud-right', (41, 11), (39, 16), radius_x=6, radius_y=6, large_arc=False, sweep=True)
        self.add_line('cloud-base', (39, 16), (32, 16))
        self.add_arc('cloud-left', (32, 16), (32, 11), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_contour('obelisk', *('obelisk-1', 'obelisk-2', 'obelisk-3', 'obelisk-4', 'obelisk-5'), closed=False)
        self.add_contour('plinth', *('plinth-1', 'plinth-2', 'plinth-3'), closed=False)
        self.add_contour('cloud', *('cloud-top', 'cloud-right', 'cloud-base', 'cloud-left'), closed=True)
        self.relate('connect', *('plinth', 'obelisk'))
