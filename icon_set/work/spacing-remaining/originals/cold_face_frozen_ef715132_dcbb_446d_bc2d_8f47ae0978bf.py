'Frozen face: smooth circular crown, clear eyes and mouth, and deliberate ice points.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ef715132-dcbb-446d-bc2d-8f47ae0978bf'
SOURCE_PATH = 'icons-json/smileys/cold face frozen_ef715132-dcbb-446d-bc2d-8f47ae0978bf.json'
AUTHOR = 'gpt-6'

class ColdFaceFrozen(Solo48):
    icon_id = 'cold-face-frozen'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'smileys'
    aliases = ()
    keywords = ('cold', 'face', 'frozen', 'smileys')

    def build(self):
        # Frozen face: circular crown, balanced eyes and an open neutral mouth above the deliberate ice points.
        l = self.add_line
        p = self.add_polyline
        link = self.relate

        def a(name, start, end, rx, ry=None, sweep=True):
            self.add_arc(name, start, end, radius_x=rx,
                         radius_y=rx if ry is None else ry, sweep=sweep)

        a('face-top',(6,24),(42,24),18)
        p('ice',(42,24),(42,34),(36,42),(30,36),(24,42),(18,36),(12,42),(6,34),(6,24))
        link('connect','face-top','ice')
        l('mouth',(16,27),(32,27))
        for x in (20,28):
            self.add_dot(f'eye-{x}',(x,16))
