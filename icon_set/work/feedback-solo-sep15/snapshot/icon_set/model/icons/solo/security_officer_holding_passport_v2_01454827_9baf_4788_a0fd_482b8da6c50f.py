'Human construction repair. Replace pinched collar with smooth rounded shoulders touching the circular face ink; retain cap, raised arm and passport.\nShared reference: icon_set/references/human_ref/full_body_ref.png; busts use human_ref/user.svg.\nLucide person-standing original and atomic-debug inform shared limb junctions. Preserve intentional action-pose asymmetry.\n'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '01454827-9baf-4788-a0fd-482b8da6c50f'
SOURCE_PATH = 'pictographic-primitives/travel/security officer passport_01454827-9baf-4788-a0fd-482b8da6c50f.svg'
AUTHOR = 'gpt-6'
HUMAN_CONSTRUCTION = 'bust'

class SecurityOfficerHoldingPassportVariant2(Solo48):
    icon_id = 'security-officer-holding-passport-v2'
    variant_of = 'security-officer-holding-passport'
    variant_label = 'Correct human head and torso construction'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/travel'
    aliases = ()
    keywords = ('security', 'officer', 'passport', 'document', 'checkpoint', 'immigration', 'guard', 'airport')

    # Second spacing pass complete.
    def build(self):
        self.add_line('cap-1', (28, 6), (42, 7))
        self.add_line('cap-2', (42, 7), (40, 16))
        self.add_line('cap-3', (40, 16), (28, 16))
        self.add_line('cap-4', (28, 16), (28, 6))
        self.add_arc('face', (40, 16), (28, 16), radius_x=6, radius_y=6, large_arc=False, sweep=True)
        self.add_line('booklet-1', (6, 8), (18, 10))
        self.add_line('booklet-2', (18, 10), (18, 26))
        self.add_line('booklet-3', (18, 26), (12, 25))
        self.add_line('booklet-4', (12, 25), (6, 24))
        self.add_line('booklet-5', (6, 24), (6, 8))
        self.add_line('raised-arm-1', (12, 25), (10, 36))
        self.add_line('raised-arm-2', (10, 36), (20, 38))
        self.add_line('raised-arm-3', (20, 38), (26, 34))
        self.add_line('torso-left', (26, 42), (26, 34))
        self.add_arc('shoulder-left', (26, 34), (34, 26), radius_x=8, radius_y=8, large_arc=False, sweep=True)
        self.add_arc('shoulder-right', (34, 26), (42, 34), radius_x=8, radius_y=8, large_arc=False, sweep=True)
        self.add_line('torso-right', (42, 34), (42, 42))
        self.add_line('torso-base', (42, 42), (26, 42))
        self.add_contour('cap', *('cap-1', 'cap-2', 'cap-3', 'cap-4'), closed=True)
        self.add_contour('booklet', *('booklet-1', 'booklet-2', 'booklet-3', 'booklet-4', 'booklet-5'), closed=True)
        self.add_contour('raised-arm', *('raised-arm-1', 'raised-arm-2', 'raised-arm-3'), closed=False)
        self.add_contour('torso', *('torso-left', 'shoulder-left', 'shoulder-right', 'torso-right', 'torso-base'), closed=True)
        self.relate('connect', *('cap', 'face'))
        self.relate('connect', *('booklet', 'raised-arm'))
        self.relate('connect', *('torso', 'raised-arm'))
        self.relate('connect', *('face', 'torso'))
