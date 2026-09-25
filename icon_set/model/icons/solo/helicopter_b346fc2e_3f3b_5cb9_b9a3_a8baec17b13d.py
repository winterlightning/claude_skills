"""A right-facing helicopter with a main rotor, forked tail, cockpit divider and landing skid. Broad envelope preserves the long rotor and tail. Lucide helicopter informed the joined fuselage and skid; curved window reduced to one shared divider."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b346fc2e-3f3b-5cb9-b9a3-a8baec17b13d'
SOURCE_PATH = 'pictographic-primitives/transportation/chopper_b346fc2e-3f3b-5cb9-b9a3-a8baec17b13d.svg'
SOURCE_REFERENCES = (('b346fc2e-3f3b-5cb9-b9a3-a8baec17b13d', 'pictographic-primitives/transportation/chopper_b346fc2e-3f3b-5cb9-b9a3-a8baec17b13d.svg'),)
AUTHOR = 'gpt-6'

class Helicopter(Solo48):
    icon_id = 'helicopter'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'transportation'
    categories = ('transportation', 'primitives')
    aliases = ()
    keywords = ('helicopter', 'chopper', 'aircraft', 'rotor', 'flight', 'aviation', 'air transport', 'side view')

    def build(self) -> None:
        self.add_line('roof-a',(20,16),(28,16))
        self.add_line('roof-b',(28,16),(32,16))
        self.add_arc('nose',(32,16),(32,32),radius_x=12,radius_y=8)
        self.add_line('bottom-a',(32,32),(30,32))
        self.add_line('bottom-b',(30,32),(22,32))
        self.add_line('bottom-c',(22,32),(20,32))
        self.add_arc('back-bottom',(20,32),(16,28),radius_x=4)
        self.add_line('back-a',(16,28),(16,24))
        self.add_line('back-b',(16,24),(16,20))
        self.add_arc('back-top',(16,20),(20,16),radius_x=4)
        self.add_contour('cabin','roof-a','roof-b','nose','bottom-a','bottom-b','bottom-c','back-bottom','back-a','back-b','back-top',closed=True)
        self.add_line('window',(32,16),(32,32))
        self.relate('connect','window','cabin')
        self.add_polyline('rotor',(12,8),(28,8),(44,8))
        self.add_line('mast',(28,8),(28,16))
        self.relate('connect','mast','rotor')
        self.relate('connect','mast','cabin')
        self.add_polyline('tail',(4,18),(8,24),(4,30))
        self.add_line('boom',(8,24),(16,24))
        self.relate('connect','boom','tail')
        self.relate('connect','boom','cabin')
        self.add_polyline('skid',(12,40),(22,40),(30,40),(44,40))
        for x in (22,30):
            self.add_line(f'leg-{x}',(x,32),(x,40))
            self.relate('connect',f'leg-{x}','cabin')
            self.relate('connect',f'leg-{x}','skid')
