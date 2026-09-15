'Human construction repair. Set head-outline to shoulder centerline separation to exactly 8u. Keep the extended arm clear of the detached head. Align the upper torso tangent with its own head center.\nShared reference: icon_set/references/human_ref/full_body_ref.png; busts use human_ref/user.svg.\nLucide person-standing original and atomic-debug inform shared limb junctions. Preserve intentional action-pose asymmetry.\n'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'da1dc22a-d712-50d8-b7bf-bb9850b68366'
SOURCE_PATH = 'pictographic-primitives/recreation/sport windsurfing_da1dc22a-d712-50d8-b7bf-bb9850b68366.svg'
AUTHOR = 'gpt-6'
HUMAN_CONSTRUCTION = 'stick-figure'

class CrouchingWindsurferVariant2(Solo48):
    icon_id = 'crouching-windsurfer-v2'
    variant_of = 'crouching-windsurfer'
    variant_label = 'Correct human head and torso construction'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/recreation'
    aliases = ()
    keywords = ('crouching', 'windsurfer')

    def build(self):
        self.add_arc('sail-edge', (25, 6), (8, 30), radius_x=36, radius_y=36, large_arc=False, sweep=False)
        self.add_line('sail-base-1', (8, 30), (20, 30))
        self.add_line('sail-base-2', (20, 30), (21, 25))
        self.add_line('sail-base-3', (21, 25), (25, 6))
        self.add_line('mast', (20, 30), (18, 38))
        self.add_arc('head-top', (34, 17), (40, 17), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('head-bottom', (40, 17), (34, 17), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('person-1', (23, 26), (25, 28))
        self.add_line('person-1-continued', (25, 28), (37, 28))
        self.add_bezier('person-2', (37, 28), *(((37.0, 30.75), (33.25, 33.25), (32, 35)),))
        self.add_line('person-3', (32, 35), (35, 40))
        self.add_line('hand', (23, 26), (21, 25))
        self.add_line('board-1', (6, 36), (18, 38))
        self.add_line('board-2', (18, 38), (35, 40))
        self.add_line('board-3', (35, 40), (42, 42))
        self.add_contour('sail', *('sail-edge', 'sail-base-1', 'sail-base-2', 'sail-base-3'), closed=True)
        self.add_contour('head', *('head-top', 'head-bottom'), closed=True)
        self.add_contour('person', *('person-1', 'person-1-continued', 'person-2', 'person-3'), closed=False)
        self.add_contour('board', *('board-1', 'board-2', 'board-3'), closed=False)
        self.relate('connect', *('sail', 'mast'))
        self.relate('connect', *('person', 'hand'))
        self.relate('connect', *('hand', 'sail'))
        self.relate('connect', *('mast', 'board'))
        self.relate('connect', *('person', 'board'))
        self.mark_human_figure('person-1', head='head', torso='person-2', torso_junction='start')
