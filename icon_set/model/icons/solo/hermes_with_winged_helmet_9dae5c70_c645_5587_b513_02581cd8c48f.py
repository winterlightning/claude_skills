'Human construction repair. Use a circular face and raise the shoulder arch to tangent ink contact for a bust (0u visible gap).\nShared reference: icon_set/references/human_ref/full_body_ref.png; busts use human_ref/user.svg.\nLucide person-standing original and atomic-debug inform shared limb junctions. Preserve intentional action-pose asymmetry.\n'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9dae5c70-c645-5587-b513-02581cd8c48f'
SOURCE_PATH = 'pictographic-primitives/religion/hermes_9dae5c70-c645-5587-b513-02581cd8c48f.svg'
AUTHOR = 'gpt-6'
HUMAN_CONSTRUCTION = 'bust'

class HermesWithWingedHelmet(Solo48):
    icon_id = 'hermes-with-winged-helmet'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'religion'
    aliases = ()
    keywords = ('hermes', 'helmet', 'wing', 'head', 'greek', 'mythology', 'portrait')

    human_construction = 'bust'

    # Second spacing pass complete.
    def build(self):
        self.add_arc('helmet', (14, 19), (34, 19), radius_x=10, radius_y=11, large_arc=False, sweep=True)
        self.add_line('band', (14, 19), (34, 19))
        self.add_arc('face', (34, 19), (14, 19), radius_x=10, radius_y=10, large_arc=False, sweep=True)
        self.add_line('wing-left-1', (14, 19), (7, 18))
        self.add_line('wing-left-2', (7, 18), (4, 9))
        self.add_line('wing-left-3', (4, 9), (14, 10))
        self.add_line('wing-right-1', (34, 19), (41, 18))
        self.add_line('wing-right-2', (41, 18), (44, 9))
        self.add_line('wing-right-3', (44, 9), (34, 10))
        self.add_arc('shoulders', (8, 40), (40, 40), radius_x=16, radius_y=7, large_arc=False, sweep=True)
        self.add_contour('wing-left', *('wing-left-1', 'wing-left-2', 'wing-left-3'), closed=False)
        self.add_contour('wing-right', *('wing-right-1', 'wing-right-2', 'wing-right-3'), closed=False)
        self.relate('connect', *('helmet', 'band'))
        self.relate('connect', *('face', 'helmet'))
        self.relate('connect', *('face', 'band'))
        self.relate('connect', *('wing-left', 'helmet'))
        self.relate('connect', *('wing-left', 'band'))
        self.relate('connect', *('wing-left', 'face'))
        self.relate('connect', *('wing-right', 'helmet'))
        self.relate('connect', *('wing-right', 'band'))
        self.relate('connect', *('wing-right', 'face'))
        self.relate('connect', *('face', 'shoulders'))
