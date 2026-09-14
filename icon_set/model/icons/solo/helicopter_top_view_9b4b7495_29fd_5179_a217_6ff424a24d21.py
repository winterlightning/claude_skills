"""Helicopter Top View, re-authored from its reference on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '9b4b7495-29fd-5179-a217-6ff424a24d21'
SOURCE_PATH = 'pictographic-primitives/transportation/helicopter top view_9b4b7495-29fd-5179-a217-6ff424a24d21.svg'
AUTHOR = 'gpt-6'

class HelicopterTopView(Solo48):
    icon_id = 'helicopter-top-view'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/transportation'
    aliases = ()
    keywords = ('helicopter', 'top view', 'aerial', 'rotor', 'aircraft', 'chopper', 'aviation', 'overhead')

    def build(self) -> None:
        # Height repair: exact SOLO48 keyshape extremes; original subject and stroke retained.
        self.add_arc('cockpit', (14, 14), (34, 14), radius_x=10)
        self.add_polyline('fuselage', (34, 14), (34, 34), (24, 38), (14, 34), (14, 14))
        self.relate('connect', 'cockpit', 'fuselage')
        self.add_polyline('rotor-a', (8, 8), (14, 14), (24, 24), (34, 34), (40, 40))
        self.add_polyline('rotor-b', (8, 40), (14, 34), (24, 24), (34, 14), (40, 8))
        self.relate('connect', 'rotor-a', 'rotor-b')
        self.relate('connect', 'rotor-a', 'fuselage')
        self.relate('connect', 'rotor-b', 'fuselage')
        self.add_line('tail', (24, 38), (24, 44))
        self.add_polyline('tail-rotor', (18, 44), (24, 44), (30, 44))
        self.relate('connect', 'tail', 'fuselage')
        self.relate('connect', 'tail', 'tail-rotor')
        self.relate('connect', 'cockpit', 'rotor-a')
        self.relate('connect', 'cockpit', 'rotor-b')
