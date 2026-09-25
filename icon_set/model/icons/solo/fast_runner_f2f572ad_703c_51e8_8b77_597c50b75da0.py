'Human construction repair. Set head-outline to shoulder centerline separation to exactly 8u. Align the upper torso tangent with its own head center.\nShared reference: icon_set/references/human_ref/full_body_ref.png; busts use human_ref/user.svg.\nLucide person-standing original and atomic-debug inform shared limb junctions. Preserve intentional action-pose asymmetry.\n'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f2f572ad-703c-51e8-8b77-597c50b75da0'
SOURCE_PATH = 'pictographic-primitives/sports/jogging fast running_f2f572ad-703c-51e8-8b77-597c50b75da0.svg'
AUTHOR = 'gpt-6'
HUMAN_CONSTRUCTION = 'stick-figure'

class FastRunner(Solo48):
    icon_id = 'fast-runner'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'sports'
    aliases = ()
    keywords = ('running', 'sprint', 'runner', 'speed', 'athlete', 'fitness')

    # Second spacing pass complete.
    def build(self):
        self.add_arc('head-top', (13, 9), (19, 9), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('head-bottom', (19, 9), (13, 9), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_bezier('body-0', (16, 20), *(((16.0, 22.75), (20.5, 27.5), (22, 30)),))
        self.add_line('left-arm-0', (16, 20), (12, 25))
        self.add_line('left-arm-1', (12, 25), (6, 20))
        self.add_line('right-arm-0', (16, 20), (26, 21))
        self.add_line('right-arm-1', (26, 21), (29, 24))
        self.add_line('bent-leg-0', (22, 30), (12, 34))
        self.add_line('bent-leg-1', (12, 34), (14, 42))
        self.add_line('rear-leg-0', (22, 30), (32, 42))
        self.add_line('motion-0', (38, 12), (42, 12))
        self.add_line('motion-1', (38, 22), (42, 22))
        self.add_line('motion-2', (38, 32), (42, 32))
        self.add_contour('head', *('head-top', 'head-bottom'), closed=True)
        self.add_contour('left-arm', *('left-arm-0', 'left-arm-1'), closed=False)
        self.add_contour('right-arm', *('right-arm-0', 'right-arm-1'), closed=False)
        self.add_contour('bent-leg', *('bent-leg-0', 'bent-leg-1'), closed=False)
        self.relate('connect', *('body-0', 'left-arm-0'))
        self.relate('connect', *('body-0', 'right-arm-0'))
        self.relate('connect', *('body-0', 'bent-leg-0'))
        self.relate('connect', *('body-0', 'rear-leg-0'))
        self.relate('connect', *('left-arm-0', 'left-arm-1'))
        self.relate('connect', *('left-arm-0', 'right-arm-0'))
        self.relate('connect', *('right-arm-0', 'right-arm-1'))
        self.relate('connect', *('bent-leg-0', 'bent-leg-1'))
        self.relate('connect', *('bent-leg-0', 'rear-leg-0'))
        self.mark_human_figure('person-1', head='head', torso='body-0', torso_junction='start')
