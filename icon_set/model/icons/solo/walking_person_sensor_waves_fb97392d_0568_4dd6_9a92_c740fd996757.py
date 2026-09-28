'Human construction repair. Set head-outline to shoulder centerline separation to exactly 8u. Align the upper torso tangent with its own head center.\nShared reference: icon_set/references/human_ref/full_body_ref.png; busts use human_ref/user.svg.\nLucide person-standing original and atomic-debug inform shared limb junctions. Preserve intentional action-pose asymmetry.\n'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'fb97392d-0568-4dd6-9a92-c740fd996757'
SOURCE_PATH = 'pictographic-primitives/technology/motion sensor pir_fb97392d-0568-4dd6-9a92-c740fd996757.svg'
AUTHOR = 'gpt-6'
HUMAN_CONSTRUCTION = 'stick-figure'

class WalkingPersonSensorWaves(Solo48):
    icon_id = 'walking-person-sensor-waves'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'technology'
    categories = ('primitives', 'technology')
    aliases = ()
    keywords = ('motion-sensor', 'pir', 'walking', 'person', 'detection', 'waves', 'presence')

    def build(self):
        self.add_arc('heada', (24, 6), (24, 12), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('headb', (24, 12), (24, 6), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_bezier('body-1', (24, 20), *(((24.0, 22.75), (22.5, 27.5), (22, 30)),))
        self.add_line('body-2', (22, 30), (17, 42))
        self.add_line('leg', (22, 30), (30, 42))
        self.add_line('arms-1', (17, 28), (24, 20))
        self.add_line('arms-2', (24, 20), (31, 28))
        self.add_arc('left-top', (8, 14), (6, 24), radius_x=2, radius_y=10, large_arc=False, sweep=False)
        self.add_arc('left-bottom', (6, 24), (8, 34), radius_x=2, radius_y=10, large_arc=False, sweep=False)
        self.add_arc('right-top', (40, 14), (42, 24), radius_x=2, radius_y=10, large_arc=False, sweep=True)
        self.add_arc('right-bottom', (42, 24), (40, 34), radius_x=2, radius_y=10, large_arc=False, sweep=True)
        self.add_contour('head', *('heada', 'headb'), closed=True)
        self.add_contour('body', *('body-1', 'body-2'), closed=False)
        self.add_contour('arms', *('arms-1', 'arms-2'), closed=False)
        self.add_contour('left-wave', *('left-top', 'left-bottom'), closed=False)
        self.add_contour('right-wave', *('right-top', 'right-bottom'), closed=False)
        self.relate('connect', *('leg', 'body'))
        self.relate('connect', *('arms', 'body'))
        self.mark_human_figure('person-1', head='head', torso='body-1', torso_junction='start')
