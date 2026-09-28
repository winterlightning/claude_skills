'Cao Dai eye triangle: retain the triangle and a clear round eye opening; omit the pupil and narrow eyelid layers that cannot fit MIC4.'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '1a804c88-15f7-4476-b406-236f03484b85'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__cao-dai/20260926T182452Z-thuan-mac-1/reference/cao dai_1a804c88-15f7-4476-b406-236f03484b85.svg'
AUTHOR = 'gpt-6'

class CaoDai(Solo48):
    icon_id = 'cao-dai'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'religion'
    categories = ('primitives', 'religion')
    aliases = ()
    keywords = ('cao', 'dai', 'religion')

    def build(self) -> None:
        self.add_polyline('triangle',(24,8),(44,40),(4,40),closed=True)

        # The reference's defining eye is a lens, rather than a single dot.
        self.add_arc('eye-upper',(21,29),(27,29),radius_x=3,radius_y=3,sweep=True)
        self.add_arc('eye-lower',(27,29),(21,29),radius_x=3,radius_y=3,sweep=True)
        self.add_contour('eye','eye-upper','eye-lower',closed=True)
