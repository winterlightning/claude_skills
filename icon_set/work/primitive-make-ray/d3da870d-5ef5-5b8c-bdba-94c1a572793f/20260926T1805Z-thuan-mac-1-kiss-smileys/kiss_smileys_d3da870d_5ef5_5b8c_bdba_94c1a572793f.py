'kiss-smileys: preserve the expression with balanced eyes and a clear mouth; omit redundant tiny eyebrow or blush marks where the three detail rows could not meet MIC4.'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'd3da870d-5ef5-5b8c-bdba-94c1a572793f'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__kiss-smileys/20260926T175531Z-thuan-mac-1/reference/kiss_d3da870d-5ef5-5b8c-bdba-94c1a572793f.svg'
AUTHOR = 'gpt-6'

class KissSmileys(Solo48):
    icon_id = 'kiss-smileys'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'smileys'
    categories = ('smileys', 'primitives')
    aliases = ()
    keywords = ('kiss', 'smileys')

    def build(self) -> None:
        self.add_arc('rim-top', (4,24), (44,24), radius_x=20, radius_y=20)
        self.add_arc('rim-bottom', (44,24), (4,24), radius_x=20, radius_y=20)
        self.add_contour('rim', 'rim-top', 'rim-bottom', closed=True)
        self.add_line('eye-left',(15,18),(21,18))
        self.add_arc('eye-right',(29,18),(33,18),radius_x=2,radius_y=2)
        self.add_bezier('mouth',(24,26),((29,26),(29,29),(24,30)),((29,31),(29,34),(23,35)))
