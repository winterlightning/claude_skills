'Human construction repair. Bring the top of the outlined body under the head with exact 4u ink clearance.\nShared reference: icon_set/references/human_ref/full_body_ref.png; busts use human_ref/user.svg.\nLucide person-standing original and atomic-debug inform shared limb junctions. Preserve intentional action-pose asymmetry.\n'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1f4f73c6-0617-4a56-8e0e-463dcef59a3a'
SOURCE_PATH = 'pictographic-primitives/recreation/sport jet skiing_1f4f73c6-0617-4a56-8e0e-463dcef59a3a.svg'
AUTHOR = 'gpt-6'
HUMAN_CONSTRUCTION = 'outlined-body'

class JetSkiRiderJumpingAWave(Solo48):
    icon_id = 'jet-ski-rider-jumping-a-wave'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/recreation'
    aliases = ()
    keywords = ('jet', 'ski', 'rider', 'jumping', 'a', 'wave')

    def build(self):
        self.add_arc('head-top', (17, 8), (21, 8), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_arc('head-bottom', (21, 8), (17, 8), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_line('rider-2', (19, 28), (19, 18))
        self.add_line('rider-3', (19, 18), (34, 22))
        self.add_line('rider-4', (34, 22), (36, 32))
        self.add_line('craft-1', (6, 30), (6, 25))
        self.add_line('craft-2', (6, 25), (13, 25))
        self.add_line('craft-3', (13,25),(19,28))
        self.add_line('craft-seat',(19,28),(21,29))
        self.add_line('craft-4', (21, 29), (34, 32))
        self.add_line('craft-5', (34, 32), (36, 32))
        self.add_line('craft-6', (36, 32), (42, 32))
        self.add_arc('wave', (6, 42), (18, 42), radius_x=6, radius_y=3, large_arc=False, sweep=True)
        self.add_line('water', (18, 42), (42, 42))
        self.add_contour('head', *('head-top', 'head-bottom'), closed=True)
        self.add_contour('rider', *('rider-2', 'rider-3', 'rider-4'), closed=False)
        self.add_contour('craft', *('craft-1', 'craft-2', 'craft-3', 'craft-seat', 'craft-4', 'craft-5', 'craft-6'), closed=False)
        self.relate('connect', *('craft', 'rider'))
        self.relate('connect', *('wave', 'water'))
        self.mark_human_figure('person',head='head',torso='rider-2',torso_junction='end')
