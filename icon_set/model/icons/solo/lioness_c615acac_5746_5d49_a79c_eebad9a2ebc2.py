'Lioness face: mirrored rounded ears, cheeks and jaw with a clear central nose. SQUARE preserves natural face proportions.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c615acac-5746-5d49-a79c-eebad9a2ebc2'
SOURCE_PATH = 'pictographic-primitives/animals/lioness_c615acac-5746-5d49-a79c-eebad9a2ebc2.svg'
AUTHOR = 'gpt-6'


class LionessFace(Solo48):
    icon_id = 'lioness-face'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "animals"
    categories = ("animals", "other", "primitives-generate")
    aliases = ()
    keywords = ('lioness', 'face', 'animal')

    def build(self) -> None:
        # Paired ears and cheeks use mirrored continuous curves.
        self.add_bezier('crown',(18,14),((20,12),(22,11),(24,11)),((26,11),(28,12),(30,14)))
        self.add_bezier('right',(30,14),((36,18),(40,20),(40,25)),((40,34),(33,42),(24,42)))
        self.add_bezier('left',(24,42),((15,42),(8,34),(8,25)),((8,20),(12,18),(18,14)))
        self.add_contour('head','crown','right','left',closed=True)
        self.add_arc('ear-left-top',(18,14),(6,14),radius_x=6,radius_y=8,sweep=False)
        self.add_bezier('ear-left-low',(6,14),((6,18),(6,22),(8,25)))
        self.add_contour('ear-left','ear-left-top','ear-left-low')
        self.add_arc('ear-right-top',(30,14),(42,14),radius_x=6,radius_y=8)
        self.add_bezier('ear-right-low',(42,14),((42,18),(42,22),(40,25)))
        self.add_contour('ear-right','ear-right-top','ear-right-low')
        self.relate('connect','ear-left','head')
        self.relate('connect','ear-right','head')
        self.add_polyline('nose',(20,25),(24,29),(28,25))
        self.add_line('philtrum',(24,29),(24,33))
        self.relate('connect','nose','philtrum')
