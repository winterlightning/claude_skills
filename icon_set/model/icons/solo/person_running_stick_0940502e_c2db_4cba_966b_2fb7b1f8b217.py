"""Running Person. Preserves the forward lean and asymmetric running limbs; uses clean deliberate bends.

SQUARE visible extremes (4, 4, 44, 44); centerlines (6, 6, 42, 42).
Lucide person-standing: a detached circular head and shared limb junctions; the supplied reference determines the running pose.
Repeated features share dimensions; deliberate asymmetry preserves the
letter order, handles and chart heights. Authored directly on SOLO48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0940502e-c2db-4cba-966b-2fb7b1f8b217'
SOURCE_PATH = 'pictographic-primitives/symbol/climbing 1_0940502e-c2db-4cba-966b-2fb7b1f8b217.svg'
AUTHOR = 'gpt-6'


class PersonRunningStick(Solo48):
    icon_id = 'person-running-stick'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "symbol"
    aliases = ()
    keywords = ('running', 'person', 'run', 'sport', 'exercise', 'jogging', 'figure', 'activity')

    def build(self) -> None:
        self.add_arc('head-right', (34, 6), (34, 14), radius_x=4, radius_y=4, sweep=True)
        self.add_arc('head-left', (34, 14), (34, 6), radius_x=4, radius_y=4, sweep=True)
        self.add_contour('head', 'head-right', 'head-left', closed=True)
        self.add_line('torso', (26, 20), (20, 30))
        self.add_polyline('back-arm', (26, 20), (16, 16), (8, 22))
        self.add_polyline('front-arm', (26, 20), (34, 28), (42, 28))
        self.add_polyline('front-leg', (20, 30), (28, 36), (28, 42))
        self.add_polyline('back-leg', (20, 30), (14, 36), (6, 34))
        self.relate("connect", 'torso', 'back-arm')
        self.relate("connect", 'torso', 'front-arm')
        self.relate("connect", 'torso', 'front-leg')
        self.relate("connect", 'torso', 'back-leg')
        self.relate("connect", 'back-arm', 'front-arm')
        self.relate("connect", 'front-leg', 'back-leg')
