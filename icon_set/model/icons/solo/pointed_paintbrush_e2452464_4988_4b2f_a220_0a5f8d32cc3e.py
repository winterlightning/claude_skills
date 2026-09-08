"""A diagonal paintbrush with a rounded handle and a broad pointed bristle head."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e2452464-4988-4b2f-a220-0a5f8d32cc3e'
SOURCE_PATH = 'pictographic-primitives/decoration/batch-01/brush_e2452464-4988-4b2f-a220-0a5f8d32cc3e.svg'
AUTHOR = 'gpt-6'


class PointedPaintbrush(Solo48):
    icon_id = 'pointed-paintbrush'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/decoration"
    aliases = ()
    keywords = ('paintbrush', 'brush', 'paint', 'art', 'bristles', 'handle', 'craft')

    def build(self) -> None:
        self.add_line('handle-upper',(20,24),(38,4))
        self.add_arc('handle-tip-a',(38,4),(42,2),radius_x=5)
        self.add_arc('handle-tip-b',(42,2),(46,6),radius_x=4)
        self.add_arc('handle-tip-c',(46,6),(44,10),radius_x=5)
        self.add_line('handle-lower',(44,10),(26,30))
        self.add_line('ferrule',(26,30),(20,24))
        self.add_contour('handle','handle-upper','handle-tip-a','handle-tip-b','handle-tip-c','handle-lower','ferrule',closed=True)
        self.add_arc('bristle-crown',(20,24),(8,32),radius_x=10,sweep=False)
        self.add_arc('bristle-tip',(8,32),(2,46),radius_x=24)
        self.add_arc('bristle-base',(2,46),(22,42),radius_x=20,radius_y=4,sweep=False)
        self.add_arc('bristle-side',(22,42),(26,30),radius_x=11,sweep=False)
        self.add_contour('bristles','bristle-crown','bristle-tip','bristle-base','bristle-side')
        self.relate('connect','handle','bristles')
