'Human construction repair. Set head-outline to shoulder centerline separation to exactly 8u. Align the upper torso tangent with its own head center.\nShared reference: icon_set/references/human_ref/full_body_ref.png; busts use human_ref/user.svg.\nLucide person-standing original and atomic-debug inform shared limb junctions. Preserve intentional action-pose asymmetry.\n'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ad6a0427-9dcf-56bc-a271-c70f6694c4d6'
SOURCE_PATH = 'pictographic-primitives/sports/shooting rifle person aim_ad6a0427-9dcf-56bc-a271-c70f6694c4d6.svg'
AUTHOR = 'gpt-6'
HUMAN_CONSTRUCTION = 'stick-figure'

class AimingRifleShooterVariant2(Solo48):
    icon_id = 'aiming-rifle-shooter-v2'
    variant_of = 'aiming-rifle-shooter'
    variant_label = 'Correct human head and torso construction'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/sports'
    aliases = ()
    keywords = ('shooting', 'rifle', 'shooter', 'aim', 'target', 'sport')

    def build(self):
        self.add_arc('head-a', (12, 6), (12, 12), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('head-b', (12, 12), (12, 6), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('torso', (12, 20), (12, 30))
        self.add_line('legs-1', (6, 42), (12, 30))
        self.add_line('legs-2', (12, 30), (22, 42))
        self.add_line('rifle-1', (12, 20), (33, 21))
        self.add_line('rifle-2', (33, 21), (42, 21))
        self.add_line('arms-1', (12, 20), (24, 31))
        self.add_line('arms-2', (24, 31), (33, 21))
        self.add_contour('head', *('head-a', 'head-b'), closed=True)
        self.add_contour('legs', *('legs-1', 'legs-2'), closed=False)
        self.add_contour('rifle', *('rifle-1', 'rifle-2'), closed=False)
        self.add_contour('arms', *('arms-1', 'arms-2'), closed=False)
        self.relate('connect', *('torso', 'legs'))
        self.relate('connect', *('rifle', 'torso'))
        self.relate('connect', *('arms', 'rifle'))
        self.relate('connect', *('arms', 'torso'))
        self.mark_human_figure('person-1', head='head', torso='torso', torso_junction='start')
