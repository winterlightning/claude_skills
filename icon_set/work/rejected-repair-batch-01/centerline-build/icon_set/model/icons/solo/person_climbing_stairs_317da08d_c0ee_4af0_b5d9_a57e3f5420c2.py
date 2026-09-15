'Human construction repair. Align the upper torso tangent with its own head center.\nShared reference: icon_set/references/human_ref/full_body_ref.png; busts use human_ref/user.svg.\nLucide person-standing original and atomic-debug inform shared limb junctions. Preserve intentional action-pose asymmetry.\n'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '317da08d-c0ee-4af0-b5d9-a57e3f5420c2'
SOURCE_PATH = 'pictographic-primitives/wayfinding/stairs person ascend_317da08d-c0ee-4af0-b5d9-a57e3f5420c2.svg'
AUTHOR = 'gpt-6'
HUMAN_CONSTRUCTION = 'stick-figure'

class PersonClimbingStairs(Solo48):
    icon_id = 'person-climbing-stairs'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/wayfinding'
    aliases = ()
    keywords = ('person', 'stairs', 'ascending', 'climbing', 'steps', 'wayfinding')

    # Second spacing pass complete.
    def build(self):
        self.add_arc('person-head-a', (14, 10), (22, 10), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('person-head-b', (22, 10), (14, 10), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_bezier('person-body-1', (18, 22), *(((18.0, 25.0), (16.5, 28.5), (16, 30)),))
        self.add_line('person-arms-1', (6, 22), (18, 22))
        self.add_line('person-legs-1', (8, 42), (16, 30))
        self.add_line('person-legs-2', (16, 30), (26, 30))
        self.add_line('person-legs-3', (26, 30), (30, 30))
        self.add_line('stairs-1', (20, 42), (20, 38))
        self.add_line('stairs-2', (20, 38), (30, 38))
        self.add_line('stairs-3', (30, 38), (30, 30))
        self.add_line('stairs-4', (30, 30), (36, 30))
        self.add_line('stairs-5', (36, 30), (36, 24))
        self.add_line('stairs-6', (36, 24), (42, 24))
        self.add_line('forward-arm-0', (18, 22), (26, 22))
        self.add_line('forward-arm-1', (26, 22), (29, 18))
        self.add_contour('person-head', *('person-head-a', 'person-head-b'), closed=True)
        self.add_contour('person-body', *('person-body-1',), closed=False)
        self.add_contour('person-legs', *('person-legs-1', 'person-legs-2', 'person-legs-3'), closed=False)
        self.add_contour('stairs', *('stairs-1', 'stairs-2', 'stairs-3', 'stairs-4', 'stairs-5', 'stairs-6'), closed=False)
        self.add_contour('forward-arm', *('forward-arm-0', 'forward-arm-1'), closed=False)
        self.relate('connect', *('person-body', 'person-arms-1'))
        self.relate('connect', *('person-body', 'person-legs'))
        self.relate('connect', *('stairs', 'person-legs'))
        self.relate('connect', *('forward-arm-0', 'forward-arm-1'))
        self.relate('connect', *('forward-arm-0', 'person-body-1'))
        self.relate('connect', *('forward-arm-0', 'person-arms-1'))
        self.mark_human_figure('person-1', head='person-head', torso='person-body-1', torso_junction='start')
