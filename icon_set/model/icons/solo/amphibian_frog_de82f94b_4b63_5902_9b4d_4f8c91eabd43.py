'Frog head: paired rounded eye bulges and broad curved mouth, fitted exactly to HRECT_L.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'de82f94b-4b63-5902-9b4d-4f8c91eabd43'
SOURCE_PATH = 'pictographic-primitives/animals/amphibian frog_de82f94b-4b63-5902-9b4d-4f8c91eabd43.svg'
AUTHOR = 'gpt-6'


class FrogHead(Solo48):
    icon_id = 'frog-head'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "animals"
    aliases = ()
    keywords = ('frog', 'amphibian', 'head', 'face', 'toad', 'animal', 'pond', 'nature')

    def build(self) -> None:
        # Paired eye bulges share radii; the wide mouth reaches the lower envelope.
        self.add_line('left',(4,28),(4,16))
        self.add_arc('left-eye',(4,16),(20,16),radius_x=8)
        self.add_line('brow',(20,16),(28,16))
        self.add_arc('right-eye',(28,16),(44,16),radius_x=8)
        self.add_line('right',(44,16),(44,28))
        self.add_contour('head','left','left-eye','brow','right-eye','right')
        self.add_arc('mouth-top',(4,28),(44,28),radius_x=20,radius_y=2)
        self.add_arc('mouth-bottom',(44,28),(4,28),radius_x=20,radius_y=12)
        self.add_contour('mouth','mouth-top','mouth-bottom',closed=True)
        self.relate('connect','head','mouth')
