'Human construction repair. Reposition head over the anatomical shoulder. Set head-outline to shoulder centerline separation to exactly 8u. Simplify to one visible balancing arm; omit the far raised arm that crowds the head and bent leg. Align the upper torso tangent with its own head center.\nShared reference: icon_set/references/human_ref/full_body_ref.png; busts use human_ref/user.svg.\nLucide person-standing original and atomic-debug inform shared limb junctions. Preserve intentional action-pose asymmetry.\n'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '31dfc8f9-9e71-491e-9f9a-e8bd904e4344'
SOURCE_PATH = 'pictographic-primitives/sports/skating_31dfc8f9-9e71-491e-9f9a-e8bd904e4344.svg'
AUTHOR = 'gpt-6'
HUMAN_CONSTRUCTION = 'stick-figure'

class BoardRiderOverWaves(Solo48):
    icon_id = 'board-rider-over-waves'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/sports'
    aliases = ()
    keywords = ('board', 'rider', 'wave', 'water', 'balance', 'sport')

    def build(self):
        self.add_arc('head-a', (20, 6), (20, 12), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('head-b', (20, 12), (20, 6), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('arms-1', (6, 22), (20, 20))
        self.add_line('torso', (20, 20), (20, 24))
        self.add_line('leg-1', (20, 24), (32, 24))
        self.add_line('leg-2', (32, 24), (35, 32))
        self.add_line('board-1', (12, 33), (17, 32))
        self.add_line('board-2', (17, 32), (35, 32))
        self.add_line('board-3', (35, 32), (42, 24))
        self.add_line('standing-leg', (20, 24), (17, 32))
        self.add_arc('wave-left', (6, 42), (24, 42), radius_x=9, radius_y=1, large_arc=False, sweep=True)
        self.add_arc('wave-right', (24, 42), (42, 42), radius_x=9, radius_y=1, large_arc=False, sweep=True)
        self.add_contour('head', *('head-a', 'head-b'), closed=True)
        self.add_contour('arms', *('arms-1',), closed=False)
        self.add_contour('leg', *('leg-1', 'leg-2'), closed=False)
        self.add_contour('board', *('board-1', 'board-2', 'board-3'), closed=False)
        self.add_contour('water', *('wave-left', 'wave-right'), closed=False)
        self.relate('connect', *('arms', 'torso'))
        self.relate('connect', *('torso', 'leg'))
        self.relate('connect', *('standing-leg', 'torso'))
        self.relate('connect', *('standing-leg', 'leg'))
        self.relate('connect', *('standing-leg', 'board'))
        self.relate('connect', *('board', 'leg'))
        self.mark_human_figure('person-1', head='head', torso='torso', torso_junction='start')
