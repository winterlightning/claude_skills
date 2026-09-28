"""0 text in circle (state), converted from the icons-json construction graph by json_to_solo --mode fit. CIRCLE keyshape; curves fitted to integer lines and arcs."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'e3714f65-499d-4ba7-9ecb-87ecc26acfff'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__icon-0-text-in-circle/20260927T070849Z-thuan-mac-1/reference/0 text in circle_e3714f65-499d-4ba7-9ecb-87ecc26acfff.svg'
AUTHOR = 'gpt-6'

class Icon0TextInCircle(Solo48):
    icon_id = 'icon-0-text-in-circle'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'state'
    categories = ('state',)
    aliases = ()
    keywords = ('text', 'in', 'circle', 'state')

    def build(self) -> None:
        # Symbol plan: preserve the subject, contour topology and curve types.
        # Rebalance whole parts on the SOLO48 integer grid; keep real shared contacts.
        self.add_arc('sym-e0', (4, 24), (44, 24), radius_x=20, radius_y=20, large_arc=False, sweep=True)
        self.add_arc('sym-e1', (44, 24), (4, 24), radius_x=20, radius_y=20, large_arc=False, sweep=True)
        # The source's zero is a smooth upright oval, not a four-arc wobble.
        self.add_arc('sym-e2', (24, 13), (31, 24), radius_x=7, radius_y=11, sweep=True)
        self.add_arc('sym-e5', (31, 24), (24, 35), radius_x=7, radius_y=11, sweep=True)
        self.add_arc('sym-e6', (24, 35), (17, 24), radius_x=7, radius_y=11, sweep=True)
        self.add_arc('sym-e9', (17, 24), (24, 13), radius_x=7, radius_y=11, sweep=True)
        self.add_contour('sym-c0', *('sym-e0', 'sym-e1'), closed=True)
        self.add_contour('sym-c1', *('sym-e2', 'sym-e5', 'sym-e6', 'sym-e9'), closed=True)
