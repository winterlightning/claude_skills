'Cao Dai eye triangle: retain the triangle and a clear round eye opening; omit the pupil and narrow eyelid layers that cannot fit MIC4.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1a804c88-15f7-4476-b406-236f03484b85'
SOURCE_PATH = 'pictographic-primitives/religion/cao dai_1a804c88-15f7-4476-b406-236f03484b85.svg'
AUTHOR = 'gpt-6'

class CaoDai(Solo48):
    icon_id = 'cao-dai'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'religion'
    aliases = ()
    keywords = ('cao', 'dai', 'religion')

    def build(self) -> None:
        self.add_polyline('triangle',(24,8),(44,40),(4,40),closed=True)

        self.add_dot('pupil',(24,29))
