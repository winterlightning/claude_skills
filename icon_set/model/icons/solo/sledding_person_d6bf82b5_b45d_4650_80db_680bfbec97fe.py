'Human construction repair. Set head-outline to shoulder centerline separation to exactly 8u. Rebalance raised hand to keep it clear of the head. Align the upper torso tangent with its own head center.\nShared reference: icon_set/references/human_ref/full_body_ref.png; busts use human_ref/user.svg.\nLucide person-standing original and atomic-debug inform shared limb junctions. Preserve intentional action-pose asymmetry.\n'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd6bf82b5-b45d-4650-80db-680bfbec97fe'
SOURCE_PATH = 'pictographic-primitives/symbol/snow slide_d6bf82b5-b45d-4650-80db-680bfbec97fe.svg'
AUTHOR = 'gpt-6'
HUMAN_CONSTRUCTION = 'stick-figure'

class SleddingPerson(Solo48):
    icon_id = 'sledding-person'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/symbols'
    aliases = ()
    keywords = ('sledding', 'toboggan', 'luge', 'winter', 'snow', 'slide', 'sport', 'sled')

    # Second spacing pass complete.
    def build(self):
        self.add_arc('head-top', (32, 18), (42, 18), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_arc('head-bottom', (42, 18), (32, 18), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_line('body-1', (9, 6), (12, 16))
        self.add_bezier('body-2', (12, 16), *(((14.5, 17.75), (22.0, 24.25), (25, 23)),))
        self.add_line('arm', (18, 7), (25, 23))
        self.add_line('sled-run', (6, 26), (28, 40))
        self.add_arc('sled-curve', (28, 40), (42, 40), radius_x=7, radius_y=2, large_arc=False, sweep=False)
        self.add_contour('head', *('head-top', 'head-bottom'), closed=True)
        self.add_contour('body', *('body-1', 'body-2'), closed=False)
        self.add_contour('sled', *('sled-run', 'sled-curve'), closed=False)
        self.relate('connect', *('body', 'arm'))
        self.mark_human_figure('person-1', head='head', torso='body-2', torso_junction='end')
