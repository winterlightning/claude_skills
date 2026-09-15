'Human construction repair. Reposition head over the anatomical shoulder. Set head-outline to shoulder centerline separation to exactly 8u. Align the upper torso tangent with its own head center.\nShared reference: icon_set/references/human_ref/full_body_ref.png; busts use human_ref/user.svg.\nLucide person-standing original and atomic-debug inform shared limb junctions. Preserve intentional action-pose asymmetry.\n'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8d3730da-df45-48a8-9d4e-6cf0a350df28'
SOURCE_PATH = 'pictographic-primitives/symbol/cycling_8d3730da-df45-48a8-9d4e-6cf0a350df28.svg'
AUTHOR = 'gpt-6'
HUMAN_CONSTRUCTION = 'stick-figure'

class CyclingVariant2(Solo48):
    icon_id = 'cycling-v2'
    variant_of = 'cycling'
    variant_label = 'Correct human head and torso construction'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbols/standalone'
    aliases = ()
    keywords = ('cycling', 'bicycle', 'bike', 'cyclist', 'sport', 'ride', 'exercise', 'transport')

    def build(self):
        self.add_arc('rear-wheel-right', (11, 32), (11, 42), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_arc('rear-wheel-left', (11, 42), (11, 32), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_arc('front-wheel-right', (37, 32), (37, 42), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_arc('front-wheel-left', (37, 42), (37, 32), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_arc('head-right', (28, 6), (28, 14), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('head-left', (28, 14), (28, 6), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_bezier('rider-1', (28, 22), *(((28.0, 25.0), (19.0, 23.5), (16, 24)),))
        self.add_line('rider-2', (16, 24), (24, 28))
        self.add_line('rider-3', (24, 28), (24, 31))
        self.add_line('arm-1', (28, 22), (30, 23))
        self.add_line('arm-2', (30, 23), (38, 23))
        self.add_contour('rear-wheel', *('rear-wheel-right', 'rear-wheel-left'), closed=True)
        self.add_contour('front-wheel', *('front-wheel-right', 'front-wheel-left'), closed=True)
        self.add_contour('head', *('head-right', 'head-left'), closed=True)
        self.add_contour('rider', *('rider-1', 'rider-2', 'rider-3'), closed=False)
        self.add_contour('arm', *('arm-1', 'arm-2'), closed=False)
        self.relate('connect', *('rider', 'arm'))
        self.mark_human_figure('person-1', head='head', torso='rider-1', torso_junction='start')
