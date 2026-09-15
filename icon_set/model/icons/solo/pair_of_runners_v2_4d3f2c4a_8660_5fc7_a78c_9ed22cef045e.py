'Human construction repair. Align the upper torso tangent with its own head center.\nShared reference: icon_set/references/human_ref/full_body_ref.png; busts use human_ref/user.svg.\nLucide person-standing original and atomic-debug inform shared limb junctions. Preserve intentional action-pose asymmetry.\n'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4d3f2c4a-8660-5fc7-a78c-9ed22cef045e'
SOURCE_PATH = 'pictographic-primitives/sports/group running_4d3f2c4a-8660-5fc7-a78c-9ed22cef045e.svg'
AUTHOR = 'gpt-6'
HUMAN_CONSTRUCTION = 'stick-figure'

class PairOfRunnersVariant2(Solo48):
    icon_id = 'pair-of-runners-v2'
    variant_of = 'pair-of-runners'
    variant_label = 'Correct human head and torso construction'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/sports'
    aliases = ()
    keywords = ('running', 'runner', 'pair', 'group', 'athlete', 'fitness')

    # Second spacing pass complete.
    def build(self):
        self.add_arc('left-head-a', (10, 10), (18, 10), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('left-head-b', (18, 10), (10, 10), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('right-head-a', (30, 10), (38, 10), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('right-head-b', (38, 10), (30, 10), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_bezier('left-body-0', (14, 22), *(((14.0, 25.8), (14.0, 28.25), (14, 30)),))
        self.add_line('left-back-arm-0', (14, 22), (6, 22))
        self.add_line('left-back-arm-1', (6, 22), (6, 28))
        self.add_line('left-front-arm-0', (14, 22), (18, 24))
        self.add_line('left-back-leg-0', (14, 30), (6, 40))
        self.add_line('left-front-leg-0', (14, 30), (20, 34))
        self.add_line('left-front-leg-1', (20, 34), (20, 42))
        self.add_bezier('right-body-0', (34, 22), *(((34.0, 25.0), (32.5, 28.0), (32, 30)),))
        self.add_line('right-front-arm-0', (34, 22), (42, 22))
        self.add_line('right-back-arm-0', (34, 22), (26, 22))
        self.add_line('right-back-arm-1', (26, 22), (26, 24))
        self.add_line('right-back-leg-0', (32, 30), (30, 42))
        self.add_line('right-front-leg-0', (32, 30), (40, 36))
        self.add_line('right-front-leg-1', (40, 36), (42, 42))
        self.add_contour('left-head', *('left-head-a', 'left-head-b'), closed=True)
        self.add_contour('right-head', *('right-head-a', 'right-head-b'), closed=True)
        self.add_contour('left-back-arm', *('left-back-arm-0', 'left-back-arm-1'), closed=False)
        self.add_contour('left-front-leg', *('left-front-leg-0', 'left-front-leg-1'), closed=False)
        self.add_contour('right-back-arm', *('right-back-arm-0', 'right-back-arm-1'), closed=False)
        self.add_contour('right-front-leg', *('right-front-leg-0', 'right-front-leg-1'), closed=False)
        self.relate('connect', *('left-body-0', 'left-back-arm-0'))
        self.relate('connect', *('left-body-0', 'left-front-arm-0'))
        self.relate('connect', *('left-body-0', 'left-back-leg-0'))
        self.relate('connect', *('left-body-0', 'left-front-leg-0'))
        self.relate('connect', *('left-back-arm-0', 'left-back-arm-1'))
        self.relate('connect', *('left-back-arm-0', 'left-front-arm-0'))
        self.relate('connect', *('left-back-leg-0', 'left-front-leg-0'))
        self.relate('connect', *('left-front-leg-0', 'left-front-leg-1'))
        self.relate('connect', *('right-body-0', 'right-front-arm-0'))
        self.relate('connect', *('right-body-0', 'right-back-arm-0'))
        self.relate('connect', *('right-body-0', 'right-back-leg-0'))
        self.relate('connect', *('right-body-0', 'right-front-leg-0'))
        self.relate('connect', *('right-front-arm-0', 'right-back-arm-0'))
        self.relate('connect', *('right-back-arm-0', 'right-back-arm-1'))
        self.relate('connect', *('right-back-leg-0', 'right-front-leg-0'))
        self.relate('connect', *('right-front-leg-0', 'right-front-leg-1'))
        self.mark_human_figure('person-1', head='left-head', torso='left-body-0', torso_junction='start')
        self.mark_human_figure('person-2', head='right-head', torso='right-body-0', torso_junction='start')
