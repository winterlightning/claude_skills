'Sad face under a hat: preserve the hat, drooping expression and separated eye marks; simplify the short eye strokes.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e8706f48-92e6-456f-814d-96b950152738'
SOURCE_PATH = 'pictographic-primitives/smileys/sad face_e8706f48-92e6-456f-814d-96b950152738.svg'
AUTHOR = 'gpt-6'

class SadFaceE8706f48(Solo48):
    icon_id = 'sad-face-e8706f48'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'smileys'
    categories = ('smileys', 'primitives')
    aliases = ()
    keywords = ('sad', 'face', 'smileys')

    def build(self) -> None:
        self.add_polyline('brim',(6,22),(42,22))
        self.add_bezier('hat',(10,22),((11,12),(12,6),(19,6)),((22,6),(26,6),(29,6)),((36,6),(37,12),(38,22)))
        self.relate('connect','hat','brim')
        self.add_dot('eye-left',(16,31));self.add_dot('eye-right',(32,31))
        self.add_arc('frown',(13,42),(35,42),radius_x=11,radius_y=3)
