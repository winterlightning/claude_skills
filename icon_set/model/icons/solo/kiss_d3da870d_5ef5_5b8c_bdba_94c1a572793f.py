'kiss-smileys: preserve the expression with balanced eyes and a clear mouth; omit redundant tiny eyebrow or blush marks where the three detail rows could not meet MIC4.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd3da870d-5ef5-5b8c-bdba-94c1a572793f'
SOURCE_PATH = 'icons-json/smileys/kiss_d3da870d-5ef5-5b8c-bdba-94c1a572793f.json'
AUTHOR = 'gpt-6'

class KissSmileys(Solo48):
    icon_id = 'kiss-smileys'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'smileys'
    aliases = ()
    keywords = ('kiss', 'smileys')

    def build(self) -> None:
        self.add_arc('rim-top', (4,24), (44,24), radius_x=20, radius_y=20)
        self.add_arc('rim-bottom', (44,24), (4,24), radius_x=20, radius_y=20)
        self.add_contour('rim', 'rim-top', 'rim-bottom', closed=True)
        self.add_line('eye-left',(15,18),(21,18))
        self.add_arc('eye-right',(29,18),(33,18),radius_x=2,radius_y=2)
        self.add_bezier('mouth',(22,27),((28,27),(28,30),(23,30)),((28,30),(28,33),(22,33)))
