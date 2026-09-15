'Human construction repair. Raise gown neckline to exactly 4u ink clearance below the head.\nShared reference: icon_set/references/human_ref/full_body_ref.png; busts use human_ref/user.svg.\nLucide person-standing original and atomic-debug inform shared limb junctions. Preserve intentional action-pose asymmetry.\n'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '339413a2-9f25-4881-9b93-a087f3da321c'
SOURCE_PATH = 'pictographic-primitives/religion/zeus_339413a2-9f25-4881-9b93-a087f3da321c.svg'
AUTHOR = 'gpt-6'
HUMAN_CONSTRUCTION = 'outlined-body'

class ZeusWithLightningBoltVariant2(Solo48):
    icon_id = 'zeus-with-lightning-bolt-v2'
    variant_of = 'zeus-with-lightning-bolt'
    variant_label = 'Correct human head and torso construction'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'culture/religion'
    aliases = ()
    keywords = ('zeus', 'lightning', 'bolt', 'greek', 'god', 'mythology', 'figure')

    def build(self):
        self.add_arc('head-top', (9, 10), (21, 10), radius_x=6, radius_y=6, large_arc=False, sweep=True)
        self.add_arc('head-bottom', (21, 10), (9, 10), radius_x=6, radius_y=6, large_arc=False, sweep=True)
        self.add_line('hair', (9, 10), (8, 17))
        self.add_line('gown-1', (13, 24), (8, 44))
        self.add_line('gown-2', (8, 44), (27, 44))
        self.add_line('gown-3', (27, 44), (25, 34))
        self.add_line('gown-4', (25, 34), (23, 24))
        self.add_line('gown-5', (23, 24), (13, 24))
        self.add_line('arm-1', (25, 34), (31, 34))
        self.add_line('arm-2', (31, 34), (31, 28))
        self.add_line('bolt-1', (40, 4), (28, 18))
        self.add_line('bolt-2', (28, 18), (39, 18))
        self.add_line('bolt-3', (39, 18), (31, 28))
        self.add_contour('head', *('head-top', 'head-bottom'), closed=True)
        self.add_contour('gown', *('gown-1', 'gown-2', 'gown-3', 'gown-4', 'gown-5'), closed=False)
        self.add_contour('arm', *('arm-1', 'arm-2'), closed=False)
        self.add_contour('bolt', *('bolt-1', 'bolt-2', 'bolt-3'), closed=False)
        self.relate('connect', *('head', 'hair'))
        self.relate('connect', *('arm', 'gown'))
        self.relate('connect', *('bolt', 'arm'))
