'Cheeky smile: round face with paired smiling eyes and a continuous elliptical mouth curve.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '98399b8c-5ee0-5d65-ade4-f5d99b52d90f'
SOURCE_PATH = 'icons-json/smileys/cheeky_98399b8c-5ee0-5d65-ade4-f5d99b52d90f.json'
AUTHOR = 'gpt-6'

class Cheeky(Solo48):
    icon_id = 'cheeky'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'smileys'
    aliases = ()
    keywords = ('cheeky', 'smileys')

    def build(self) -> None:
        self.add_arc('rim-top', (4,24), (44,24), radius_x=20, radius_y=20)
        self.add_arc('rim-bottom', (44,24), (4,24), radius_x=20, radius_y=20)
        self.add_contour('rim', 'rim-top', 'rim-bottom', closed=True)

        # Matched smiling eyes and a broad smooth smile; no elliptical distortion of the face.
        for label,x in (('left',17),('right',31)):
            self.add_arc(label+'-eye',(x-3,20),(x+3,20),radius_x=3,radius_y=2)
        self.add_arc('smile',(16,28),(32,28),radius_x=8,radius_y=6,sweep=False)
