"""A portable circular saw with top handle, guard and exposed blade; small teeth are reduced to three broad cuts."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6d7f07b0-c4a7-5343-80d4-cc97519098e9'
SOURCE_PATH = 'pictographic-primitives/tools/power tools electric saw_6d7f07b0-c4a7-5343-80d4-cc97519098e9.svg'
AUTHOR = 'gpt-6'

class HandheldCircularSaw(Solo48):
    icon_id = 'handheld-circular-saw'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/tools"
    aliases = ()
    keywords = ('circular saw', 'saw', 'power tool', 'blade', 'cutting', 'woodworking', 'handheld', 'construction')

    def build(self) -> None:
        self.add_arc('guard',(10,28),(42,28),radius_x=16)
        self.add_line('shoe',(6,28),(42,28))
        self.relate('connect','shoe','guard')
        self.add_polyline('handle',(10,28),(6,20),(6,6),(26,6),(26,12))
        self.relate('connect','handle','guard')
        self.relate('connect','handle','shoe')
        self.add_polyline('blade',(14,28),(14,36),(20,36),(20,40),(28,38),(32,42),(36,36),(40,36),(40,28))
        self.relate('connect','blade','shoe')
