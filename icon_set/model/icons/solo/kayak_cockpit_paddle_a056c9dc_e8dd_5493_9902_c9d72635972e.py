"""Kayak with Cockpit and Paddle, re-authored from its reference on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'a056c9dc-e8dd-5493-9902-c9d72635972e'
SOURCE_PATH = 'pictographic-primitives/transportation/kayak_a056c9dc-e8dd-5493-9902-c9d72635972e.svg'
AUTHOR = 'gpt-6'

class KayakCockpitPaddle(Solo48):
    icon_id = 'kayak-cockpit-paddle'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/transportation'
    aliases = ()
    keywords = ('kayak', 'paddle', 'cockpit', 'canoe', 'boat', 'water sports', 'paddling', 'outdoor')

    def build(self) -> None:
        # Height repair: exact SOLO48 keyshape extremes; original subject and stroke retained.
        self.add_arc('hull-right-top', (24, 4), (31, 9), radius_x=35, radius_y=25)
        self.add_arc('hull-right-middle', (31, 9), (38, 24), radius_x=35, radius_y=25)
        self.add_arc('hull-right-bottom', (38, 24), (24, 44), radius_x=35, radius_y=25)
        self.add_arc('hull-left-bottom', (24, 44), (10, 24), radius_x=35, radius_y=25)
        self.add_arc('hull-left-top', (10, 24), (24, 4), radius_x=35, radius_y=25)
        self.add_contour('hull', 'hull-right-top', 'hull-right-middle', 'hull-right-bottom', 'hull-left-bottom', 'hull-left-top', closed=True)
        self.add_line('paddle-shaft', (10, 24), (31, 9))
        self.relate('connect', 'paddle-shaft', 'hull')
        self.add_polyline('blade-left', (10, 24), (8, 28), (8, 32))
        self.add_polyline('blade-right', (31, 9), (36, 4), (40, 4))
        self.relate('connect', 'paddle-shaft', 'blade-left')
        self.relate('connect', 'paddle-shaft', 'blade-right')
        self.relate('connect', 'hull', 'blade-left')
        self.relate('connect', 'hull', 'blade-right')
        self.add_arc('cockpit-a', (24, 26), (24, 32), radius_x=3)
        self.add_arc('cockpit-b', (24, 32), (24, 26), radius_x=3)
        self.add_contour('cockpit', 'cockpit-a', 'cockpit-b', closed=True)
