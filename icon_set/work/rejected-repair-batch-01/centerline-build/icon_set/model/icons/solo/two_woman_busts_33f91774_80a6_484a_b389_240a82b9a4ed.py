'Human construction repair. Raise front bust shoulder arch to an exact 4u detached ink gap; preserve the rear continuous neck.\nShared reference: icon_set/references/human_ref/full_body_ref.png; busts use human_ref/user.svg.\nLucide person-standing original and atomic-debug inform shared limb junctions. Preserve intentional action-pose asymmetry.\n'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '33f91774-80a6-484a-b389-240a82b9a4ed'
SOURCE_PATH = 'pictographic-primitives/users/multiple woman 1_33f91774-80a6-484a-b389-240a82b9a4ed.svg'
AUTHOR = 'gpt-6'
HUMAN_CONSTRUCTION = 'group-busts'

class TwoWomanBusts(Solo48):
    icon_id = 'two-woman-busts'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'people/groups'
    aliases = ()
    keywords = ('women', 'busts', 'two', 'users', 'people', 'female', 'pair', 'group')

    # Second spacing pass complete.
    def build(self):
        self.add_arc('front-head-a', (6, 16), (26, 16), radius_x=10, radius_y=10, large_arc=False, sweep=True)
        self.add_arc('front-head-b', (26, 16), (6, 16), radius_x=10, radius_y=10, large_arc=False, sweep=True)
        self.add_line('hair-left', (6, 16), (6, 28))
        self.add_line('hair-right', (26, 16), (26, 28))
        self.add_line('fringe-1', (6, 16), (16, 14))
        self.add_line('fringe-2', (16, 14), (26, 16))
        self.add_arc('front-shoulders', (6, 42), (26, 42), radius_x=10, radius_y=8, large_arc=False, sweep=True)
        self.add_line('front-base', (26, 42), (6, 42))
        self.add_arc('rear-crown', (32, 6), (40, 14), radius_x=8, radius_y=8, large_arc=False, sweep=True)
        self.add_arc('rear-jaw', (40, 14), (36, 22), radius_x=8, radius_y=8, large_arc=False, sweep=True)
        self.add_line('rear-neck', (36, 22), (36, 28))
        self.add_arc('rear-shoulder', (36, 28), (42, 34), radius_x=6, radius_y=6, large_arc=False, sweep=True)
        self.add_line('rear-side', (42, 34), (42, 42))
        self.add_line('rear-base', (42, 42), (36, 42))
        self.add_contour('front-head', *('front-head-a', 'front-head-b'), closed=True)
        self.add_contour('fringe', *('fringe-1', 'fringe-2'), closed=False)
        self.add_contour('front-body', *('front-shoulders', 'front-base'), closed=True)
        self.add_contour('rear', *('rear-crown', 'rear-jaw', 'rear-neck', 'rear-shoulder', 'rear-side', 'rear-base'), closed=False)
        self.relate('connect', *('front-head', 'hair-left'))
        self.relate('connect', *('front-head', 'hair-right'))
        self.relate('connect', *('front-head', 'fringe'))
