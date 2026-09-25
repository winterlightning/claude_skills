'Human construction repair. Separate the director torso from the leg at the hip without moving ink.\nShared reference: icon_set/references/human_ref/full_body_ref.png; busts use human_ref/user.svg.\nLucide person-standing original and atomic-debug inform shared limb junctions. Preserve intentional action-pose asymmetry.\n'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '18bef7d9-966c-46ce-9638-fea7a1c81585'
SOURCE_PATH = 'pictographic-primitives/work/worker lay off fired user finger box_18bef7d9-966c-46ce-9638-fea7a1c81585.svg'
AUTHOR = 'gpt-6'
HUMAN_CONSTRUCTION = 'mixed-segmented-body'

class PersonDirectingBoxCarrier(Solo48):
    icon_id = 'person-directing-box-carrier'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'work'
    categories = ('work', 'primitives')
    aliases = ()
    keywords = ('person', 'box', 'worker', 'leaving', 'dismissal', 'carrying')

    # Second spacing pass complete.
    def build(self):
        self.add_arc('carrier-head-a', (16, 10), (24, 10), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('carrier-head-b', (24, 10), (16, 10), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('director-head-a', (32, 10), (40, 10), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('director-head-b', (40, 10), (32, 10), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('box-1', (6, 26), (14, 26))
        self.add_line('box-2', (14, 26), (14, 34))
        self.add_line('box-3', (14, 34), (6, 34))
        self.add_line('box-4', (6, 34), (6, 26))
        self.add_bezier('carrier-1', (20, 22), *(((20, 26), (27, 29), (28, 32)),))
        self.add_line('carrier-2', (28, 32), (18, 42))
        self.add_line('back-leg', (28, 32), (28, 42))
        self.add_line('carrying-arm', (20, 22), (14, 34))
        self.add_line('director-1', (36, 22), (36, 32))
        self.add_line('director-leg', (36, 32), (36, 42))
        self.add_line('director-2', (36, 42), (42, 42))
        self.add_line('pointing-arm', (36, 22), (20, 22))
        self.add_contour('carrier-head', *('carrier-head-a', 'carrier-head-b'), closed=True)
        self.add_contour('director-head', *('director-head-a', 'director-head-b'), closed=True)
        self.add_contour('box', *('box-1', 'box-2', 'box-3', 'box-4'), closed=True)
        self.add_contour('carrier', *('carrier-1', 'carrier-2'), closed=False)
        self.add_contour('director', *('director-1', 'director-leg', 'director-2'), closed=False)
        self.relate('connect', *('back-leg', 'carrier'))
        self.relate('connect', *('carrying-arm', 'carrier'))
        self.relate('connect', *('carrying-arm', 'box'))
        self.relate('connect', *('pointing-arm', 'director'))
        self.relate('connect', *('pointing-arm', 'carrier'))
        self.relate('connect', *('pointing-arm', 'carrying-arm'))
        self.mark_human_figure('person-1', head='carrier-head', torso='carrier-1', torso_junction='start')
        self.mark_human_figure('person-2', head='director-head', torso='director-1', torso_junction='start')
