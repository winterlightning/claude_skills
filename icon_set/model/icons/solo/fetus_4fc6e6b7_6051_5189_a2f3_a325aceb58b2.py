"""Curled fetus facing right. VRECT_XL extremes (5,2)-(43,46). Lucide baby informs a dominant rounded head; anatomy is intentionally asymmetric. Fingers and toes omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4fc6e6b7-6051-5189-a2f3-a325aceb58b2'
SOURCE_PATH = 'pictographic-primitives/babies/fetus_4fc6e6b7-6051-5189-a2f3-a325aceb58b2.svg'
AUTHOR = 'gpt-6'

class Fetus(Solo48):
    icon_id = 'fetus'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/maternity'
    aliases = ('embryo',)
    keywords = ('fetus', 'pregnancy', 'unborn', 'womb', 'embryo', 'prenatal', 'baby', 'gestation')

    def build(self) -> None:
        self.add_arc('head-right', (18,2), (31,15), radius_x=13)
        self.add_arc('chin', (31,15), (22,24), radius_x=9)
        self.add_line('neck', (22,24), (19,24))
        self.add_arc('head-left', (5,15), (18,2), radius_x=13)
        self.add_line('back', (5,28), (5,15))
        self.add_arc('spine', (23,46), (5,28), radius_x=18)
        self.add_arc('tucked-leg', (33,41), (23,46), radius_x=13)
        self.add_line('ankle', (38,44), (33,41))
        self.add_arc('foot', (38,34), (38,44), radius_x=5)
        self.add_arc('knee', (35,31), (38,34), radius_x=3)
        self.add_contour('body', 'knee', 'foot', 'ankle', 'tucked-leg', 'spine', 'back', 'head-left', 'head-right', 'chin', 'neck')
        self.add_line('upper-arm', (22,24), (27,27))
        self.add_line('forearm-top', (27,27), (34,21))
        self.add_arc('hand', (34,21), (40,27), radius_x=5)
        self.add_line('forearm-bottom-a', (40,27), (35,31))
        self.add_line('forearm-bottom-b', (35,31), (30,35))
        self.add_arc('elbow', (30,35), (22,35), radius_x=7)
        self.add_line('arm-inner', (22,35), (15,31))
        self.add_contour('arm', 'upper-arm', 'forearm-top', 'hand', 'forearm-bottom-a', 'forearm-bottom-b', 'elbow', 'arm-inner')
        self.relate('connect', 'body', 'arm')
