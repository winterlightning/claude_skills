from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ced624e7-6780-47bf-96e5-579058e49c81'
SOURCE_PATH = 'pictographic-primitives/animals/sloth on tree_ced624e7-6780-47bf-96e5-579058e49c81.svg'
AUTHOR = 'gpt-6'


class SlothOnBranch(Solo48):
    icon_id = 'sloth-on-branch'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "nature/animals"
    aliases = ()
    keywords = ('sloth', 'branch', 'hanging', 'tree', 'slow', 'animal', 'rainforest', 'wildlife')

    def build(self) -> None:
        # Rightward draped body and pendant limb; extremes (2,8)-(46,40).
        self.add_arc('head0', (2, 18), (12, 8), radius_x=10, radius_y=10, sweep=True)
        self.add_arc('head1', (12, 8), (22, 18), radius_x=10, radius_y=10, sweep=True)
        self.add_arc('head2', (22, 18), (12, 28), radius_x=10, radius_y=10, sweep=True)
        self.add_arc('head3', (12, 28), (2, 18), radius_x=10, radius_y=10, sweep=True)
        self.add_contour('head', 'head0', 'head1', 'head2', 'head3', closed=True)
        self.add_dot('eye-l', (9, 18))
        self.add_dot('eye-r', (15, 18))
        self.add_line('back-start', (12, 8), (27, 8))
        self.add_arc('back', (27, 8), (42, 23), radius_x=15, radius_y=15, sweep=True)
        self.add_line('rump-1', (42, 23), (46, 31))
        self.add_line('rump-2', (46, 31), (39, 31))
        self.add_arc('rear-paw', (39, 31), (33, 25), radius_x=6, radius_y=6, sweep=True)
        self.add_line('rear-arm', (33, 25), (33, 21))
        self.add_contour('body', 'back-start', 'back', 'rump-1', 'rump-2', 'rear-paw', 'rear-arm', closed=False)
        self.add_line('front-arm', (22, 18), (22, 36))
        self.add_arc('front-paw', (22, 36), (30, 36), radius_x=4, radius_y=4, sweep=False)
        self.add_line('front-rise', (30, 36), (30, 29))
        self.add_contour('arm', 'front-arm', 'front-paw', 'front-rise', closed=False)
        self.add_line('branch-left', (2, 28), (12, 28))
        self.add_line('branch-right', (39, 31), (46, 31))
        self.relate("connect", 'head', 'body')
        self.relate("connect", 'head', 'arm')
        self.relate("connect", 'head', 'branch-left')
        self.relate("connect", 'body', 'branch-right')
