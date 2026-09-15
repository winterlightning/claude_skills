'Bear face: retain round ears, clear eyes and an oval muzzle; omit the cramped dot inside the muzzle.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8d5b656b-3421-5a09-b55b-b470ebf0175b'
SOURCE_PATH = 'pictographic-primitives/animals/tiger_8d5b656b-3421-5a09-b55b-b470ebf0175b.svg'
AUTHOR = 'gpt-6'


class BearMuzzleFace(Solo48):
    icon_id = 'bear-muzzle-face'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "nature/animals"
    aliases = ()
    keywords = ('bear', 'face', 'head', 'muzzle', 'nose', 'animal', 'cute', 'wildlife')

    def build(self) -> None:
        self.add_bezier('top-left',(6,12),((6,8),(8,6),(11,6)),((14,6),(16,8),(18,10)))
        self.add_bezier('crown',(18,10),((21,9),(27,9),(30,10)))
        self.add_bezier('top-right',(30,10),((32,8),(34,6),(37,6)),((40,6),(42,8),(42,12)))
        self.add_line('right',(42,12),(42,26))
        self.add_bezier('chin',(42,26),((42,36),(33,42),(24,42)),((15,42),(6,36),(6,26)))
        self.add_line('left',(6,26),(6,12))
        self.add_contour('head','top-left','crown','top-right','right','chin','left',closed=True)
        self.add_dot('eye-left',(16,19));self.add_dot('eye-right',(32,19))

        self.add_arc('muzzle-top', (18,29), (30,29), radius_x=6, radius_y=4)
        self.add_arc('muzzle-bottom', (30,29), (18,29), radius_x=6, radius_y=4)
        self.add_contour('muzzle', 'muzzle-top', 'muzzle-bottom', closed=True)
